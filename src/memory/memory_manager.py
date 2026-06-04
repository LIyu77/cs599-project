"""
记忆管理器 - 使用Chroma向量数据库存储和检索用户偏好
"""

import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime

import chromadb
from chromadb.config import Settings
import requests

from config import get_config


class MemoryManager:
    """记忆管理器类"""

    def __init__(self):
        self.config = get_config()
        self.client = None
        self.collection = None
        self._init_chroma()

    def _init_chroma(self):
        """初始化Chroma向量数据库"""
        try:
            # 创建持久化目录
            persist_dir = self.config.api.CHROMA_PERSIST_DIR
            os.makedirs(persist_dir, exist_ok=True)

            # 初始化Chroma客户端
            self.client = chromadb.PersistentClient(
                path=persist_dir,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )

            # 获取或创建集合
            self.collection = self.client.get_or_create_collection(
                name=self.config.api.CHROMA_COLLECTION_NAME,
                metadata={"description": "用户旅行偏好记忆库"}
            )

            print(f"[OK] Chroma向量数据库初始化成功，集合: {self.config.api.CHROMA_COLLECTION_NAME}")

        except Exception as e:
            print(f"[FAIL] Chroma初始化失败: {e}")
            # 使用内存模式作为备选
            self.client = chromadb.Client()
            self.collection = self.client.get_or_create_collection(
                name=self.config.api.CHROMA_COLLECTION_NAME,
                metadata={"description": "用户旅行偏好记忆库（内存模式）"}
            )

    def _get_embedding(self, text: str) -> List[float]:
        """
        使用智谱AI获取文本的向量嵌入

        Args:
            text: 输入文本

        Returns:
            向量嵌入列表
        """
        try:
            # 调用智谱AI的Embedding API
            url = "https://open.bigmodel.cn/api/paas/v4/embeddings"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api.ZHIPU_API_KEY}"
            }
            data = {
                "model": self.config.model.ZHIPU_EMBEDDING_MODEL,
                "input": text
            }

            response = requests.post(url, headers=headers, json=data, timeout=10)

            if response.status_code == 200:
                result = response.json()
                if "data" in result and len(result["data"]) > 0:
                    return result["data"][0]["embedding"]

            # 如果API调用失败，使用随机向量（仅用于演示）
            import random
            return [random.random() for _ in range(1024)]

        except Exception as e:
            print(f"获取嵌入向量失败: {e}")
            # 使用随机向量作为备选
            import random
            return [random.random() for _ in range(1024)]

    def add_preference(self, user_id: str, preference: Dict[str, Any]) -> bool:
        """
        添加用户偏好到记忆库

        Args:
            user_id: 用户ID
            preference: 偏好信息字典

        Returns:
            是否添加成功
        """
        try:
            # 构建偏好文本
            pref_text = self._build_preference_text(preference)

            # 获取嵌入向量
            embedding = self._get_embedding(pref_text)

            # 生成唯一ID
            doc_id = f"{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

            # 存入向量数据库
            self.collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[pref_text],
                metadatas=[{
                    "user_id": user_id,
                    "timestamp": datetime.now().isoformat(),
                    "preference_type": preference.get("type", "general"),
                    **{k: str(v) for k, v in preference.items() if k != "type"}
                }]
            )

            print(f"[OK] 偏好已添加: {doc_id}")
            return True

        except Exception as e:
            print(f"[FAIL] 添加偏好失败: {e}")
            return False

    def search_preferences(self, user_id: str, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        搜索用户偏好

        Args:
            user_id: 用户ID
            query: 查询文本
            top_k: 返回结果数量

        Returns:
            相关偏好列表
        """
        try:
            # 获取查询的嵌入向量
            query_embedding = self._get_embedding(query)

            # 搜索相似偏好
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                where={"user_id": user_id} if user_id else None
            )

            # 格式化结果
            preferences = []
            if results and results["documents"] and len(results["documents"]) > 0:
                for i, doc in enumerate(results["documents"][0]):
                    pref = {
                        "text": doc,
                        "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                        "distance": results["distances"][0][i] if results["distances"] else 0
                    }
                    preferences.append(pref)

            return preferences

        except Exception as e:
            print(f"[FAIL] 搜索偏好失败: {e}")
            return []

    def get_user_history(self, user_id: str) -> List[Dict[str, Any]]:
        """
        获取用户的历史偏好

        Args:
            user_id: 用户ID

        Returns:
            历史偏好列表
        """
        try:
            # 获取用户的所有偏好
            results = self.collection.get(
                where={"user_id": user_id} if user_id else None,
                include=["documents", "metadatas"]
            )

            # 格式化结果
            history = []
            if results and results["documents"]:
                for i, doc in enumerate(results["documents"]):
                    pref = {
                        "text": doc,
                        "metadata": results["metadatas"][i] if results["metadatas"] else {}
                    }
                    history.append(pref)

            return history

        except Exception as e:
            print(f"[FAIL] 获取历史失败: {e}")
            return []

    def _build_preference_text(self, preference: Dict[str, Any]) -> str:
        """
        构建偏好文本

        Args:
            preference: 偏好字典

        Returns:
            偏好文本
        """
        parts = []

        # 提取关键信息
        if "destination" in preference:
            parts.append(f"目的地: {preference['destination']}")

        if "budget" in preference:
            parts.append(f"预算: {preference['budget']}元")

        if "travel_style" in preference:
            parts.append(f"旅行风格: {preference['travel_style']}")

        if "accommodation" in preference:
            parts.append(f"住宿偏好: {preference['accommodation']}")

        if "cuisine" in preference:
            parts.append(f"美食偏好: {preference['cuisine']}")

        if "activities" in preference:
            parts.append(f"活动偏好: {preference['activities']}")

        if "selected_plan" in preference:
            parts.append(f"选择的方案: {preference['selected_plan']}")

        if "feedback" in preference:
            parts.append(f"反馈: {preference['feedback']}")

        # 如果没有特定字段，使用整个字典
        if not parts:
            parts.append(json.dumps(preference, ensure_ascii=False))

        return "；".join(parts)

    def inject_preferences_to_prompt(self, user_id: str, query: str, top_k: int = 3) -> str:
        """
        将历史偏好注入到提示词中

        Args:
            user_id: 用户ID
            query: 当前查询
            top_k: 检索数量

        Returns:
            格式化的偏好文本
        """
        preferences = self.search_preferences(user_id, query, top_k)

        if not preferences:
            return ""

        # 构建偏好提示
        pref_lines = ["用户历史偏好："]
        for i, pref in enumerate(preferences, 1):
            pref_lines.append(f"{i}. {pref['text']}")

        return "\n".join(pref_lines)

    def clear_user_data(self, user_id: str) -> bool:
        """
        清除用户数据

        Args:
            user_id: 用户ID

        Returns:
            是否清除成功
        """
        try:
            # 获取用户的所有文档ID
            results = self.collection.get(
                where={"user_id": user_id} if user_id else None,
                include=[]
            )

            if results and results["ids"]:
                self.collection.delete(ids=results["ids"])
                print(f"[OK] 已清除用户 {user_id} 的 {len(results['ids'])} 条记录")

            return True

        except Exception as e:
            print(f"[FAIL] 清除数据失败: {e}")
            return False

    def get_collection_stats(self) -> Dict[str, Any]:
        """
        获取集合统计信息

        Returns:
            统计信息字典
        """
        try:
            count = self.collection.count()
            return {
                "collection_name": self.config.api.CHROMA_COLLECTION_NAME,
                "total_documents": count,
                "persist_dir": self.config.api.CHROMA_PERSIST_DIR
            }
        except Exception as e:
            return {"error": str(e)}


# 全局实例
memory_manager = MemoryManager()


def get_memory_manager() -> MemoryManager:
    """获取记忆管理器实例"""
    return memory_manager

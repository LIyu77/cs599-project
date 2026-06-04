"""
智能体基类 - 提供通用功能
"""

import json
from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod

import requests

from config import get_config


class BaseAgent(ABC):
    """智能体基类"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.config = get_config()
        self.tools = []
        self.tool_functions = {}

    def register_tool(self, tool_def: Dict[str, Any], func):
        """
        注册工具函数

        Args:
            tool_def: 工具定义（OpenAI格式）
            func: 工具函数
        """
        self.tools.append(tool_def)
        func_name = tool_def["function"]["name"]
        self.tool_functions[func_name] = func

    def call_llm(self, messages: List[Dict[str, str]], tools: Optional[List[Dict]] = None) -> Dict[str, Any]:
        """
        调用大语言模型

        Args:
            messages: 消息列表
            tools: 工具定义列表

        Returns:
            模型响应
        """
        try:
            url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api.ZHIPU_API_KEY}"
            }

            data = {
                "model": self.config.model.ZHIPU_MODEL,
                "messages": messages,
                "temperature": self.config.model.TEMPERATURE,
                "max_tokens": self.config.model.MAX_TOKENS
            }

            # 添加工具定义
            if tools:
                data["tools"] = tools
                data["tool_choice"] = "auto"

            response = requests.post(url, headers=headers, json=data, timeout=30)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"LLM调用失败: {response.status_code} - {response.text}")
                return {"error": f"API调用失败: {response.status_code}"}

        except Exception as e:
            print(f"LLM调用异常: {e}")
            return {"error": str(e)}

    def execute_tool_call(self, tool_call: Dict[str, Any]) -> str:
        """
        执行工具调用

        Args:
            tool_call: 工具调用信息

        Returns:
            工具执行结果
        """
        func_name = tool_call["function"]["name"]
        arguments = json.loads(tool_call["function"]["arguments"])

        if func_name in self.tool_functions:
            try:
                result = self.tool_functions[func_name](**arguments)
                return result
            except Exception as e:
                return json.dumps({"error": f"工具执行失败: {e}"}, ensure_ascii=False)
        else:
            return json.dumps({"error": f"未找到工具: {func_name}"}, ensure_ascii=False)

    def process_with_tools(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        处理消息并执行工具调用

        Args:
            messages: 消息列表

        Returns:
            最终响应
        """
        # 第一次调用，可能触发工具
        response = self.call_llm(messages, self.tools)

        if "error" in response:
            return response

        # 检查是否有工具调用
        if "choices" in response and len(response["choices"]) > 0:
            choice = response["choices"][0]
            message = choice.get("message", {})

            # 如果有工具调用
            if "tool_calls" in message and message["tool_calls"]:
                # 执行所有工具调用
                tool_results = []
                for tool_call in message["tool_calls"]:
                    result = self.execute_tool_call(tool_call)
                    tool_results.append({
                        "tool_call_id": tool_call["id"],
                        "role": "tool",
                        "content": result
                    })

                # 将工具结果添加到消息中
                messages.append(message)
                messages.extend(tool_results)

                # 第二次调用，获取最终响应
                final_response = self.call_llm(messages)
                return final_response

        return response

    def extract_content(self, response: Dict[str, Any]) -> str:
        """
        从响应中提取内容

        Args:
            response: 模型响应

        Returns:
            内容文本
        """
        if "error" in response:
            return f"错误: {response['error']}"

        if "choices" in response and len(response["choices"]) > 0:
            choice = response["choices"][0]
            message = choice.get("message", {})
            return message.get("content", "")

        return ""

    def parse_json_response(self, content: str) -> Dict[str, Any]:
        """
        解析JSON响应

        Args:
            content: 响应内容

        Returns:
            解析后的字典
        """
        try:
            # 尝试直接解析
            return json.loads(content)
        except json.JSONDecodeError:
            # 尝试提取JSON部分
            import re
            json_match = re.search(r'\{[\s\S]*\}', content)
            if json_match:
                try:
                    return json.loads(json_match.group())
                except json.JSONDecodeError:
                    pass

            # 返回原始内容
            return {"raw_content": content}

    @abstractmethod
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        运行智能体

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        pass

"""
配置文件 - 多智能体旅行规划系统
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class APIConfig:
    """API配置"""
    # 飞猪API
    FLIGGY_API_KEY: str = "sk-NE0H98jhcZ91PxNHXV6NNkbQSnQGndzK"

    # 高德地图API
    AMAP_API_KEY: str = "b9abcb9b529950874961df8bb236cc66"

    # 智谱AI API
    ZHIPU_API_KEY: str = "71e299e253844718aeaa6a74cb033752.7TViGw1pvSLlz3cd"

    # Chroma向量数据库配置
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    CHROMA_COLLECTION_NAME: str = "travel_preferences"


@dataclass
class ModelConfig:
    """模型配置"""
    # 智谱AI模型
    ZHIPU_MODEL: str = "glm-4-flash"
    ZHIPU_EMBEDDING_MODEL: str = "embedding-2"

    # 温度参数
    TEMPERATURE: float = 0.7

    # 最大token数
    MAX_TOKENS: int = 4096


@dataclass
class TravelConfig:
    """旅行配置"""
    # 默认预算范围（元）
    DEFAULT_BUDGET_MIN: int = 1000
    DEFAULT_BUDGET_MAX: int = 10000

    # 默认旅行天数
    DEFAULT_DAYS: int = 3

    # 酒店搜索数量
    HOTEL_COUNT: int = 3

    # 餐厅搜索数量
    RESTAURANT_COUNT: int = 3

    # 景点搜索数量
    ATTRACTION_COUNT: int = 5


@dataclass
class SystemConfig:
    """系统配置"""
    api: APIConfig = None
    model: ModelConfig = None
    travel: TravelConfig = None

    def __post_init__(self):
        self.api = self.api or APIConfig()
        self.model = self.model or ModelConfig()
        self.travel = self.travel or TravelConfig()


# 全局配置实例
config = SystemConfig()


def get_config() -> SystemConfig:
    """获取系统配置"""
    return config


def update_config(**kwargs):
    """更新配置"""
    global config
    for key, value in kwargs.items():
        if hasattr(config.api, key):
            setattr(config.api, key, value)
        elif hasattr(config.model, key):
            setattr(config.model, key, value)
        elif hasattr(config.travel, key):
            setattr(config.travel, key, value)

"""
状态定义 - LangGraph状态管理
"""

from typing import Dict, Any, List, Optional, TypedDict, Annotated
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TravelState:
    """
    旅行规划状态

    包含所有Agent共享的状态信息
    """
    # 用户输入
    user_id: str = "default_user"
    destination: str = ""
    departure: str = ""
    date: str = ""
    days: int = 3
    budget: float = 5000
    preferences: Dict[str, Any] = field(default_factory=dict)

    # Agent输出
    destination_info: Dict[str, Any] = field(default_factory=dict)
    transport_info: Dict[str, Any] = field(default_factory=dict)
    accommodation_info: Dict[str, Any] = field(default_factory=dict)
    budget_analysis: Dict[str, Any] = field(default_factory=dict)

    # 方案生成
    economic_plan: Dict[str, Any] = field(default_factory=dict)
    quality_plan: Dict[str, Any] = field(default_factory=dict)
    efficient_plan: Dict[str, Any] = field(default_factory=dict)

    # 记忆上下文
    memory_context: str = ""

    # 执行状态
    current_step: str = "start"
    errors: List[str] = field(default_factory=list)
    execution_log: List[str] = field(default_factory=list)

    # 时间戳
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "user_id": self.user_id,
            "destination": self.destination,
            "departure": self.departure,
            "date": self.date,
            "days": self.days,
            "budget": self.budget,
            "preferences": self.preferences,
            "destination_info": self.destination_info,
            "transport_info": self.transport_info,
            "accommodation_info": self.accommodation_info,
            "budget_analysis": self.budget_analysis,
            "economic_plan": self.economic_plan,
            "quality_plan": self.quality_plan,
            "efficient_plan": self.efficient_plan,
            "memory_context": self.memory_context,
            "current_step": self.current_step,
            "errors": self.errors,
            "execution_log": self.execution_log,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def update_step(self, step: str, message: str = ""):
        """更新执行步骤"""
        self.current_step = step
        self.updated_at = datetime.now().isoformat()
        log_entry = f"[{self.updated_at}] {step}: {message}" if message else f"[{self.updated_at}] {step}"
        self.execution_log.append(log_entry)

    def add_error(self, error: str):
        """添加错误信息"""
        self.errors.append(error)
        self.execution_log.append(f"[{datetime.now().isoformat()}] ERROR: {error}")

    def get_all_plans(self) -> Dict[str, Dict[str, Any]]:
        """获取所有方案"""
        return {
            "economic": self.economic_plan,
            "quality": self.quality_plan,
            "efficient": self.efficient_plan
        }


def create_initial_state(
    destination: str,
    departure: str = "",
    date: str = "",
    days: int = 3,
    budget: float = 5000,
    user_id: str = "default_user",
    preferences: Dict[str, Any] = None
) -> TravelState:
    """
    创建初始状态

    Args:
        destination: 目的地
        departure: 出发地
        date: 出发日期
        days: 旅行天数
        budget: 预算
        user_id: 用户ID
        preferences: 用户偏好

    Returns:
        初始状态对象
    """
    # 如果没有指定日期，使用明天
    if not date:
        from datetime import datetime, timedelta
        tomorrow = datetime.now() + timedelta(days=1)
        date = tomorrow.strftime("%Y-%m-%d")

    # 如果没有指定出发地
    if not departure:
        departure = "北京"  # 默认出发地

    state = TravelState(
        user_id=user_id,
        destination=destination,
        departure=departure,
        date=date,
        days=days,
        budget=budget,
        preferences=preferences or {}
    )

    state.update_step("initialized", f"创建旅行规划任务: {departure} -> {destination}")

    return state

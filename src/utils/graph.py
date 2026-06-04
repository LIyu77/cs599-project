"""
LangGraph图定义 - 工作流管理
"""

from typing import Dict, Any, List, Callable, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

from .state import TravelState
from agents import (
    DestinationAgent,
    TransportAgent,
    AccommodationAgent,
    BudgetAgent,
    EconomicPlanAgent,
    QualityPlanAgent,
    EfficientPlanAgent
)
from memory import get_memory_manager


class TravelGraph:
    """
    旅行规划工作流图

    实现两层智能体架构：
    1. 前缀智能体层（并行执行）
    2. 方案生成智能体层（并行执行）
    """

    def __init__(self):
        # 初始化智能体
        self.destination_agent = DestinationAgent()
        self.transport_agent = TransportAgent()
        self.accommodation_agent = AccommodationAgent()
        self.budget_agent = BudgetAgent()
        self.economic_agent = EconomicPlanAgent()
        self.quality_agent = QualityPlanAgent()
        self.efficient_agent = EfficientPlanAgent()

        # 记忆管理器
        self.memory_manager = get_memory_manager()

        # 执行历史
        self.execution_history: List[Dict[str, Any]] = []

    def _retrieve_memory(self, state: TravelState) -> TravelState:
        """
        检索用户历史偏好

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        state.update_step("memory_retrieval", "开始检索用户历史偏好")

        try:
            # 检索相关偏好
            query = f"{state.destination}旅行"
            preferences = self.memory_manager.search_preferences(
                state.user_id, query, top_k=3
            )

            if preferences:
                # 构建记忆上下文
                pref_texts = [p["text"] for p in preferences]
                state.memory_context = "用户历史偏好：\n" + "\n".join(f"- {t}" for t in pref_texts)
                state.update_step("memory_retrieval", f"找到{len(preferences)}条相关偏好")
            else:
                state.memory_context = ""
                state.update_step("memory_retrieval", "未找到相关历史偏好")

        except Exception as e:
            state.add_error(f"记忆检索失败: {e}")
            state.memory_context = ""

        return state

    def _run_prefix_agents(self, state: TravelState) -> TravelState:
        """
        并行运行前缀智能体层

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        state.update_step("prefix_agents", "开始并行运行前缀智能体")

        # 定义任务
        tasks = [
            ("destination", self.destination_agent, state),
            ("transport", self.transport_agent, state),
            ("accommodation", self.accommodation_agent, state)
        ]

        # 并行执行
        results = {}
        with ThreadPoolExecutor(max_workers=3) as executor:
            # 提交所有任务
            future_to_name = {
                executor.submit(self._run_agent, agent, state): name
                for name, agent, state in tasks
            }

            # 收集结果
            for future in as_completed(future_to_name):
                name = future_to_name[future]
                try:
                    result = future.result(timeout=60)  # 60秒超时
                    results[name] = result
                    state.update_step("prefix_agents", f"{name} Agent完成")
                except Exception as e:
                    state.add_error(f"{name} Agent执行失败: {e}")
                    results[name] = state

        # 更新状态
        if "destination" in results:
            state.destination_info = results["destination"].get("destination_info", {})
        if "transport" in results:
            state.transport_info = results["transport"].get("transport_info", {})
        if "accommodation" in results:
            state.accommodation_info = results["accommodation"].get("accommodation_info", {})

        state.update_step("prefix_agents", "前缀智能体层完成")

        return state

    def _run_agent(self, agent, state: TravelState) -> Dict[str, Any]:
        """
        运行单个智能体

        Args:
            agent: 智能体实例
            state: 当前状态

        Returns:
            智能体输出
        """
        try:
            result = agent.run(state.to_dict())
            return result
        except Exception as e:
            raise Exception(f"Agent {agent.name} 执行失败: {e}")

    def _run_budget_analysis(self, state: TravelState) -> TravelState:
        """
        运行预算核算

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        state.update_step("budget_analysis", "开始预算核算")

        try:
            result = self.budget_agent.run(state.to_dict())
            state.budget_analysis = result.get("budget_analysis", {})
            state.update_step("budget_analysis", "预算核算完成")
        except Exception as e:
            state.add_error(f"预算核算失败: {e}")

        return state

    def _run_plan_agents(self, state: TravelState) -> TravelState:
        """
        并行运行方案生成智能体层

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        state.update_step("plan_agents", "开始并行生成三套方案")

        # 定义任务
        tasks = [
            ("economic", self.economic_agent, state),
            ("quality", self.quality_agent, state),
            ("efficient", self.efficient_agent, state)
        ]

        # 并行执行
        results = {}
        with ThreadPoolExecutor(max_workers=3) as executor:
            # 提交所有任务
            future_to_name = {
                executor.submit(self._run_agent, agent, state): name
                for name, agent, state in tasks
            }

            # 收集结果
            for future in as_completed(future_to_name):
                name = future_to_name[future]
                try:
                    result = future.result(timeout=60)  # 60秒超时
                    results[name] = result
                    state.update_step("plan_agents", f"{name} 方案生成完成")
                except Exception as e:
                    state.add_error(f"{name} 方案生成失败: {e}")
                    results[name] = state

        # 更新状态
        if "economic" in results:
            state.economic_plan = results["economic"].get("economic_plan", {})
        if "quality" in results:
            state.quality_plan = results["quality"].get("quality_plan", {})
        if "efficient" in results:
            state.efficient_plan = results["efficient"].get("efficient_plan", {})

        state.update_step("plan_agents", "方案生成智能体层完成")

        return state

    def _save_to_memory(self, state: TravelState) -> TravelState:
        """
        保存用户偏好到记忆库

        Args:
            state: 当前状态

        Returns:
            更新后的状态
        """
        state.update_step("memory_save", "开始保存用户偏好")

        try:
            # 构建偏好信息
            preference = {
                "destination": state.destination,
                "budget": state.budget,
                "days": state.days,
                "departure": state.departure,
                "date": state.date
            }

            # 保存到记忆库
            self.memory_manager.add_preference(state.user_id, preference)
            state.update_step("memory_save", "用户偏好已保存")

        except Exception as e:
            state.add_error(f"保存偏好失败: {e}")

        return state

    def run(self, state: TravelState) -> TravelState:
        """
        运行完整的旅行规划工作流

        Args:
            state: 初始状态

        Returns:
            最终状态
        """
        start_time = time.time()

        try:
            # 步骤1: 检索记忆
            state = self._retrieve_memory(state)

            # 步骤2: 并行运行前缀智能体
            state = self._run_prefix_agents(state)

            # 步骤3: 预算核算
            state = self._run_budget_analysis(state)

            # 步骤4: 并行生成三套方案
            state = self._run_plan_agents(state)

            # 步骤5: 保存到记忆库
            state = self._save_to_memory(state)

            # 计算执行时间
            execution_time = time.time() - start_time
            state.update_step("completed", f"旅行规划完成，耗时{execution_time:.2f}秒")

            # 记录执行历史
            self.execution_history.append({
                "timestamp": state.updated_at,
                "destination": state.destination,
                "execution_time": execution_time,
                "success": len(state.errors) == 0
            })

        except Exception as e:
            state.add_error(f"工作流执行失败: {e}")
            state.update_step("error", str(e))

        return state

    def run_async(self, state: TravelState, callback: Callable[[TravelState], None] = None):
        """
        异步运行工作流

        Args:
            state: 初始状态
            callback: 完成回调函数
        """
        import threading

        def _run():
            result = self.run(state)
            if callback:
                callback(result)

        thread = threading.Thread(target=_run)
        thread.start()

        return thread

    def get_execution_history(self) -> List[Dict[str, Any]]:
        """获取执行历史"""
        return self.execution_history


def create_travel_graph() -> TravelGraph:
    """
    创建旅行规划图实例

    Returns:
        TravelGraph实例
    """
    return TravelGraph()

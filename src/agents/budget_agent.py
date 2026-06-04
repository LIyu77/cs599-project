"""
预算核算Agent - 汇总费用并计算预算
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent


class BudgetAgent(BaseAgent):
    """预算核算Agent"""

    def __init__(self):
        super().__init__(
            name="预算核算Agent",
            description="汇总交通、住宿、餐饮、门票费用，计算总预算并与用户预算对比"
        )

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行预算核算Agent"""
        transport_info = state.get("transport_info", {})
        accommodation_info = state.get("accommodation_info", {})
        destination_info = state.get("destination_info", {})
        budget = state.get("budget", 5000)
        days = state.get("days", 3)

        try:
            # 1. 交通费用 - 取最便宜的往返
            transport_cost = 0
            transport_options = []
            if transport_info.get("flights"):
                cheapest = min(transport_info["flights"], key=lambda x: x["price"])
                transport_cost = cheapest["price"] * 2  # 往返
                transport_options.append({"type": "飞机", "name": cheapest["flight_no"], "price": cheapest["price"]})
            if transport_info.get("trains"):
                cheapest = min(transport_info["trains"], key=lambda x: x["price"])
                transport_options.append({"type": "火车", "name": cheapest["train_no"], "price": cheapest["price"]})
            if not transport_cost and transport_options:
                transport_cost = min(o["price"] for o in transport_options) * 2
            elif not transport_cost:
                transport_cost = 500  # 默认

            # 2. 住宿费用
            accommodation_cost = 0
            if accommodation_info.get("hotels"):
                # 取中间价位的酒店
                hotels_sorted = sorted(accommodation_info["hotels"], key=lambda x: x["price_per_night"])
                mid_hotel = hotels_sorted[len(hotels_sorted) // 2]
                accommodation_cost = mid_hotel["price_per_night"] * max(1, days - 1)
            else:
                accommodation_cost = 300 * max(1, days - 1)

            # 3. 餐饮费用
            dining_cost = 0
            if accommodation_info.get("restaurants"):
                avg_price = sum(r["avg_price"] for r in accommodation_info["restaurants"]) / len(accommodation_info["restaurants"])
                dining_cost = avg_price * 3 * days  # 每天3餐
            else:
                dining_cost = 80 * 3 * days

            # 4. 景点门票费用
            attraction_cost = 0
            if destination_info.get("attractions"):
                prices = [a.get("price", 0) for a in destination_info["attractions"] if a.get("price", 0) > 0]
                attraction_cost = sum(sorted(prices)[:3])  # 取前3个收费景点
            else:
                attraction_cost = 150

            # 5. 其他费用（交通、购物等）
            other_cost = 200 * days

            total_cost = transport_cost + accommodation_cost + dining_cost + attraction_cost + other_cost

            # 生成建议
            suggestions = []
            if total_cost > budget:
                over_amount = total_cost - budget
                suggestions.append(f"当前方案超出预算 {over_amount:.0f} 元")
                if transport_cost > budget * 0.3:
                    suggestions.append("建议选择火车代替飞机以节省交通费用")
                if accommodation_cost > budget * 0.35:
                    suggestions.append("建议选择经济型酒店以节省住宿费用")
            else:
                remaining = budget - total_cost
                suggestions.append(f"当前方案在预算内，剩余 {remaining:.0f} 元可用于购物或升级体验")

            budget_analysis = {
                "expenses": {
                    "transport": transport_cost,
                    "accommodation": accommodation_cost,
                    "dining": dining_cost,
                    "attractions": attraction_cost,
                    "others": other_cost,
                },
                "total": total_cost,
                "budget": budget,
                "is_over_budget": total_cost > budget,
                "over_amount": max(0, total_cost - budget),
                "suggestions": suggestions,
                "transport_options": transport_options,
            }

            return {**state, "budget_analysis": budget_analysis}

        except Exception as e:
            return {**state, "budget_analysis": {"error": str(e)}}

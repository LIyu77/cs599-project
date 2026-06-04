"""
经济型方案Agent - 生成低成本旅行方案
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent


class EconomicPlanAgent(BaseAgent):
    """经济型方案Agent"""

    def __init__(self):
        super().__init__(
            name="经济型方案Agent",
            description="从所有选项中挑选价格最低的组合，生成满足基本出行需求的低成本方案"
        )

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行经济型方案Agent"""
        transport_info = state.get("transport_info", {})
        accommodation_info = state.get("accommodation_info", {})
        destination_info = state.get("destination_info", {})
        budget_analysis = state.get("budget_analysis", {})
        destination = state.get("destination", "")
        departure = state.get("departure", "")
        days = state.get("days", 3)
        date = state.get("date", "")

        try:
            # 1. 选择最便宜的交通
            transport_choice = None
            transport_reason = ""
            if transport_info.get("trains"):
                cheapest_train = min(transport_info["trains"], key=lambda x: x["price"])
                transport_choice = cheapest_train
                transport_reason = f"选择{cheapest_train['train_no']}次列车，价格最低仅需{cheapest_train['price']}元"
            elif transport_info.get("flights"):
                cheapest_flight = min(transport_info["flights"], key=lambda x: x["price"])
                transport_choice = cheapest_flight
                transport_reason = f"选择{cheapest_flight['flight_no']}航班，价格最低{cheapest_flight['price']}元"

            # 2. 选择最便宜的住宿
            hotel_choice = None
            hotel_reason = ""
            if accommodation_info.get("hotels"):
                hotel_choice = min(accommodation_info["hotels"], key=lambda x: x["price_per_night"])
                hotel_reason = f"选择{hotel_choice['name']}，每晚仅需{hotel_choice['price_per_night']}元，性价比最高"

            # 3. 选择最便宜的餐厅
            restaurant_choices = []
            restaurant_reason = ""
            if accommodation_info.get("restaurants"):
                restaurant_choices = sorted(accommodation_info["restaurants"], key=lambda x: x["avg_price"])[:2]
                restaurant_reason = f"选择人均{restaurant_choices[0]['avg_price']}元的{restaurant_choices[0]['name']}等经济实惠餐厅"

            # 4. 选择免费/低价景点
            attraction_choices = []
            attraction_reason = ""
            if destination_info.get("attractions"):
                # 优先免费景点
                free_attractions = [a for a in destination_info["attractions"] if a.get("price", 0) == 0]
                paid_attractions = sorted(
                    [a for a in destination_info["attractions"] if a.get("price", 0) > 0],
                    key=lambda x: x.get("price", 0)
                )
                attraction_choices = free_attractions[:2] + paid_attractions[:1]
                attraction_reason = f"优先选择{'、'.join(a['name'] for a in free_attractions[:2])}等免费景点"

            # 5. 计算总费用
            transport_cost = transport_choice["price"] * 2 if transport_choice else 500
            hotel_cost = hotel_choice["price_per_night"] * max(1, days - 1) if hotel_choice else 200 * (days - 1)
            dining_cost = sum(r["avg_price"] for r in restaurant_choices) * 3 if restaurant_choices else 50 * 3 * days
            attraction_cost = sum(a.get("price", 0) for a in attraction_choices)
            total_cost = transport_cost + hotel_cost + dining_cost + attraction_cost + 100 * days  # 其他费用

            # 6. 生成行程
            itinerary = self._generate_itinerary(destination, days, attraction_choices, restaurant_choices, date)

            economic_plan = {
                "plan_name": f"{destination}经济实惠之旅",
                "plan_type": "经济型",
                "total_budget": round(total_cost),
                "transport": {
                    "choice": transport_choice,
                    "reason": transport_reason,
                },
                "accommodation": {
                    "choice": hotel_choice,
                    "reason": hotel_reason,
                },
                "dining": {
                    "choices": restaurant_choices,
                    "reason": restaurant_reason,
                },
                "attractions": {
                    "choices": attraction_choices,
                    "reason": attraction_reason,
                },
                "itinerary": itinerary,
                "tips": [
                    f"提前预订{departure}到{destination}的火车票可享受折扣",
                    "选择当地人常去的小吃街，既便宜又地道",
                    "利用公共交通出行，节省打车费用",
                    "关注景点免费开放日和优惠政策",
                ],
            }

            return {**state, "economic_plan": economic_plan}

        except Exception as e:
            return {**state, "economic_plan": {"error": str(e)}}

    def _generate_itinerary(self, destination: str, days: int, attractions: List, restaurants: List, start_date: str) -> List[Dict]:
        """生成行程安排"""
        from datetime import datetime, timedelta

        itinerary = []
        start = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.now()

        for day in range(1, days + 1):
            current_date = start + timedelta(days=day - 1)
            day_plan = {
                "day": day,
                "date": current_date.strftime("%m月%d日"),
                "activities": [],
            }

            if day == 1:
                day_plan["activities"] = [
                    {"time": "上午", "activity": f"从出发地抵达{destination}，办理入住", "location": "酒店"},
                    {"time": "下午", "activity": "休息调整，周边闲逛感受当地氛围", "location": "酒店周边"},
                    {"time": "晚上", "activity": f"品尝当地特色美食", "location": restaurants[0]["name"] if restaurants else "当地餐厅"},
                ]
            elif day == days:
                day_plan["activities"] = [
                    {"time": "上午", "activity": "退房，购买当地特产作为纪念", "location": "酒店/商店"},
                    {"time": "下午", "activity": f"返程，结束愉快的{destination}之旅", "location": "交通枢纽"},
                ]
            else:
                attr = attractions[min(day - 2, len(attractions) - 1)] if attractions else None
                rest = restaurants[min(day - 1, len(restaurants) - 1)] if restaurants else None
                day_plan["activities"] = [
                    {"time": "上午", "activity": f"游览{attr['name']}" if attr else f"探索{destination}", "location": attr["name"] if attr else destination},
                    {"time": "下午", "activity": f"继续游览{attr['name']}" if attr else "自由活动", "location": attr["name"] if attr else destination},
                    {"time": "晚上", "activity": f"在{rest['name']}享用晚餐" if rest else "品尝当地美食", "location": rest["name"] if rest else "餐厅"},
                ]

            itinerary.append(day_plan)

        return itinerary

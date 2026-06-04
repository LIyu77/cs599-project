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

            # 3. 选择最便宜的餐厅（根据天数选择更多餐厅）
            restaurant_choices = []
            restaurant_reason = ""
            if accommodation_info.get("restaurants"):
                # 根据天数选择餐厅数量：每天2家
                num_restaurants = min(days * 2, len(accommodation_info["restaurants"]))
                restaurant_choices = sorted(accommodation_info["restaurants"], key=lambda x: x["avg_price"])[:num_restaurants]
                restaurant_reason = f"选择人均{restaurant_choices[0]['avg_price']}元的{restaurant_choices[0]['name']}等{len(restaurant_choices)}家经济实惠餐厅"

            # 4. 选择免费/低价景点（根据天数选择，每天1-2个景点）
            attraction_choices = []
            attraction_reason = ""
            if destination_info.get("attractions"):
                # 优先免费景点
                free_attractions = [a for a in destination_info["attractions"] if a.get("price", 0) == 0]
                paid_attractions = sorted(
                    [a for a in destination_info["attractions"] if a.get("price", 0) > 0],
                    key=lambda x: x.get("price", 0)
                )
                # 根据天数选择景点数量：每天1-2个
                num_attractions = min(days * 2, len(destination_info["attractions"]))
                attraction_choices = free_attractions[:num_attractions // 2] + paid_attractions[:num_attractions // 2]
                attraction_reason = f"优先选择{'、'.join(a['name'] for a in attraction_choices[:3])}等景点"

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

        # 计算每天分配的景点和餐厅数量
        attr_per_day = max(1, len(attractions) // max(1, days - 2)) if attractions else 0
        rest_per_day = max(1, len(restaurants) // max(1, days - 1)) if restaurants else 0

        attr_idx = 0
        rest_idx = 0

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
                rest_idx = 1
            elif day == days:
                day_plan["activities"] = [
                    {"time": "上午", "activity": "退房，购买当地特产作为纪念", "location": "酒店/商店"},
                    {"time": "下午", "activity": f"返程，结束愉快的{destination}之旅", "location": "交通枢纽"},
                ]
            else:
                # 安排上午景点
                morning_attr = attractions[attr_idx] if attr_idx < len(attractions) else None
                if morning_attr:
                    attr_idx += 1

                # 安排下午景点
                afternoon_attr = attractions[attr_idx] if attr_idx < len(attractions) else None
                if afternoon_attr:
                    attr_idx += 1

                # 安排晚餐
                dinner_rest = restaurants[rest_idx] if rest_idx < len(restaurants) else None
                if dinner_rest:
                    rest_idx += 1

                activities = []
                if morning_attr:
                    activities.append({"time": "上午", "activity": f"游览{morning_attr['name']}", "location": morning_attr["name"]})
                else:
                    activities.append({"time": "上午", "activity": f"探索{destination}", "location": destination})

                if afternoon_attr:
                    activities.append({"time": "下午", "activity": f"游览{afternoon_attr['name']}", "location": afternoon_attr["name"]})
                else:
                    activities.append({"time": "下午", "activity": "自由活动", "location": destination})

                if dinner_rest:
                    activities.append({"time": "晚上", "activity": f"在{dinner_rest['name']}享用晚餐", "location": dinner_rest["name"]})
                else:
                    activities.append({"time": "晚上", "activity": "品尝当地美食", "location": "餐厅"})

                day_plan["activities"] = activities

            itinerary.append(day_plan)

        return itinerary

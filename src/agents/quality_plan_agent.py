"""
品质型方案Agent - 生成高品质旅行方案
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent


class QualityPlanAgent(BaseAgent):
    """品质型方案Agent"""

    def __init__(self):
        super().__init__(
            name="品质型方案Agent",
            description="从所有选项中挑选评分最高、特色标签最优的组合，生成注重体验的品质方案"
        )

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行品质型方案Agent"""
        transport_info = state.get("transport_info", {})
        accommodation_info = state.get("accommodation_info", {})
        destination_info = state.get("destination_info", {})
        destination = state.get("destination", "")
        departure = state.get("departure", "")
        days = state.get("days", 3)
        date = state.get("date", "")

        try:
            # 1. 选择最舒适的交通（优先飞机公务舱/高铁一等座）
            transport_choice = None
            transport_reason = ""
            if transport_info.get("flights"):
                # 优先公务舱
                business = [f for f in transport_info["flights"] if f.get("cabin_class") in ["公务舱", "头等舱"]]
                if business:
                    transport_choice = business[0]
                    transport_reason = f"选择{transport_choice['airline']}{transport_choice['flight_no']}航班{transport_choice['cabin_class']}，享受舒适飞行体验"
                else:
                    transport_choice = max(transport_info["flights"], key=lambda x: x["price"])
                    transport_reason = f"选择{transport_choice['airline']}{transport_choice['flight_no']}航班，服务品质有保障"
            elif transport_info.get("trains"):
                # 优先一等座/商务座
                first_class = [t for t in transport_info["trains"] if t.get("seat_type") in ["一等座", "商务座"]]
                if first_class:
                    transport_choice = first_class[0]
                    transport_reason = f"选择{transport_choice['train_no']}次列车{transport_choice['seat_type']}，宽敞舒适"
                else:
                    transport_choice = max(transport_info["trains"], key=lambda x: x["price"])
                    transport_reason = f"选择{transport_choice['train_no']}次列车，品质出行"

            # 2. 选择评分最高的住宿
            hotel_choice = None
            hotel_reason = ""
            if accommodation_info.get("hotels"):
                hotel_choice = max(accommodation_info["hotels"], key=lambda x: x["rating"])
                hotel_reason = f"选择{hotel_choice['name']}，评分{hotel_choice['rating']}分，{hotel_choice['type']}，设施完善"

            # 3. 选择评分最高的餐厅
            restaurant_choices = []
            restaurant_reason = ""
            if accommodation_info.get("restaurants"):
                restaurant_choices = sorted(accommodation_info["restaurants"], key=lambda x: x["rating"], reverse=True)[:3]
                restaurant_reason = f"精选{restaurant_choices[0]['name']}等{len(restaurant_choices)}家高评分特色餐厅"

            # 4. 选择评分最高的景点
            attraction_choices = []
            attraction_reason = ""
            if destination_info.get("attractions"):
                attraction_choices = sorted(destination_info["attractions"], key=lambda x: x.get("rating", 0), reverse=True)[:4]
                names = '、'.join(a['name'] for a in attraction_choices[:3])
                attraction_reason = f"深度游览{names}等必去景点"

            # 5. 计算总费用
            transport_cost = transport_choice["price"] * 2 if transport_choice else 1500
            hotel_cost = hotel_choice["price_per_night"] * max(1, days - 1) if hotel_choice else 800 * (days - 1)
            dining_cost = sum(r["avg_price"] for r in restaurant_choices) * 2 if restaurant_choices else 150 * 2 * days
            attraction_cost = sum(a.get("price", 0) for a in attraction_choices)
            total_cost = transport_cost + hotel_cost + dining_cost + attraction_cost + 300 * days

            # 6. 生成行程
            itinerary = self._generate_itinerary(destination, days, attraction_choices, restaurant_choices, hotel_choice, date)

            quality_plan = {
                "plan_name": f"{destination}品质尊享之旅",
                "plan_type": "品质型",
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
                "highlights": [
                    f"入住{hotel_choice['name']}，享受{hotel_choice['type']}住宿体验" if hotel_choice else "高品质住宿体验",
                    f"品尝{restaurant_choices[0]['name']}等当地顶级美食" if restaurant_choices else "精选特色美食",
                    f"深度游览{attraction_choices[0]['name']}等核心景点" if attraction_choices else "深度景点体验",
                    "全程舒适交通，尊享出行体验",
                ],
            }

            return {**state, "quality_plan": quality_plan}

        except Exception as e:
            return {**state, "quality_plan": {"error": str(e)}}

    def _generate_itinerary(self, destination: str, days: int, attractions: List, restaurants: List, hotel: Dict, start_date: str) -> List[Dict]:
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
                    {"time": "上午", "activity": f"抵达{destination}，专车接送至酒店", "location": "机场/车站"},
                    {"time": "下午", "activity": f"入住{hotel['name'] if hotel else '酒店'}，享受酒店设施", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "晚上", "activity": f"在{restaurants[0]['name'] if restaurants else '餐厅'}享用欢迎晚宴", "location": restaurants[0]["name"] if restaurants else "餐厅"},
                ]
            elif day == days:
                day_plan["activities"] = [
                    {"time": "上午", "activity": "享用精致早餐，退房", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "下午", "activity": f"专车送至机场/车站，结束{destination}品质之旅", "location": "交通枢纽"},
                ]
            else:
                attr = attractions[min(day - 2, len(attractions) - 1)] if attractions else None
                rest = restaurants[min(day - 1, len(restaurants) - 1)] if restaurants else None
                day_plan["activities"] = [
                    {"time": "上午", "activity": f"深度游览{attr['name']}" if attr else f"探索{destination}", "location": attr["name"] if attr else destination},
                    {"time": "下午", "activity": f"继续体验{attr['name']}周边" if attr else "享受当地特色体验", "location": attr["name"] if attr else destination},
                    {"time": "晚上", "activity": f"在{rest['name']}品尝{rest['cuisine']}美食" if rest else "品尝特色美食", "location": rest["name"] if rest else "餐厅"},
                ]

            itinerary.append(day_plan)

        return itinerary

"""
高效型方案Agent - 生成时间效率最优的旅行方案
"""

import re
from typing import Dict, Any, List
from .base_agent import BaseAgent


class EfficientPlanAgent(BaseAgent):
    """高效型方案Agent"""

    def __init__(self):
        super().__init__(
            name="高效型方案Agent",
            description="从所有选项中挑选总耗时最短的组合，生成时间效率最优的方案"
        )

    def _parse_duration(self, duration_str: str) -> int:
        """解析时长字符串为分钟数"""
        hours = 0
        minutes = 0
        hour_match = re.search(r'(\d+)\s*小时', duration_str)
        if hour_match:
            hours = int(hour_match.group(1))
        min_match = re.search(r'(\d+)\s*分钟', duration_str)
        if min_match:
            minutes = int(min_match.group(1))
        return hours * 60 + minutes

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行高效型方案Agent"""
        transport_info = state.get("transport_info", {})
        accommodation_info = state.get("accommodation_info", {})
        destination_info = state.get("destination_info", {})
        destination = state.get("destination", "")
        departure = state.get("departure", "")
        days = state.get("days", 3)
        date = state.get("date", "")

        try:
            # 1. 选择最快的交通
            transport_choice = None
            transport_reason = ""
            all_transport = []
            if transport_info.get("flights"):
                all_transport.extend([{"type": "flight", **f} for f in transport_info["flights"]])
            if transport_info.get("trains"):
                all_transport.extend([{"type": "train", **t} for t in transport_info["trains"]])

            if all_transport:
                transport_choice = min(all_transport, key=lambda x: self._parse_duration(x["duration"]))
                if transport_choice["type"] == "flight":
                    transport_reason = f"选择{transport_choice['airline']}{transport_choice['flight_no']}航班，耗时仅{transport_choice['duration']}，最大化游玩时间"
                else:
                    transport_reason = f"选择{transport_choice['train_no']}次列车，耗时{transport_choice['duration']}，高效出行"

            # 2. 选择位置便利的住宿（评分较高的通常位置好）
            hotel_choice = None
            hotel_reason = ""
            if accommodation_info.get("hotels"):
                hotel_choice = max(accommodation_info["hotels"], key=lambda x: x["rating"])
                hotel_reason = f"选择{hotel_choice['name']}，评分{hotel_choice['rating']}分，位置便利，减少通勤时间"

            # 3. 选择评分高的餐厅（通常服务快）
            restaurant_choices = []
            restaurant_reason = ""
            if accommodation_info.get("restaurants"):
                # 根据天数选择餐厅数量：每天2家
                num_restaurants = min(days * 2, len(accommodation_info["restaurants"]))
                restaurant_choices = sorted(accommodation_info["restaurants"], key=lambda x: x["rating"], reverse=True)[:num_restaurants]
                restaurant_reason = f"选择{restaurant_choices[0]['name']}等{len(restaurant_choices)}家高评分餐厅，服务高效"

            # 4. 选择位置集中的景点（根据天数选择更多景点）
            attraction_choices = []
            attraction_reason = ""
            if destination_info.get("attractions"):
                # 根据天数选择景点数量：每天2个
                num_attractions = min(days * 2, len(destination_info["attractions"]))
                attraction_choices = sorted(destination_info["attractions"], key=lambda x: x.get("rating", 0), reverse=True)[:num_attractions]
                names = '、'.join(a['name'] for a in attraction_choices[:3])
                attraction_reason = f"精选{names}等{len(attraction_choices)}个核心景点，路线优化减少往返"

            # 5. 计算总费用
            transport_cost = transport_choice["price"] * 2 if transport_choice else 800
            hotel_cost = hotel_choice["price_per_night"] * max(1, days - 1) if hotel_choice else 400 * (days - 1)
            dining_cost = sum(r["avg_price"] for r in restaurant_choices) * 2 if restaurant_choices else 100 * 2 * days
            attraction_cost = sum(a.get("price", 0) for a in attraction_choices)
            total_cost = transport_cost + hotel_cost + dining_cost + attraction_cost + 200 * days

            # 6. 生成行程
            itinerary = self._generate_itinerary(destination, days, attraction_choices, restaurant_choices, hotel_choice, date)

            efficient_plan = {
                "plan_name": f"{destination}高效畅游之旅",
                "plan_type": "高效型",
                "total_budget": round(total_cost),
                "total_time_saved": "相比其他方案节省约2-3小时交通时间",
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
                "time_saving_tips": [
                    "提前在线购买景点门票，避免现场排队",
                    "选择地铁等公共交通，避免堵车浪费时间",
                    "在景点附近用餐，减少往返路程",
                    "合理规划游览顺序，避免走回头路",
                ],
            }

            return {**state, "efficient_plan": efficient_plan}

        except Exception as e:
            return {**state, "efficient_plan": {"error": str(e)}}

    def _generate_itinerary(self, destination: str, days: int, attractions: List, restaurants: List, hotel: Dict, start_date: str) -> List[Dict]:
        """生成行程安排"""
        from datetime import datetime, timedelta

        itinerary = []
        start = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.now()

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
                # 安排第一天
                morning_attr = attractions[attr_idx] if attr_idx < len(attractions) else None
                if morning_attr:
                    attr_idx += 1

                dinner_rest = restaurants[rest_idx] if rest_idx < len(restaurants) else None
                if dinner_rest:
                    rest_idx += 1

                day_plan["activities"] = [
                    {"time": "08:00-12:00", "activity": f"乘坐最早班次抵达{destination}", "location": "机场/车站"},
                    {"time": "12:00-13:00", "activity": f"在{restaurants[rest_idx]['name'] if rest_idx < len(restaurants) else '餐厅'}快速午餐", "location": restaurants[rest_idx]["name"] if rest_idx < len(restaurants) else "餐厅"},
                    {"time": "13:00-14:00", "activity": f"入住{hotel['name'] if hotel else '酒店'}，放置行李", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "14:00-18:00", "activity": f"游览{morning_attr['name']}" if morning_attr else f"探索{destination}", "location": morning_attr["name"] if morning_attr else destination},
                    {"time": "18:00-19:30", "activity": f"在{dinner_rest['name']}晚餐" if dinner_rest else "晚餐", "location": dinner_rest["name"] if dinner_rest else "餐厅"},
                ]
                if dinner_rest:
                    rest_idx += 1
            elif day == days:
                day_plan["activities"] = [
                    {"time": "08:00-09:00", "activity": "早餐，退房", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "09:00-12:00", "activity": "最后游览或购买纪念品", "location": "景点/商店"},
                    {"time": "12:00-13:00", "activity": "午餐", "location": "餐厅"},
                    {"time": "13:00-14:00", "activity": "前往交通枢纽", "location": "机场/车站"},
                    {"time": "14:00起", "activity": f"返程，结束{destination}之旅", "location": "飞机/火车"},
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

                # 安排午餐
                lunch_rest = restaurants[rest_idx] if rest_idx < len(restaurants) else None
                if lunch_rest:
                    rest_idx += 1

                # 安排晚餐
                dinner_rest = restaurants[rest_idx] if rest_idx < len(restaurants) else None
                if dinner_rest:
                    rest_idx += 1

                day_plan["activities"] = [
                    {"time": "08:00-09:00", "activity": "早餐", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "09:00-12:00", "activity": f"游览{morning_attr['name']}" if morning_attr else f"探索{destination}", "location": morning_attr["name"] if morning_attr else destination},
                    {"time": "12:00-13:00", "activity": f"在{lunch_rest['name']}午餐" if lunch_rest else "午餐", "location": lunch_rest["name"] if lunch_rest else "餐厅"},
                    {"time": "13:00-17:00", "activity": f"继续游览{afternoon_attr['name']}" if afternoon_attr else "自由活动", "location": afternoon_attr["name"] if afternoon_attr else destination},
                    {"time": "17:00-18:00", "activity": "返回酒店休息", "location": hotel["name"] if hotel else "酒店"},
                    {"time": "18:00-19:30", "activity": f"在{dinner_rest['name']}晚餐" if dinner_rest else "晚餐", "location": dinner_rest["name"] if dinner_rest else "餐厅"},
                ]

            itinerary.append(day_plan)

        return itinerary

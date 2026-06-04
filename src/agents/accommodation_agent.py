"""
食宿筛选Agent - 使用Function Calling搜索酒店和餐厅
"""

import json
from typing import Dict, Any
from .base_agent import BaseAgent
from tools import search_hotels, search_restaurants, search_attractions
from memory import get_memory_manager


class AccommodationAgent(BaseAgent):
    """食宿筛选Agent"""

    def __init__(self):
        super().__init__(
            name="食宿筛选Agent",
            description="通过智谱AI + Function Calling，自主决定搜索酒店和餐厅的时机与关键词"
        )

        # 注册工具
        self.register_tool(
            {
                "type": "function",
                "function": {
                    "name": "search_hotels",
                    "description": "搜索酒店信息，获取酒店名称、价格、评分、设施等信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "城市名称"},
                            "check_in": {"type": "string", "description": "入住日期(YYYY-MM-DD)"},
                            "check_out": {"type": "string", "description": "离店日期(YYYY-MM-DD)"},
                            "count": {"type": "integer", "description": "返回数量", "default": 3},
                        },
                        "required": ["city", "check_in", "check_out"],
                    },
                },
            },
            search_hotels,
        )

        self.register_tool(
            {
                "type": "function",
                "function": {
                    "name": "search_restaurants",
                    "description": "搜索餐厅信息，获取餐厅名称、菜系、价格、评分等信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "城市名称"},
                            "count": {"type": "integer", "description": "返回数量", "default": 3},
                        },
                        "required": ["city"],
                    },
                },
            },
            search_restaurants,
        )

        self.memory_manager = get_memory_manager()

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行食宿筛选Agent"""
        destination = state.get("destination", "")
        date = state.get("date", "")
        days = state.get("days", 3)
        user_id = state.get("user_id", "default_user")

        if not destination:
            return {**state, "accommodation_info": {"error": "未提供目的地"}}

        try:
            # 计算入住和离店日期
            from datetime import datetime, timedelta
            check_in = date
            check_out_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=max(1, days - 1))
            check_out = check_out_date.strftime("%Y-%m-%d")

            # 1. 直接调用工具获取酒店数据
            hotels_result = json.loads(search_hotels(destination, check_in, check_out, 3))
            hotels = []
            for h in hotels_result:
                hotels.append({
                    "name": h["name"],
                    "type": h["type"],
                    "city": h.get("city", destination),
                    "address": h.get("address", ""),
                    "price_per_night": h["price_per_night"],
                    "rating": h["rating"],
                    "review_count": h.get("review_count", 0),
                    "facilities": h.get("facilities", []),
                })

            # 2. 直接调用工具获取餐厅数据（包含早餐、午餐、晚餐推荐）
            restaurants_result = json.loads(search_restaurants(destination, 5))
            restaurants = []
            for r in restaurants_result:
                restaurants.append({
                    "name": r["name"],
                    "cuisine": r["cuisine"],
                    "avg_price": r["avg_price"],
                    "rating": r["rating"],
                    "specialties": r.get("specialties", []),
                    "address": r.get("address", ""),
                })

            # 3. 直接调用工具获取景点数据（7个景点）
            attractions_result = json.loads(search_attractions(destination, 7))
            attractions = []
            for a in attractions_result:
                attractions.append({
                    "name": a["name"],
                    "type": a["type"],
                    "price": a["price"],
                    "rating": a["rating"],
                    "description": a.get("description", ""),
                })

            # 4. 获取用户偏好（如果有的话）
            pref_text = self.memory_manager.inject_preferences_to_prompt(
                user_id, f"{destination}旅行住宿餐饮景点"
            )

            accommodation_info = {
                "hotels": hotels,
                "restaurants": restaurants,
                "attractions": attractions,
                "check_in": check_in,
                "check_out": check_out,
                "days": days,
                "user_preferences": pref_text if pref_text else None,
            }

            return {**state, "accommodation_info": accommodation_info}

        except Exception as e:
            return {**state, "accommodation_info": {"error": str(e)}}

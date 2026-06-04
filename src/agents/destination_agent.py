"""
目的地查询Agent - 获取目的地信息、天气、景点
"""

import json
from typing import Dict, Any
from .base_agent import BaseAgent
from tools import geocode, get_weather, search_poi


class DestinationAgent(BaseAgent):
    """目的地查询Agent"""

    def __init__(self):
        super().__init__(
            name="目的地查询Agent",
            description="将用户输入的模糊地名标准化为精确坐标；获取当地实时天气；查询热门景点信息"
        )

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行目的地查询Agent"""
        destination = state.get("destination", "")
        if not destination:
            return {**state, "destination_info": {"error": "未提供目的地"}}

        try:
            # 1. 地理编码
            geocode_result = json.loads(geocode(destination, destination))
            location_info = {}
            if geocode_result.get("geocodes"):
                g = geocode_result["geocodes"][0]
                location_info = {
                    "name": destination,
                    "formatted_address": g.get("formatted_address", destination),
                    "location": g.get("location", ""),
                    "province": g.get("province", ""),
                    "city": g.get("city", ""),
                }

            # 2. 天气查询
            weather_result = json.loads(get_weather(destination))
            weather_info = {}
            if weather_result.get("lives"):
                w = weather_result["lives"][0]
                weather_info = {
                    "condition": w.get("weather", "未知"),
                    "temperature": w.get("temperature", ""),
                    "humidity": w.get("humidity", ""),
                    "wind": w.get("winddirection", ""),
                }
            if weather_result.get("forecast", {}).get("casts"):
                weather_info["forecast"] = [
                    {
                        "date": c["date"],
                        "day_weather": c["dayweather"],
                        "night_weather": c["nightweather"],
                        "day_temp": c["daytemp"],
                        "night_temp": c["nighttemp"],
                    }
                    for c in weather_result["forecast"]["casts"][:4]
                ]

            # 3. 景点查询
            poi_result = json.loads(search_poi("景点", destination, "", 5))
            attractions = []
            for p in poi_result:
                attractions.append({
                    "name": p["name"],
                    "type": p["type"],
                    "rating": p["rating"],
                    "price": p.get("price", 0),
                    "description": p.get("description", ""),
                    "address": p.get("address", ""),
                })

            destination_info = {
                "location": location_info,
                "weather": weather_info,
                "attractions": attractions,
            }

            return {**state, "destination_info": destination_info}

        except Exception as e:
            return {**state, "destination_info": {"error": str(e)}}

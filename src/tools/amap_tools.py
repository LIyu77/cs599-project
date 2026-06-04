"""
高德地图API工具函数 - 支持真实API调用 + 本地知识库兜底
"""

import json
import random
import requests
from typing import List, Dict, Any
from datetime import datetime, timedelta

from config import get_config


# 复用飞猪工具中的目的地数据库
from tools.fliggy_tools import DESTINATION_DB, _get_city_data


class AmapAPI:
    """高德地图API封装类 - 真实API调用"""

    def __init__(self):
        self.config = get_config().api
        self.api_key = self.config.AMAP_API_KEY
        self.base_url = "https://restapi.amap.com/v3"

        # 城市坐标库（用于本地数据）
        self.city_coords = {
            "北京": {"lng": 116.397428, "lat": 39.90923},
            "上海": {"lng": 121.473701, "lat": 31.230416},
            "广州": {"lng": 113.264385, "lat": 23.129112},
            "深圳": {"lng": 114.057868, "lat": 22.543099},
            "成都": {"lng": 104.065735, "lat": 30.659462},
            "杭州": {"lng": 120.153576, "lat": 30.287459},
            "大理": {"lng": 100.225576, "lat": 25.591276},
            "丽江": {"lng": 100.231695, "lat": 26.872299},
            "西安": {"lng": 108.948024, "lat": 34.263161},
            "三亚": {"lng": 109.508268, "lat": 18.247872},
            "重庆": {"lng": 106.504962, "lat": 29.533155},
            "武汉": {"lng": 114.298572, "lat": 30.584355},
            "南京": {"lng": 118.767413, "lat": 32.041544},
            "厦门": {"lng": 118.112334, "lat": 24.492867},
            "青岛": {"lng": 120.355173, "lat": 36.082982},
            "桂林": {"lng": 110.299121, "lat": 25.274215},
            "拉萨": {"lng": 91.132212, "lat": 29.660361},
            "张家界": {"lng": 110.479191, "lat": 29.117096},
        }

    def geocode(self, address: str, city: str = "") -> str:
        """
        地理编码 - 优先调用高德API，失败时使用本地数据
        """
        # 1. 优先调用真实API
        try:
            params = {
                "key": self.api_key,
                "address": address,
                "city": city
            }
            response = requests.get(f"{self.base_url}/geocode/geo", params=params, timeout=5)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "1" and result.get("geocodes"):
                    print(f"[OK] 高德地理编码API调用成功")
                    return json.dumps(result, ensure_ascii=False)
        except Exception as e:
            print(f"[WARN] 高德地理编码API调用失败: {e}")

        # 2. API失败，使用本地数据
        print(f"[INFO] 使用本地地理编码数据")
        for city_name, coords in self.city_coords.items():
            if city_name in address or city_name in city:
                result = {
                    "status": "1",
                    "info": "OK",
                    "geocodes": [{
                        "formatted_address": f"{city_name}市",
                        "province": city_name,
                        "city": city_name,
                        "location": f"{coords['lng']},{coords['lat']}",
                        "level": "城市",
                    }],
                }
                return json.dumps(result, ensure_ascii=False)

        # 默认
        result = {
            "status": "1",
            "info": "OK",
            "geocodes": [{
                "formatted_address": address,
                "province": city or "未知",
                "city": city or address,
                "location": f"{random.uniform(100, 120):.6f},{random.uniform(20, 40):.6f}",
                "level": "兴趣点",
            }],
        }
        return json.dumps(result, ensure_ascii=False)

    def search_poi(self, keywords: str, city: str, types: str = "", count: int = 5) -> str:
        """
        搜索POI兴趣点 - 优先调用高德API，失败时使用本地数据
        """
        # 1. 优先调用真实API
        try:
            params = {
                "key": self.api_key,
                "keywords": keywords,
                "city": city,
                "types": types,
                "output": "json"
            }
            response = requests.get(f"{self.base_url}/place/text", params=params, timeout=5)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "1" and result.get("pois"):
                    print(f"[OK] 高德POI搜索API调用成功，返回{len(result['pois'])}条结果")
                    return json.dumps(result, ensure_ascii=False)
        except Exception as e:
            print(f"[WARN] 高德POI搜索API调用失败: {e}")

        # 2. API失败，使用本地数据
        print(f"[INFO] 使用本地景点数据: {city}")
        city_data = _get_city_data(city)
        attractions = city_data["attractions"][:count]

        pois = []
        for i, attr in enumerate(attractions):
            coords = self.city_coords.get(city, {"lng": 100 + random.random() * 20, "lat": 25 + random.random() * 15})
            pois.append({
                "id": f"POI{i+1:06d}",
                "name": attr["name"],
                "type": attr["type"],
                "address": f"{city}{attr.get('address', '')}",
                "city": city,
                "location": f"{coords['lng'] + random.uniform(-0.1, 0.1):.6f},{coords['lat'] + random.uniform(-0.1, 0.1):.6f}",
                "rating": attr["rating"],
                "price": attr.get("price", 0),
                "description": attr.get("description", ""),
                "review_count": random.randint(500, 10000),
            })

        return json.dumps(pois, ensure_ascii=False, indent=2)

    def get_weather(self, city: str) -> str:
        """
        获取天气信息 - 优先调用高德API，失败时使用本地数据
        """
        # 1. 优先调用真实API
        try:
            params = {
                "key": self.api_key,
                "city": city,
                "extensions": "all",
                "output": "json"
            }
            response = requests.get(f"{self.base_url}/weather/weatherInfo", params=params, timeout=5)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "1" and result.get("lives"):
                    print(f"[OK] 高德天气API调用成功")
                    return json.dumps(result, ensure_ascii=False)
        except Exception as e:
            print(f"[WARN] 高德天气API调用失败: {e}")

        # 2. API失败，使用本地数据
        print(f"[INFO] 使用本地天气数据: {city}")
        weather_data = {
            "大理": {"condition": "晴", "temp_high": 25, "temp_low": 15, "humidity": 50, "wind": "南风"},
            "丽江": {"condition": "多云", "temp_high": 23, "temp_low": 12, "humidity": 45, "wind": "西南风"},
            "三亚": {"condition": "多云", "temp_high": 32, "temp_low": 26, "humidity": 78, "wind": "东南风"},
            "北京": {"condition": "晴", "temp_high": 32, "temp_low": 22, "humidity": 45, "wind": "北风"},
            "成都": {"condition": "阴", "temp_high": 28, "temp_low": 20, "humidity": 70, "wind": "微风"},
            "西安": {"condition": "晴", "temp_high": 34, "temp_low": 22, "humidity": 40, "wind": "东风"},
            "杭州": {"condition": "小雨", "temp_high": 29, "temp_low": 22, "humidity": 72, "wind": "东风"},
        }

        info = weather_data.get(city, {
            "condition": random.choice(["晴", "多云", "阴", "小雨"]),
            "temp_high": random.randint(20, 35),
            "temp_low": random.randint(10, 25),
            "humidity": random.randint(30, 80),
            "wind": random.choice(["东风", "南风", "西风", "北风"]),
        })

        result = {
            "status": "1",
            "info": "OK",
            "lives": [{
                "city": city,
                "weather": info["condition"],
                "temperature": str(info["temp_high"]),
                "temperature_float": str(info["temp_high"]),
                "humidity": str(info["humidity"]),
                "humidity_float": str(info["humidity"]),
                "winddirection": info["wind"],
                "windpower": str(random.randint(1, 4)),
                "reporttime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }],
            "forecast": {
                "city": city,
                "reporttime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "casts": [
                    {
                        "date": (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
                        "week": str((datetime.now() + timedelta(days=i)).isoweekday()),
                        "dayweather": info["condition"],
                        "nightweather": random.choice(["晴", "多云", "阴"]),
                        "daytemp": str(info["temp_high"] + random.randint(-2, 2)),
                        "nighttemp": str(info["temp_low"] + random.randint(-2, 2)),
                        "daywind": info["wind"],
                        "nightwind": info["wind"],
                        "daypower": str(random.randint(1, 4)),
                        "nightpower": str(random.randint(1, 4)),
                    }
                    for i in range(4)
                ],
            },
        }

        return json.dumps(result, ensure_ascii=False, indent=2)


# 全局实例
amap_api = AmapAPI()


def geocode(address: str, city: str = "") -> str:
    """地理编码"""
    return amap_api.geocode(address, city)


def search_poi(keywords: str, city: str, types: str = "", count: int = 5) -> str:
    """搜索POI"""
    return amap_api.search_poi(keywords, city, types, count)


def get_weather(city: str) -> str:
    """获取天气"""
    return amap_api.get_weather(city)


# Function Calling工具定义
AMAP_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "geocode",
            "description": "将地址转换为经纬度坐标，用于定位和导航",
            "parameters": {
                "type": "object",
                "properties": {
                    "address": {"type": "string", "description": "详细地址，如'北京市天安门'"},
                    "city": {"type": "string", "description": "城市名称，如'北京'", "default": ""},
                },
                "required": ["address"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_poi",
            "description": "搜索兴趣点（POI），包括景点、酒店、餐厅等",
            "parameters": {
                "type": "object",
                "properties": {
                    "keywords": {"type": "string", "description": "搜索关键词，如'故宫'、'酒店'、'餐厅'"},
                    "city": {"type": "string", "description": "城市名称，如'北京'"},
                    "types": {"type": "string", "description": "POI类型", "default": ""},
                    "count": {"type": "integer", "description": "返回数量，默认为5", "default": 5},
                },
                "required": ["keywords", "city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气信息，包括当前天气和未来预报",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如'北京'"},
                },
                "required": ["city"],
            },
        },
    },
]

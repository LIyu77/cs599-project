"""
工具函数层 - 提供API调用功能
"""

from .fliggy_tools import search_flights, search_trains, search_hotels, search_restaurants, search_attractions
from .amap_tools import geocode, search_poi, get_weather

__all__ = [
    'search_flights',
    'search_trains',
    'search_hotels',
    'search_restaurants',
    'search_attractions',
    'geocode',
    'search_poi',
    'get_weather'
]

"""
交通规划Agent - 查询飞机和火车方案
"""

import json
from typing import Dict, Any
from .base_agent import BaseAgent
from tools import search_flights, search_trains


class TransportAgent(BaseAgent):
    """交通规划Agent"""

    def __init__(self):
        super().__init__(
            name="交通规划Agent",
            description="查询出发地到目的地的飞机和火车方案，返回每种方案的时长、价格、承运方"
        )

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """运行交通规划Agent"""
        departure = state.get("departure", "")
        destination = state.get("destination", "")
        date = state.get("date", "")

        if not departure or not destination:
            return {**state, "transport_info": {"error": "未提供出发地或目的地"}}

        try:
            # 1. 查询航班
            flights_result = json.loads(search_flights(departure, destination, date))
            flights = []
            for f in flights_result:
                flights.append({
                    "flight_no": f["flight_no"],
                    "airline": f["airline"],
                    "departure": f["departure"],
                    "destination": f["destination"],
                    "departure_time": f["departure_time"],
                    "arrival_time": f["arrival_time"],
                    "duration": f["duration"],
                    "price": f["price"],
                    "cabin_class": f["cabin_class"],
                    "discount": f.get("discount", 1.0),
                })

            # 2. 查询火车
            trains_result = json.loads(search_trains(departure, destination, date))
            trains = []
            for t in trains_result:
                trains.append({
                    "train_no": t["train_no"],
                    "train_type": t["train_type"],
                    "departure": t["departure"],
                    "destination": t["destination"],
                    "departure_time": t["departure_time"],
                    "arrival_time": t["arrival_time"],
                    "duration": t["duration"],
                    "seat_type": t["seat_type"],
                    "price": t["price"],
                    "tickets_left": t.get("tickets_left", 0),
                })

            # 3. 生成推荐
            cheapest_flight = min(flights, key=lambda x: x["price"]) if flights else None
            cheapest_train = min(trains, key=lambda x: x["price"]) if trains else None
            fastest_flight = min(flights, key=lambda x: self._parse_duration(x["duration"])) if flights else None
            fastest_train = min(trains, key=lambda x: self._parse_duration(x["duration"])) if trains else None

            transport_info = {
                "flights": flights,
                "trains": trains,
                "summary": {
                    "cheapest": self._pick_cheaper(cheapest_flight, cheapest_train),
                    "fastest": self._pick_faster(fastest_flight, fastest_train),
                    "recommended": self._pick_recommended(flights, trains),
                },
            }

            return {**state, "transport_info": transport_info}

        except Exception as e:
            return {**state, "transport_info": {"error": str(e)}}

    def _parse_duration(self, duration_str: str) -> int:
        """解析时长字符串为分钟数"""
        import re
        hours = 0
        minutes = 0
        hour_match = re.search(r'(\d+)\s*小时', duration_str)
        if hour_match:
            hours = int(hour_match.group(1))
        min_match = re.search(r'(\d+)\s*分钟', duration_str)
        if min_match:
            minutes = int(min_match.group(1))
        return hours * 60 + minutes

    def _pick_cheaper(self, flight, train):
        """选择更便宜的"""
        if not flight and not train:
            return None
        if not flight:
            return {"type": "train", **train}
        if not train:
            return {"type": "flight", **flight}
        if train["price"] < flight["price"]:
            return {"type": "train", **train}
        return {"type": "flight", **flight}

    def _pick_faster(self, flight, train):
        """选择更快的"""
        if not flight and not train:
            return None
        if not flight:
            return {"type": "train", **train}
        if not train:
            return {"type": "flight", **flight}
        if self._parse_duration(flight["duration"]) < self._parse_duration(train["duration"]):
            return {"type": "flight", **flight}
        return {"type": "train", **train}

    def _pick_recommended(self, flights, trains):
        """推荐方案：综合考虑价格和时间"""
        all_options = []
        for f in flights:
            score = f["price"] * 0.6 + self._parse_duration(f["duration"]) * 2 * 0.4
            all_options.append({"type": "flight", "score": score, **f})
        for t in trains:
            score = t["price"] * 0.6 + self._parse_duration(t["duration"]) * 2 * 0.4
            all_options.append({"type": "train", "score": score, **t})

        if all_options:
            return min(all_options, key=lambda x: x["score"])
        return None

"""
飞猪API工具函数
"""

import json
import random
from typing import List, Dict, Any
from datetime import datetime


# 目的地知识库
DESTINATION_DB = {
    "大理": {
        "province": "云南",
        "hotels": [
            {"name": "大理古城既下山酒店", "type": "高档型", "price_per_night": 680, "rating": 4.8, "facilities": ["WiFi", "停车场", "餐厅", "观景台"], "address": "大理古城人民路12号"},
            {"name": "洱海天域海景民宿", "type": "特色民宿", "price_per_night": 520, "rating": 4.7, "facilities": ["WiFi", "海景房", "早餐", "自行车"], "address": "大理市海东镇向阳路8号"},
            {"name": "大理青旅背包客栈", "type": "经济型", "price_per_night": 128, "rating": 4.3, "facilities": ["WiFi", "公共厨房", "行李寄存"], "address": "大理古城博爱路56号"},
        ],
        "restaurants": [
            {"name": "段公子·大理私房菜", "cuisine": "云南菜", "avg_price": 88, "rating": 4.7, "specialties": ["酸辣鱼", "乳扇", "鲜花饼"], "address": "大理古城复兴路88号"},
            {"name": "翠田餐厅", "cuisine": "白族菜", "avg_price": 65, "rating": 4.6, "specialties": ["砂锅鱼", "凉鸡米线", "饵块"], "address": "大理古城玉洱路112号"},
            {"name": "坏猴子酒吧餐厅", "cuisine": "融合菜", "avg_price": 52, "rating": 4.4, "specialties": ["汉堡", "意面", "精酿啤酒"], "address": "大理古城人民路46号"},
        ],
        "attractions": [
            {"name": "洱海", "type": "自然风光", "price": 0, "rating": 4.9, "description": "高原湖泊，可骑行环湖，欣赏苍山洱海美景"},
            {"name": "大理古城", "type": "历史文化", "price": 0, "rating": 4.7, "description": "始建于明代，白族文化聚集地，洋人街、人民路步行街"},
            {"name": "崇圣寺三塔", "type": "历史古迹", "price": 75, "rating": 4.8, "description": "大理地标，始建于南诏时期，三塔倒影公园绝美"},
            {"name": "苍山", "type": "自然风光", "price": 35, "rating": 4.7, "description": "十九峰十八溪，可乘坐索道登顶俯瞰洱海"},
            {"name": "双廊古镇", "type": "古镇风情", "price": 0, "rating": 4.6, "description": "洱海东岸最美小镇，杨丽萍太阳宫所在地"},
        ],
    },
    "丽江": {
        "province": "云南",
        "hotels": [
            {"name": "丽江和府洲际度假酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "餐厅"], "address": "丽江古城束河路1号"},
            {"name": "丽江花间堂问云山庄", "type": "特色民宿", "price_per_night": 480, "rating": 4.7, "facilities": ["WiFi", "花园", "茶室", "观景台"], "address": "丽江古城五一街王家庄巷"},
            {"name": "丽江懒猫青旅", "type": "经济型", "price_per_night": 89, "rating": 4.5, "facilities": ["WiFi", "公共厨房", "庭院"], "address": "丽江古城七一街崇仁巷"},
        ],
        "restaurants": [
            {"name": "阿妈意纳西饮食院", "cuisine": "纳西菜", "avg_price": 78, "rating": 4.8, "specialties": ["纳西烤鱼", "鸡豆凉粉", "腊排骨火锅"], "address": "丽江古城五一街兴仁上段"},
            {"name": "88号小吃店", "cuisine": "云南小吃", "avg_price": 35, "rating": 4.6, "specialties": ["米线", "饵丝", "丽江粑粑"], "address": "丽江古城五一街88号"},
            {"name": "滇厨餐厅", "cuisine": "滇菜", "avg_price": 68, "rating": 4.5, "specialties": ["汽锅鸡", "过桥米线", "鲜花饼"], "address": "丽江古城四方街附近"},
        ],
        "attractions": [
            {"name": "丽江古城", "type": "世界文化遗产", "price": 0, "rating": 4.8, "description": "纳西族古镇，小桥流水，夜景迷人"},
            {"name": "玉龙雪山", "type": "自然风光", "price": 100, "rating": 4.9, "description": "海拔5596米，蓝月谷、甘海子等景点"},
            {"name": "束河古镇", "type": "古镇风情", "price": 0, "rating": 4.6, "description": "比丽江古城更安静的纳西古镇"},
            {"name": "拉市海湿地公园", "type": "自然风光", "price": 30, "rating": 4.5, "description": "候鸟栖息地，可骑马、划船"},
            {"name": "虎跳峡", "type": "自然奇观", "price": 65, "rating": 4.7, "description": "世界最深峡谷之一，徒步胜地"},
        ],
    },
    "三亚": {
        "province": "海南",
        "hotels": [
            {"name": "三亚亚特兰蒂斯酒店", "type": "豪华型", "price_per_night": 2800, "rating": 4.9, "facilities": ["水族馆", "水上乐园", "私人沙滩", "SPA"], "address": "三亚市海棠区海棠北路"},
            {"name": "三亚湾红树林度假酒店", "type": "高档型", "price_per_night": 880, "rating": 4.7, "facilities": ["泳池", "沙滩", "餐厅", "健身房"], "address": "三亚市三亚湾路15号"},
            {"name": "三亚大东海海景青旅", "type": "经济型", "price_per_night": 158, "rating": 4.3, "facilities": ["WiFi", "海景", "公共厨房"], "address": "三亚市大东海旅游区"},
        ],
        "restaurants": [
            {"name": "林姐香味海鲜", "cuisine": "海鲜", "avg_price": 158, "rating": 4.8, "specialties": ["清蒸石斑鱼", "椒盐皮皮虾", "蒜蓉扇贝"], "address": "三亚市第一市场"},
            {"name": "嗲嗲的椰子鸡", "cuisine": "海南菜", "avg_price": 98, "rating": 4.7, "specialties": ["椰子鸡", "文昌鸡", "清补凉"], "address": "三亚市解放路"},
            {"name": "琼乡阁海南菜餐厅", "cuisine": "琼菜", "avg_price": 75, "rating": 4.6, "specialties": ["东山羊", "和乐蟹", "加积鸭"], "address": "三亚市河东路"},
        ],
        "attractions": [
            {"name": "亚龙湾", "type": "海滩风光", "price": 0, "rating": 4.9, "description": "天下第一湾，水质清澈，沙滩细腻"},
            {"name": "蜈支洲岛", "type": "海岛风光", "price": 144, "rating": 4.8, "description": "中国马尔代夫，潜水胜地"},
            {"name": "天涯海角", "type": "文化地标", "price": 68, "rating": 4.5, "description": "海南标志性景点，浪漫圣地"},
            {"name": "南山文化旅游区", "type": "佛教文化", "price": 129, "rating": 4.7, "description": "108米海上观音像，祈福圣地"},
            {"name": "呀诺达雨林", "type": "热带雨林", "price": 158, "rating": 4.6, "description": "天然氧吧，踏瀑戏水体验"},
        ],
    },
    "北京": {
        "province": "北京",
        "hotels": [
            {"name": "北京王府井文华东方酒店", "type": "豪华型", "price_per_night": 2200, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "米其林餐厅"], "address": "东城区王府井大街269号"},
            {"name": "北京前门皇家驿栈", "type": "高档型", "price_per_night": 680, "rating": 4.6, "facilities": ["WiFi", "餐厅", "健身房", "商务中心"], "address": "东城区前门大街48号"},
            {"name": "北京三里屯青旅", "type": "经济型", "price_per_night": 168, "rating": 4.4, "facilities": ["WiFi", "公共厨房", "酒吧"], "address": "朝阳区三里屯路"},
        ],
        "restaurants": [
            {"name": "全聚德烤鸭店", "cuisine": "京菜", "avg_price": 168, "rating": 4.6, "specialties": ["烤鸭", "芥末鸭掌", "火燎鸭心"], "address": "东城区前门大街30号"},
            {"name": "海底捞火锅", "cuisine": "火锅", "avg_price": 128, "rating": 4.7, "specialties": ["番茄锅底", "捞派毛肚", "虾滑"], "address": "朝阳区三里屯路19号"},
            {"name": "护国寺小吃", "cuisine": "北京小吃", "avg_price": 35, "rating": 4.5, "specialties": ["豆汁", "焦圈", "驴打滚"], "address": "西城区护国寺大街"},
        ],
        "attractions": [
            {"name": "故宫博物院", "type": "世界文化遗产", "price": 60, "rating": 4.9, "description": "明清两代皇宫，世界五大宫之首"},
            {"name": "八达岭长城", "type": "世界文化遗产", "price": 40, "rating": 4.8, "description": "万里长城最精华段，不到长城非好汉"},
            {"name": "天坛公园", "type": "世界文化遗产", "price": 15, "rating": 4.7, "description": "明清祭天场所，祈年殿为标志"},
            {"name": "颐和园", "type": "皇家园林", "price": 30, "rating": 4.8, "description": "中国最大皇家园林，昆明湖万寿山"},
            {"name": "天安门广场", "type": "文化地标", "price": 0, "rating": 4.7, "description": "世界最大城市广场，升旗仪式必看"},
        ],
    },
    "成都": {
        "province": "四川",
        "hotels": [
            {"name": "成都博舍酒店", "type": "豪华型", "price_per_night": 1500, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "米其林餐厅"], "address": "锦江区笔帖式街81号"},
            {"name": "成都宽窄巷子亚朵酒店", "type": "高档型", "price_per_night": 520, "rating": 4.7, "facilities": ["WiFi", "餐厅", "健身房", "书吧"], "address": "青羊区宽窄巷子附近"},
            {"name": "成都梦之旅青旅", "type": "经济型", "price_per_night": 98, "rating": 4.4, "facilities": ["WiFi", "公共厨房", "天台"], "address": "武侯区锦里附近"},
        ],
        "restaurants": [
            {"name": "大龙燚火锅", "cuisine": "火锅", "avg_price": 108, "rating": 4.7, "specialties": ["麻辣锅底", "鲜毛肚", "鸭肠"], "address": "锦江区春熙路附近"},
            {"name": "陈麻婆豆腐", "cuisine": "川菜", "avg_price": 58, "rating": 4.6, "specialties": ["麻婆豆腐", "回锅肉", "宫保鸡丁"], "address": "青羊区西玉龙街"},
            {"name": "龙抄手总店", "cuisine": "成都小吃", "avg_price": 42, "rating": 4.5, "specialties": ["抄手", "钟水饺", "赖汤圆"], "address": "锦江区春熙路"},
        ],
        "attractions": [
            {"name": "大熊猫繁育研究基地", "type": "自然生态", "price": 55, "rating": 4.8, "description": "近距离观看大熊猫，国宝故乡"},
            {"name": "武侯祠", "type": "历史文化", "price": 50, "rating": 4.7, "description": "三国文化圣地，诸葛亮祠堂"},
            {"name": "锦里古街", "type": "民俗风情", "price": 0, "rating": 4.6, "description": "成都版清明上河图，小吃一条街"},
            {"name": "宽窄巷子", "type": "历史文化", "price": 0, "rating": 4.7, "description": "清朝古街区，成都慢生活代表"},
            {"name": "都江堰", "type": "世界文化遗产", "price": 80, "rating": 4.8, "description": "两千年前水利工程奇迹"},
        ],
    },
    "西安": {
        "province": "陕西",
        "hotels": [
            {"name": "西安威斯汀酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "餐厅"], "address": "碑林区雁塔北路"},
            {"name": "西安钟楼亚朵酒店", "type": "高档型", "price_per_night": 480, "rating": 4.6, "facilities": ["WiFi", "餐厅", "健身房"], "address": "碑林区东大街"},
            {"name": "西安湘子门国际青旅", "type": "经济型", "price_per_night": 89, "rating": 4.5, "facilities": ["WiFi", "公共厨房", "天台"], "address": "碑林区湘子门街"},
        ],
        "restaurants": [
            {"name": "老孙家羊肉泡馍", "cuisine": "陕菜", "avg_price": 48, "rating": 4.7, "specialties": ["羊肉泡馍", "肉夹馍", "凉皮"], "address": "碑林区西大街"},
            {"name": "德发长饺子馆", "cuisine": "饺子宴", "avg_price": 68, "rating": 4.6, "specialties": ["饺子宴", "酸汤水饺", "锅贴"], "address": "碑林区钟鼓楼广场"},
            {"name": "永兴坊美食街", "cuisine": "陕西小吃", "avg_price": 38, "rating": 4.5, "specialties": ["biangbiang面", "肉丸胡辣汤", "甑糕"], "address": "新城区东新街"},
        ],
        "attractions": [
            {"name": "秦始皇兵马俑", "type": "世界文化遗产", "price": 120, "rating": 4.9, "description": "世界第八大奇迹，秦始皇陵陪葬坑"},
            {"name": "西安城墙", "type": "历史古迹", "price": 54, "rating": 4.8, "description": "中国保存最完整古城墙，可骑行"},
            {"name": "大雁塔", "type": "历史古迹", "price": 40, "rating": 4.7, "description": "唐代佛塔，玄奘译经之地"},
            {"name": "华清宫", "type": "历史遗迹", "price": 120, "rating": 4.6, "description": "唐代皇家温泉行宫，长恨歌演出"},
            {"name": "回民街", "type": "美食街区", "price": 0, "rating": 4.5, "description": "西安美食集中地，千年历史"},
        ],
    },
    "杭州": {
        "province": "浙江",
        "hotels": [
            {"name": "杭州西子湖四季酒店", "type": "豪华型", "price_per_night": 2800, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "湖景"], "address": "西湖区灵隐路5号"},
            {"name": "杭州西湖亚朵酒店", "type": "高档型", "price_per_night": 580, "rating": 4.7, "facilities": ["WiFi", "餐厅", "健身房"], "address": "西湖区北山路"},
            {"name": "杭州青旅", "type": "经济型", "price_per_night": 128, "rating": 4.4, "facilities": ["WiFi", "公共厨房", "自行车"], "address": "上城区河坊街"},
        ],
        "restaurants": [
            {"name": "楼外楼", "cuisine": "杭帮菜", "avg_price": 128, "rating": 4.7, "specialties": ["西湖醋鱼", "东坡肉", "龙井虾仁"], "address": "西湖区孤山路30号"},
            {"name": "外婆家", "cuisine": "杭帮菜", "avg_price": 68, "rating": 4.6, "specialties": ["茶香鸡", "麻婆豆腐", "绿茶饼"], "address": "西湖区湖滨路"},
            {"name": "知味观", "cuisine": "杭帮菜", "avg_price": 58, "rating": 4.5, "specialties": ["小笼包", "猫耳朵", "片儿川"], "address": "上城区仁和路"},
        ],
        "attractions": [
            {"name": "西湖", "type": "世界文化遗产", "price": 0, "rating": 4.9, "description": "人间天堂，断桥残雪、三潭印月等十景"},
            {"name": "灵隐寺", "type": "佛教圣地", "price": 75, "rating": 4.8, "description": "江南名刹，飞来峰石窟造像"},
            {"name": "千岛湖", "type": "自然风光", "price": 150, "rating": 4.7, "description": "天下第一秀水，1078个岛屿"},
            {"name": "西溪湿地", "type": "自然生态", "price": 80, "rating": 4.6, "description": "城市湿地，非诚勿扰取景地"},
            {"name": "宋城", "type": "主题公园", "price": 310, "rating": 4.5, "description": "给我一天，还你千年，千古情演出"},
        ],
    },
}


def _get_city_data(city: str) -> Dict[str, Any]:
    """获取城市数据，如果没有则生成默认数据"""
    # 精确匹配
    if city in DESTINATION_DB:
        return DESTINATION_DB[city]

    # 模糊匹配
    for key in DESTINATION_DB:
        if key in city or city in key:
            return DESTINATION_DB[key]

    # 默认数据
    return {
        "province": city,
        "hotels": [
            {"name": f"{city}国际大酒店", "type": "高档型", "price_per_night": 580, "rating": 4.6, "facilities": ["WiFi", "停车场", "餐厅", "健身房"], "address": f"{city}市中心区1号"},
            {"name": f"{city}如家酒店", "type": "舒适型", "price_per_night": 280, "rating": 4.3, "facilities": ["WiFi", "停车场", "早餐"], "address": f"{city}市中心区2号"},
            {"name": f"{city}青年旅舍", "type": "经济型", "price_per_night": 98, "rating": 4.2, "facilities": ["WiFi", "公共厨房"], "address": f"{city}市中心区3号"},
        ],
        "restaurants": [
            {"name": f"{city}特色餐厅", "cuisine": "地方菜", "avg_price": 78, "rating": 4.6, "specialties": ["招牌菜1", "招牌菜2", "招牌菜3"], "address": f"{city}市中心区4号"},
            {"name": f"{city}老字号小吃", "cuisine": "小吃", "avg_price": 38, "rating": 4.5, "specialties": ["特色小吃1", "特色小吃2"], "address": f"{city}市中心区5号"},
            {"name": f"{city}美食广场", "cuisine": "综合", "avg_price": 55, "rating": 4.4, "specialties": ["各地美食"], "address": f"{city}市中心区6号"},
        ],
        "attractions": [
            {"name": f"{city}著名景点1", "type": "风景名胜", "price": 60, "rating": 4.8, "description": f"{city}最著名的景点"},
            {"name": f"{city}著名景点2", "type": "历史文化", "price": 45, "rating": 4.7, "description": f"{city}历史文化景点"},
            {"name": f"{city}著名景点3", "type": "自然风光", "price": 30, "rating": 4.6, "description": f"{city}自然风光景点"},
            {"name": f"{city}公园", "type": "休闲公园", "price": 0, "rating": 4.5, "description": f"{city}市民休闲公园"},
            {"name": f"{city}博物馆", "type": "博物馆", "price": 0, "rating": 4.4, "description": f"{city}地方博物馆"},
        ],
    }


def search_flights(departure: str, destination: str, date: str) -> str:
    """搜索航班"""
    airlines = ["中国国航", "东方航空", "南方航空", "海南航空", "厦门航空", "四川航空"]
    flight_types = ["经济舱", "公务舱", "头等舱"]

    flights = []
    for i in range(random.randint(3, 5)):
        dep_hour = random.randint(6, 21)
        duration_hours = random.randint(1, 4)
        duration_mins = random.randint(0, 59)
        arr_hour = min(dep_hour + duration_hours, 23)

        base_price = 400 + duration_hours * 200
        cabin = random.choice(flight_types)
        if cabin == "公务舱":
            base_price *= 2.5
        elif cabin == "头等舱":
            base_price *= 4

        flights.append({
            "flight_no": f"{'CA' if i % 3 == 0 else 'MU' if i % 3 == 1 else 'CZ'}{random.randint(1000, 9999)}",
            "airline": random.choice(airlines),
            "departure": departure,
            "destination": destination,
            "departure_time": f"{dep_hour:02d}:{random.choice(['00', '15', '30', '45'])}",
            "arrival_time": f"{arr_hour:02d}:{random.choice(['00', '15', '30', '45'])}",
            "duration": f"{duration_hours}小时{duration_mins}分钟",
            "price": int(base_price * random.uniform(0.8, 1.2)),
            "cabin_class": cabin,
            "discount": round(random.uniform(0.7, 1.0), 2),
        })

    return json.dumps(sorted(flights, key=lambda x: x["price"]), ensure_ascii=False)


def search_trains(departure: str, destination: str, date: str) -> str:
    """搜索火车"""
    train_types = ["G", "D", "K", "T", "Z"]
    seat_types = ["二等座", "一等座", "商务座", "硬卧", "软卧"]

    trains = []
    for i in range(random.randint(3, 5)):
        t_type = random.choice(train_types[:2])  # 优先高铁动车
        dep_hour = random.randint(6, 20)
        duration_hours = random.randint(2, 8)
        duration_mins = random.randint(0, 59)
        arr_hour = min(dep_hour + duration_hours, 23)

        if t_type in ["G", "D"]:
            base_price = 200 + duration_hours * 80
            seat = random.choice(["二等座", "一等座"])
        else:
            base_price = 100 + duration_hours * 50
            seat = random.choice(["硬卧", "软卧", "硬座"])

        trains.append({
            "train_no": f"{t_type}{random.randint(100, 9999)}",
            "train_type": t_type,
            "departure": departure,
            "destination": destination,
            "departure_time": f"{dep_hour:02d}:{random.choice(['00', '15', '30', '45'])}",
            "arrival_time": f"{arr_hour:02d}:{random.choice(['00', '15', '30', '45'])}",
            "duration": f"{duration_hours}小时{duration_mins}分钟",
            "seat_type": seat,
            "price": int(base_price * random.uniform(0.9, 1.1)),
            "tickets_left": random.randint(10, 200),
        })

    return json.dumps(sorted(trains, key=lambda x: x["price"]), ensure_ascii=False)


def search_hotels(city: str, check_in: str, check_out: str, count: int = 3) -> str:
    """搜索酒店"""
    city_data = _get_city_data(city)
    hotels = city_data["hotels"][:count]

    # 补充完整字段
    for i, hotel in enumerate(hotels):
        hotel.setdefault("city", city)
        hotel.setdefault("check_in", check_in)
        hotel.setdefault("check_out", check_out)
        hotel.setdefault("review_count", random.randint(500, 5000))
        hotel.setdefault("images", [f"https://example.com/hotel{i+1}.jpg"])

    return json.dumps(hotels, ensure_ascii=False, indent=2)


def search_restaurants(city: str, count: int = 3) -> str:
    """搜索餐厅"""
    city_data = _get_city_data(city)
    restaurants = city_data["restaurants"][:count]

    # 补充完整字段
    for i, restaurant in enumerate(restaurants):
        restaurant.setdefault("city", city)
        restaurant.setdefault("business_hours", "10:00-22:00")
        restaurant.setdefault("review_count", random.randint(200, 8000))
        restaurant.setdefault("images", [f"https://example.com/restaurant{i+1}.jpg"])

    return json.dumps(restaurants, ensure_ascii=False, indent=2)


# Function Calling工具定义
FLIGGY_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_flights",
            "description": "搜索航班信息，获取航班号、航空公司、价格、时长等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure": {"type": "string", "description": "出发城市，如'北京'"},
                    "destination": {"type": "string", "description": "目的地城市，如'上海'"},
                    "date": {"type": "string", "description": "出发日期，格式为YYYY-MM-DD"},
                },
                "required": ["departure", "destination", "date"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_trains",
            "description": "搜索火车信息，获取车次、价格、时长等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure": {"type": "string", "description": "出发城市，如'北京'"},
                    "destination": {"type": "string", "description": "目的地城市，如'上海'"},
                    "date": {"type": "string", "description": "出发日期，格式为YYYY-MM-DD"},
                },
                "required": ["departure", "destination", "date"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_hotels",
            "description": "搜索酒店信息，获取酒店名称、价格、评分、设施等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如'大理'"},
                    "check_in": {"type": "string", "description": "入住日期，格式为YYYY-MM-DD"},
                    "check_out": {"type": "string", "description": "离店日期，格式为YYYY-MM-DD"},
                    "count": {"type": "integer", "description": "返回酒店数量，默认为3", "default": 3},
                },
                "required": ["city", "check_in", "check_out"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_restaurants",
            "description": "搜索餐厅信息，获取餐厅名称、菜系、价格、评分等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如'大理'"},
                    "count": {"type": "integer", "description": "返回餐厅数量，默认为3", "default": 3},
                },
                "required": ["city"],
            },
        },
    },
]

"""
飞猪API工具函数 - 支持真实API调用 + 本地知识库兜底
"""

import json
import random
import requests
from typing import List, Dict, Any
from datetime import datetime

from config import get_config

# 导入扩展城市数据
from .city_data import EXTENDED_CITY_DB
from .city_data_v2 import EXTENDED_CITY_DB as EXTENDED_CITY_DB_V2
from .city_data_v3 import EXTENDED_CITY_DB as EXTENDED_CITY_DB_V3
from .city_data_v4 import EXTENDED_CITY_DB as EXTENDED_CITY_DB_V4


class FliggyAPI:
    """飞猪API封装类 - 真实API调用"""

    def __init__(self):
        self.config = get_config().api
        self.base_url = "https://api.fliggy.com"  # 飞猪API地址
        self.api_key = self.config.FLIGGY_API_KEY

    def search_hotels(self, city: str, check_in: str, check_out: str, count: int = 3) -> List[Dict]:
        """
        调用飞猪API搜索酒店
        真实API结构示例（需要企业资质）：
        GET https://api.fliggy.com/hotel/search
        参数: city, check_in, check_out, count
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            params = {
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "count": count
            }
            # 真实API调用（当前会失败，因为需要企业资质）
            # response = requests.get(f"{self.base_url}/hotel/search", headers=headers, params=params, timeout=5)
            # if response.status_code == 200:
            #     return response.json().get("hotels", [])

            # 模拟API调用失败（因为没有真实API权限）
            raise Exception("需要企业资质申请飞猪API调用权限")

        except Exception as e:
            print(f"[WARN] 飞猪酒店API调用失败: {e}，使用本地数据")
            return None

    def search_restaurants(self, city: str, count: int = 6) -> List[Dict]:
        """
        调用飞猪/口碑API搜索餐厅
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            params = {"city": city, "count": count}

            # 模拟API调用失败
            raise Exception("需要企业资质申请飞猪/口碑API调用权限")

        except Exception as e:
            print(f"[WARN] 飞猪餐厅API调用失败: {e}，使用本地数据")
            return None

    def search_attractions(self, city: str, count: int = 12) -> List[Dict]:
        """
        调用飞猪API搜索景点
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            params = {"city": city, "count": count}

            # 模拟API调用失败
            raise Exception("需要企业资质申请飞猪API调用权限")

        except Exception as e:
            print(f"[WARN] 飞猪景点API调用失败: {e}，使用本地数据")
            return None


# 全局实例
fliggy_api = FliggyAPI()


# 目的地知识库（核心城市）
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
            {"name": "喜洲古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "白族民居建筑群，喜洲粑粑必吃"},
            {"name": "南诏风情岛", "type": "海岛风光", "price": 50, "rating": 4.5, "description": "洱海三岛之一，南诏文化展示"},
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
            {"name": "泸沽湖", "type": "自然风光", "price": 100, "rating": 4.8, "description": "东方女儿国，摩梭文化"},
            {"name": "白沙古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "纳西族古都，白沙壁画"},
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
            {"name": "槟榔谷", "type": "民俗文化", "price": 96, "rating": 4.5, "description": "海南原住民文化，黎苗风情"},
            {"name": "鹿回头", "type": "城市地标", "price": 42, "rating": 4.5, "description": "三亚制高点，俯瞰三亚湾夜景"},
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
            {"name": "南锣鼓巷", "type": "历史街区", "price": 0, "rating": 4.5, "description": "北京最古老的街区之一，文创小店"},
            {"name": "798艺术区", "type": "艺术园区", "price": 0, "rating": 4.5, "description": "当代艺术集聚地，工业遗址改造"},
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
            {"name": "青城山", "type": "自然风光", "price": 80, "rating": 4.7, "description": "道教圣地，青城天下幽"},
            {"name": "杜甫草堂", "type": "历史文化", "price": 50, "rating": 4.6, "description": "诗圣杜甫流寓成都时的故居"},
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
            {"name": "陕西历史博物馆", "type": "博物馆", "price": 0, "rating": 4.8, "description": "中国第一座大型现代化国家级博物馆"},
            {"name": "大唐不夜城", "type": "现代都市", "price": 0, "rating": 4.6, "description": "盛唐文化主题步行街，网红打卡地"},
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
            {"name": "河坊街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "南宋御街，小吃一条街"},
            {"name": "九溪烟树", "type": "自然风光", "price": 0, "rating": 4.6, "description": "西湖边秘境，徒步圣地"},
        ],
    },
    "上海": {
        "province": "上海",
        "hotels": [
            {"name": "上海外滩华尔道夫酒店", "type": "豪华型", "price_per_night": 2800, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "米其林餐厅"], "address": "黄浦区中山东一路2号"},
            {"name": "上海静安香格里拉大酒店", "type": "高档型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "健身房", "餐厅"], "address": "静安区延安中路1218号"},
            {"name": "上海人民广场地铁站青旅", "type": "经济型", "price_per_night": 128, "rating": 4.3, "facilities": ["WiFi", "公共厨房"], "address": "黄浦区南京西路"},
        ],
        "restaurants": [
            {"name": "鼎泰丰（上海恒隆广场店）", "cuisine": "台湾菜", "avg_price": 128, "rating": 4.8, "specialties": ["小笼包", "蟹粉小笼", "红油抄手"], "address": "静安区南京西路1266号"},
            {"name": "新天地朗廷酒店凯旋餐厅", "cuisine": "法餐", "avg_price": 258, "rating": 4.7, "specialties": ["鹅肝", "牛排", "甜品"], "address": "黄浦区太仓路188号"},
            {"name": "小杨生煎（多家分店）", "cuisine": "上海小吃", "avg_price": 25, "rating": 4.5, "specialties": ["生煎包", "牛肉粉丝汤", "蟹壳黄"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "外滩", "type": "城市地标", "price": 0, "rating": 4.9, "description": "上海标志性景点，万国建筑博览群，夜景绝美"},
            {"name": "东方明珠", "type": "城市地标", "price": 120, "rating": 4.7, "description": "上海电视塔，可俯瞰全城，透明观光廊刺激"},
            {"name": "豫园", "type": "历史文化", "price": 40, "rating": 4.6, "description": "明代古典园林，城隍庙商圈，传统小吃聚集"},
            {"name": "上海迪士尼乐园", "type": "主题公园", "price": 475, "rating": 4.8, "description": "中国大陆首座迪士尼，创极速光轮必玩"},
            {"name": "田子坊", "type": "文创街区", "price": 0, "rating": 4.5, "description": "弄堂里的艺术街区，手工艺品、咖啡馆聚集"},
            {"name": "新天地", "type": "时尚街区", "price": 0, "rating": 4.6, "description": "石库门建筑改造，酒吧餐厅林立，时尚地标"},
            {"name": "南京路步行街", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "中华商业第一街，百年老店云集"},
        ],
    },
    "广州": {
        "province": "广东",
        "hotels": [
            {"name": "广州白天鹅宾馆", "type": "豪华型", "price_per_night": 1500, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "江景"], "address": "荔湾区沙面南街1号"},
            {"name": "广州北京路青旅", "type": "经济型", "price_per_night": 89, "rating": 4.3, "facilities": ["WiFi", "公共厨房"], "address": "越秀区北京路"},
        ],
        "restaurants": [
            {"name": "广州酒家", "cuisine": "粤菜", "avg_price": 128, "rating": 4.7, "specialties": ["烧鹅", "白切鸡", "虾饺"], "address": "荔湾区文昌南路"},
            {"name": "点都德", "cuisine": "早茶", "avg_price": 68, "rating": 4.6, "specialties": ["虾饺", "烧卖", "肠粉"], "address": "多家分店"},
            {"name": "银记肠粉", "cuisine": "广州小吃", "avg_price": 25, "rating": 4.5, "specialties": ["肠粉", "艇仔粥", "云吞面"], "address": "上九路"},
        ],
        "attractions": [
            {"name": "广州塔", "type": "城市地标", "price": 150, "rating": 4.8, "description": "小蛮腰，广州新地标，高空观景"},
            {"name": "沙面", "type": "历史街区", "price": 0, "rating": 4.6, "description": "欧陆风情建筑群，拍照圣地"},
            {"name": "陈家祠", "type": "历史文化", "price": 10, "rating": 4.7, "description": "岭南建筑艺术明珠"},
            {"name": "白云山", "type": "自然风光", "price": 5, "rating": 4.5, "description": "羊城第一秀，登高望远"},
            {"name": "珠江夜游", "type": "城市景观", "price": 80, "rating": 4.6, "description": "珠江两岸灯光秀"},
            {"name": "长隆旅游度假区", "type": "主题公园", "price": 350, "rating": 4.7, "description": "长隆野生动物园、欢乐世界"},
            {"name": "北京路步行街", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "广州最繁华的商业街"},
        ],
    },
    "重庆": {
        "province": "重庆",
        "hotels": [
            {"name": "重庆丽晶酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "江景"], "address": "渝中区江北嘴"},
            {"name": "重庆解放碑青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi", "公共厨房"], "address": "渝中区解放碑"},
        ],
        "restaurants": [
            {"name": "珮姐老火锅", "cuisine": "火锅", "avg_price": 108, "rating": 4.7, "specialties": ["九宫格", "毛肚", "鸭血"], "address": "解放碑较场口"},
            {"name": "花市豌杂面", "cuisine": "重庆小吃", "avg_price": 18, "rating": 4.6, "specialties": ["豌杂面", "小面", "抄手"], "address": "解放碑民生路"},
            {"name": "胡记蹄花汤", "cuisine": "重庆菜", "avg_price": 55, "rating": 4.5, "specialties": ["蹄花汤", "辣子鸡", "泉水鸡"], "address": "解放碑附近"},
        ],
        "attractions": [
            {"name": "洪崖洞", "type": "城市地标", "price": 0, "rating": 4.8, "description": "千与千寻现实版，山城夜景必看"},
            {"name": "磁器口古镇", "type": "古镇风情", "price": 0, "rating": 4.6, "description": "千年古镇，小吃一条街"},
            {"name": "长江索道", "type": "城市景观", "price": 20, "rating": 4.6, "description": "万里长江第一条空中走廊"},
            {"name": "武隆天生三桥", "type": "自然奇观", "price": 125, "rating": 4.7, "description": "世界自然遗产，变形金刚4取景地"},
            {"name": "解放碑", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "重庆地标，西部第一街"},
            {"name": "李子坝轻轨站", "type": "城市景观", "price": 0, "rating": 4.5, "description": "轻轨穿楼，网红打卡地"},
            {"name": "南山一棵树", "type": "城市景观", "price": 30, "rating": 4.5, "description": "俯瞰重庆夜景的最佳位置"},
        ],
    },
    "南京": {
        "province": "江苏",
        "hotels": [
            {"name": "南京香格里拉大酒店", "type": "豪华型", "price_per_night": 1500, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "餐厅"], "address": "鼓楼区中央路329号"},
            {"name": "南京夫子庙青旅", "type": "经济型", "price_per_night": 89, "rating": 4.4, "facilities": ["WiFi", "公共厨房"], "address": "秦淮区贡院街"},
        ],
        "restaurants": [
            {"name": "南京大牌档（德基广场店）", "cuisine": "南京菜", "avg_price": 88, "rating": 4.7, "specialties": ["盐水鸭", "鸭血粉丝汤", "狮子头"], "address": "玄武区中山路18号"},
            {"name": "回味鸭血粉丝汤", "cuisine": "南京小吃", "avg_price": 25, "rating": 4.6, "specialties": ["鸭血粉丝汤", "锅贴", "汤包"], "address": "多家分店"},
            {"name": "绿柳居", "cuisine": "素食", "avg_price": 65, "rating": 4.5, "specialties": ["素什锦", "素鹅", "素鸡"], "address": "秦淮区太平南路248号"},
        ],
        "attractions": [
            {"name": "中山陵", "type": "历史文化", "price": 0, "rating": 4.9, "description": "孙中山先生陵墓，气势恢宏，免费参观"},
            {"name": "夫子庙-秦淮河", "type": "历史文化", "price": 0, "rating": 4.7, "description": "桨声灯影里的秦淮河，夫子庙商圈"},
            {"name": "明孝陵", "type": "世界文化遗产", "price": 70, "rating": 4.8, "description": "明太祖朱元璋陵墓，神道石刻绝美"},
            {"name": "总统府", "type": "历史文化", "price": 35, "rating": 4.6, "description": "中国近代史博物馆，中西合璧建筑"},
            {"name": "南京博物院", "type": "博物馆", "price": 0, "rating": 4.8, "description": "中国三大博物馆之一，民国馆必看"},
            {"name": "玄武湖", "type": "自然风光", "price": 0, "rating": 4.6, "description": "江南最大的城内公园，环湖骑行"},
            {"name": "老门东", "type": "历史街区", "price": 0, "rating": 4.5, "description": "南京传统民居建筑群，文创小店聚集"},
        ],
    },
    "武汉": {
        "province": "湖北",
        "hotels": [
            {"name": "武汉光谷希尔顿酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "东湖高新区光谷大道"},
            {"name": "武汉户部巷青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "武昌区户部巷"},
        ],
        "restaurants": [
            {"name": "蔡林记", "cuisine": "武汉小吃", "avg_price": 15, "rating": 4.7, "specialties": ["热干面", "三鲜豆皮", "糊汤粉"], "address": "多家分店"},
            {"name": "靓靓蒸虾", "cuisine": "小龙虾", "avg_price": 128, "rating": 4.6, "specialties": ["油焖大虾", "蒜蓉虾", "清蒸虾"], "address": "万松园"},
            {"name": "老通城", "cuisine": "武汉小吃", "avg_price": 25, "rating": 4.5, "specialties": ["三鲜豆皮", "谈炎记水饺"], "address": "吉庆街"},
        ],
        "attractions": [
            {"name": "黄鹤楼", "type": "历史文化", "price": 70, "rating": 4.8, "description": "江南三大名楼之一，天下江山第一楼"},
            {"name": "东湖", "type": "自然风光", "price": 0, "rating": 4.7, "description": "中国最大城中湖，樱花圣地"},
            {"name": "武汉大学", "type": "高校参观", "price": 0, "rating": 4.6, "description": "中国最美大学，樱花季必去"},
            {"name": "户部巷", "type": "美食街区", "price": 0, "rating": 4.5, "description": "武汉早点一条街"},
            {"name": "长江大桥", "type": "城市地标", "price": 0, "rating": 4.6, "description": "万里长江第一桥"},
            {"name": "昙华林", "type": "文创街区", "price": 0, "rating": 4.5, "description": "文艺青年聚集地"},
            {"name": "汉口江滩", "type": "城市景观", "price": 0, "rating": 4.5, "description": "百里长江江滩，夜景绝美"},
        ],
    },
    "苏州": {
        "province": "江苏",
        "hotels": [
            {"name": "苏州柏悦酒店", "type": "豪华型", "price_per_night": 2200, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "湖景"], "address": "工业园区金鸡湖畔"},
            {"name": "苏州平江路青旅", "type": "经济型", "price_per_night": 98, "rating": 4.4, "facilities": ["WiFi", "公共厨房"], "address": "姑苏区平江路"},
        ],
        "restaurants": [
            {"name": "松鹤楼（观前街店）", "cuisine": "苏帮菜", "avg_price": 128, "rating": 4.7, "specialties": ["松鼠鳜鱼", "响油鳝糊", "清炒虾仁"], "address": "姑苏区观前街141号"},
            {"name": "哑巴生煎（临顿路店）", "cuisine": "苏州小吃", "avg_price": 20, "rating": 4.6, "specialties": ["生煎包", "馄饨", "汤圆"], "address": "姑苏区临顿路"},
            {"name": "得月楼", "cuisine": "苏帮菜", "avg_price": 108, "rating": 4.6, "specialties": ["樱桃肉", "叫化鸡", "太湖三白"], "address": "姑苏区太监弄72号"},
        ],
        "attractions": [
            {"name": "拙政园", "type": "世界文化遗产", "price": 70, "rating": 4.9, "description": "中国四大名园之首，江南园林代表"},
            {"name": "苏州博物馆", "type": "博物馆", "price": 0, "rating": 4.8, "description": "贝聿铭设计，建筑本身就是艺术品"},
            {"name": "平江路", "type": "历史街区", "price": 0, "rating": 4.7, "description": "最能代表苏州的古街，小桥流水人家"},
            {"name": "虎丘", "type": "历史文化", "price": 60, "rating": 4.6, "description": "吴中第一名胜，剑池传说"},
            {"name": "金鸡湖", "type": "自然风光", "price": 0, "rating": 4.5, "description": "园区地标，夜景灯光秀"},
            {"name": "周庄", "type": "古镇风情", "price": 100, "rating": 4.7, "description": "中国第一水乡，双桥、沈万三故居"},
            {"name": "同里古镇", "type": "古镇风情", "price": 80, "rating": 4.6, "description": "世界文化遗产，退思园必看"},
        ],
    },
    "昆明": {
        "province": "云南",
        "hotels": [
            {"name": "昆明洲际酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "西山区滇池路"},
            {"name": "昆明翠湖青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "五华区翠湖附近"},
        ],
        "restaurants": [
            {"name": "福照楼", "cuisine": "滇菜", "avg_price": 88, "rating": 4.6, "specialties": ["汽锅鸡", "过桥米线", "野生菌"], "address": "五华区"},
            {"name": "桥香园", "cuisine": "云南小吃", "avg_price": 25, "rating": 4.5, "specialties": ["过桥米线", "小锅米线", "凉米线"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "石林", "type": "世界自然遗产", "price": 130, "rating": 4.8, "description": "世界自然遗产，喀斯特地貌奇观"},
            {"name": "滇池", "type": "自然风光", "price": 0, "rating": 4.6, "description": "云南最大淡水湖，海埂公园"},
            {"name": "翠湖", "type": "城市公园", "price": 0, "rating": 4.5, "description": "昆明城市中心，冬季红嘴鸥"},
            {"name": "西山", "type": "自然风光", "price": 30, "rating": 4.6, "description": "睡美人山，龙门石窟"},
            {"name": "云南民族村", "type": "民俗文化", "price": 90, "rating": 4.5, "description": "25个少数民族村寨"},
            {"name": "金殿", "type": "历史文化", "price": 30, "rating": 4.4, "description": "中国最大铜殿"},
            {"name": "官渡古镇", "type": "古镇风情", "price": 0, "rating": 4.4, "description": "千年古镇，官渡粑粑"},
        ],
    },
    "青岛": {
        "province": "山东",
        "hotels": [
            {"name": "青岛海景花园大酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "海景", "SPA"], "address": "市南区彰化路"},
            {"name": "青岛栈桥青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "市南区栈桥附近"},
        ],
        "restaurants": [
            {"name": "船歌鱼水饺", "cuisine": "海鲜", "avg_price": 88, "rating": 4.7, "specialties": ["墨鱼水饺", "黄花鱼水饺", "海鲜拼盘"], "address": "多家分店"},
            {"name": "劈柴院", "cuisine": "青岛小吃", "avg_price": 35, "rating": 4.5, "specialties": ["锅贴", "烤鱿鱼", "海胆"], "address": "市南区中山路"},
            {"name": "青岛啤酒街", "cuisine": "烧烤", "avg_price": 68, "rating": 4.5, "specialties": ["烤肉", "海鲜", "青岛啤酒"], "address": "市北区登州路"},
        ],
        "attractions": [
            {"name": "栈桥", "type": "城市地标", "price": 0, "rating": 4.7, "description": "青岛标志性建筑，百年历史"},
            {"name": "八大关", "type": "历史街区", "price": 0, "rating": 4.7, "description": "万国建筑博览会，花石楼"},
            {"name": "崂山", "type": "自然风光", "price": 90, "rating": 4.7, "description": "海上第一名山，道教圣地"},
            {"name": "金沙滩", "type": "海滩风光", "price": 0, "rating": 4.6, "description": "亚洲第一滩"},
            {"name": "五四广场", "type": "城市地标", "price": 0, "rating": 4.5, "description": "五月的风雕塑，奥帆中心"},
            {"name": "青岛啤酒博物馆", "type": "工业旅游", "price": 60, "rating": 4.5, "description": "百年啤酒文化"},
            {"name": "信号山", "type": "城市景观", "price": 15, "rating": 4.5, "description": "俯瞰红瓦绿树碧海蓝天"},
        ],
    },
    "厦门": {
        "province": "福建",
        "hotels": [
            {"name": "厦门康莱德酒店", "type": "豪华型", "price_per_night": 1500, "rating": 4.8, "facilities": ["WiFi", "泳池", "海景", "SPA"], "address": "思明区环岛路"},
            {"name": "厦门曾厝垵青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "思明区曾厝垵"},
        ],
        "restaurants": [
            {"name": "沙茶面", "cuisine": "厦门小吃", "avg_price": 20, "rating": 4.7, "specialties": ["沙茶面", "海蛎煎", "土笋冻"], "address": "多家分店"},
            {"name": "中山路步行街", "cuisine": "小吃", "avg_price": 35, "rating": 4.5, "specialties": ["烧肉粽", "花生汤", "姜母鸭"], "address": "思明区中山路"},
        ],
        "attractions": [
            {"name": "鼓浪屿", "type": "世界文化遗产", "price": 100, "rating": 4.8, "description": "钢琴之岛，万国建筑博物馆"},
            {"name": "南普陀寺", "type": "佛教圣地", "price": 0, "rating": 4.7, "description": "闽南佛教圣地，免费素斋"},
            {"name": "厦门大学", "type": "高校参观", "price": 0, "rating": 4.7, "description": "中国最美大学，芙蓉隧道"},
            {"name": "曾厝垵", "type": "文创街区", "price": 0, "rating": 4.5, "description": "闽南渔村改造的文创村"},
            {"name": "环岛路", "type": "城市景观", "price": 0, "rating": 4.6, "description": "最美马拉松赛道"},
            {"name": "集美学村", "type": "历史文化", "price": 0, "rating": 4.5, "description": "嘉庚建筑群，龙舟池"},
            {"name": "中山路步行街", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "厦门最繁华的商业街"},
        ],
    },
    "长沙": {
        "province": "湖南",
        "hotels": [
            {"name": "长沙万达文华酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "开福区万达广场"},
            {"name": "长沙五一广场青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "芙蓉区五一广场"},
        ],
        "restaurants": [
            {"name": "茶颜悦色", "cuisine": "奶茶", "avg_price": 15, "rating": 4.8, "specialties": ["幽兰拿铁", "声声乌龙", "桂花弄"], "address": "多家分店"},
            {"name": "文和友", "cuisine": "长沙小吃", "avg_price": 68, "rating": 4.6, "specialties": ["口味虾", "臭豆腐", "糖油粑粑"], "address": "海信广场"},
            {"name": "火宫殿", "cuisine": "湘菜", "avg_price": 65, "rating": 4.5, "specialties": ["臭豆腐", "龙脂猪血", "红烧猪脚"], "address": "坡子街"},
        ],
        "attractions": [
            {"name": "橘子洲头", "type": "历史文化", "price": 0, "rating": 4.8, "description": "毛主席青年艺术雕塑，湘江风光"},
            {"name": "岳麓山", "type": "自然风光", "price": 0, "rating": 4.7, "description": "千年学府岳麓书院，爱晚亭"},
            {"name": "太平街", "type": "历史街区", "price": 0, "rating": 4.6, "description": "长沙古城最完整的街区"},
            {"name": "湖南省博物馆", "type": "博物馆", "price": 0, "rating": 4.8, "description": "马王堆汉墓文物，辛追夫人"},
            {"name": "IFS国金中心", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "长沙最高楼，KAWS雕塑"},
            {"name": "梅溪湖", "type": "城市景观", "price": 0, "rating": 4.5, "description": "城市新中心，大剧院"},
            {"name": "铜官窑古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "陶瓷文化小镇"},
        ],
    },
    "深圳": {
        "province": "广东",
        "hotels": [
            {"name": "深圳瑞吉酒店", "type": "豪华型", "price_per_night": 1800, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "海景"], "address": "南山区后海滨路"},
            {"name": "深圳东门老街青旅", "type": "经济型", "price_per_night": 89, "rating": 4.3, "facilities": ["WiFi"], "address": "罗湖区东门"},
        ],
        "restaurants": [
            {"name": "润园四季椰子鸡", "cuisine": "广东菜", "avg_price": 128, "rating": 4.7, "specialties": ["椰子鸡", "煲仔饭", "叉烧"], "address": "多家分店"},
            {"name": "木屋烧烤", "cuisine": "烧烤", "avg_price": 88, "rating": 4.5, "specialties": ["烤肉", "烤海鲜", "啤酒"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "世界之窗", "type": "主题公园", "price": 200, "rating": 4.6, "description": "微缩世界景观，一天游遍全球"},
            {"name": "欢乐谷", "type": "主题公园", "price": 230, "rating": 4.6, "description": "华侨城主题乐园"},
            {"name": "大梅沙海滨公园", "type": "海滩风光", "price": 0, "rating": 4.5, "description": "深圳最美海滩"},
            {"name": "仙湖植物园", "type": "自然生态", "price": 15, "rating": 4.5, "description": "深圳最大植物园"},
            {"name": "东门老街", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "深圳最古老的商业街"},
            {"name": "莲花山公园", "type": "城市公园", "price": 0, "rating": 4.5, "description": "邓小平铜像，俯瞰市民中心"},
            {"name": "深圳湾公园", "type": "城市景观", "price": 0, "rating": 4.5, "description": "深圳湾滨海栈道，看海鸥"},
        ],
    },
    "天津": {
        "province": "天津",
        "hotels": [
            {"name": "天津丽思卡尔顿酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA"], "address": "河北区大沽路"},
            {"name": "天津五大道青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "和平区五大道"},
        ],
        "restaurants": [
            {"name": "狗不理包子", "cuisine": "天津小吃", "avg_price": 68, "rating": 4.5, "specialties": ["包子", "锅巴菜", "煎饼果子"], "address": "山东路77号"},
            {"name": "十八街麻花", "cuisine": "天津特产", "avg_price": 35, "rating": 4.5, "specialties": ["麻花", "糕点"], "address": "多家分店"},
            {"name": "耳朵眼炸糕", "cuisine": "天津小吃", "avg_price": 10, "rating": 4.5, "specialties": ["炸糕", "豆沙馅"], "address": "北马路"},
        ],
        "attractions": [
            {"name": "天津之眼", "type": "城市地标", "price": 70, "rating": 4.7, "description": "世界唯一建在桥上的摩天轮"},
            {"name": "五大道", "type": "历史街区", "price": 0, "rating": 4.7, "description": "万国建筑博览会，小洋楼"},
            {"name": "意大利风情区", "type": "历史街区", "price": 0, "rating": 4.6, "description": "意大利建筑群，梁启超故居"},
            {"name": "古文化街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "津门故里，泥人张"},
            {"name": "瓷房子", "type": "艺术建筑", "price": 50, "rating": 4.5, "description": "瓷器装饰的法式建筑"},
            {"name": "天津海昌极地海洋世界", "type": "主题公园", "price": 160, "rating": 4.5, "description": "极地海洋动物"},
            {"name": "盘山风景区", "type": "自然风光", "price": 75, "rating": 4.5, "description": "京东第一山"},
        ],
    },
    "桂林": {
        "province": "广西",
        "hotels": [
            {"name": "桂林香格里拉大酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "江景"], "address": "秀峰区滨江路"},
            {"name": "桂林阳朔西街青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "阳朔县西街"},
        ],
        "restaurants": [
            {"name": "阳朔啤酒鱼", "cuisine": "桂林菜", "avg_price": 88, "rating": 4.7, "specialties": ["啤酒鱼", "田螺酿", "荔浦芋扣肉"], "address": "阳朔西街"},
            {"name": "桂林米粉", "cuisine": "桂林小吃", "avg_price": 12, "rating": 4.6, "specialties": ["卤菜粉", "汤粉", "马肉米粉"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "漓江", "type": "自然风光", "price": 210, "rating": 4.9, "description": "桂林山水甲天下，竹筏漂流"},
            {"name": "阳朔西街", "type": "历史街区", "price": 0, "rating": 4.6, "description": "洋人街，中西文化交融"},
            {"name": "象鼻山", "type": "城市地标", "price": 55, "rating": 4.6, "description": "桂林城徽，水月洞"},
            {"name": "龙脊梯田", "type": "自然风光", "price": 80, "rating": 4.7, "description": "壮美梯田，少数民族村寨"},
            {"name": "两江四湖", "type": "城市景观", "price": 190, "rating": 4.5, "description": "桂林夜景，日月双塔"},
            {"name": "独秀峰", "type": "历史文化", "price": 50, "rating": 4.5, "description": "靖江王府，桂林山水之源"},
            {"name": "遇龙河", "type": "自然风光", "price": 150, "rating": 4.6, "description": "小漓江，竹筏漂流"},
        ],
    },
    "贵阳": {
        "province": "贵州",
        "hotels": [
            {"name": "贵阳世纪金源大饭店", "type": "豪华型", "price_per_night": 780, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "观山湖区"},
            {"name": "贵阳甲秀楼青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "南明区甲秀楼附近"},
        ],
        "restaurants": [
            {"name": "老凯俚酸汤鱼", "cuisine": "贵州菜", "avg_price": 78, "rating": 4.7, "specialties": ["酸汤鱼", "丝娃娃", "豆腐圆子"], "address": "多家分店"},
            {"name": "肠旺面", "cuisine": "贵阳小吃", "avg_price": 15, "rating": 4.6, "specialties": ["肠旺面", "花溪牛肉粉"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "黄果树瀑布", "type": "自然奇观", "price": 160, "rating": 4.8, "description": "中国第一大瀑布，水帘洞"},
            {"name": "甲秀楼", "type": "历史文化", "price": 0, "rating": 4.6, "description": "贵阳地标，南明河畔"},
            {"name": "青岩古镇", "type": "古镇风情", "price": 10, "rating": 4.5, "description": "600年历史古镇，状元府"},
            {"name": "黔灵山公园", "type": "城市公园", "price": 5, "rating": 4.5, "description": "贵阳后花园，野生猕猴"},
            {"name": "天河潭", "type": "自然奇观", "price": 75, "rating": 4.5, "description": "贵州浓缩盆景，溶洞"},
            {"name": "花溪公园", "type": "城市公园", "price": 0, "rating": 4.4, "description": "高原明珠"},
            {"name": "文昌阁", "type": "历史文化", "price": 0, "rating": 4.4, "description": "贵阳古城楼"},
        ],
    },
    "哈尔滨": {
        "province": "黑龙江",
        "hotels": [
            {"name": "哈尔滨松北香格里拉大酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA"], "address": "松北区世茂大道"},
            {"name": "哈尔滨中央大街青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "道里区中央大街"},
        ],
        "restaurants": [
            {"name": "东方饺子王", "cuisine": "东北菜", "avg_price": 55, "rating": 4.6, "specialties": ["饺子", "锅包肉", "酱骨架"], "address": "中央大街"},
            {"name": "马迭尔冰棍", "cuisine": "甜品", "avg_price": 5, "rating": 4.7, "specialties": ["冰棍", "面包"], "address": "中央大街"},
            {"name": "红肠", "cuisine": "哈尔滨特产", "avg_price": 30, "rating": 4.5, "specialties": ["秋林红肠", "大列巴"], "address": "秋林公司"},
        ],
        "attractions": [
            {"name": "冰雪大世界", "type": "主题公园", "price": 288, "rating": 4.8, "description": "世界最大冰雪主题乐园"},
            {"name": "中央大街", "type": "历史街区", "price": 0, "rating": 4.7, "description": "亚洲最长步行街，百年建筑"},
            {"name": "索菲亚教堂", "type": "历史文化", "price": 15, "rating": 4.6, "description": "远东最大的东正教堂"},
            {"name": "太阳岛", "type": "自然风光", "price": 30, "rating": 4.5, "description": "雪博会，冰灯"},
            {"name": "松花江", "type": "自然风光", "price": 0, "rating": 4.5, "description": "冬季冰上活动"},
            {"name": "东北虎林园", "type": "自然生态", "price": 100, "rating": 4.5, "description": "世界最大东北虎繁育基地"},
            {"name": "老道外", "type": "历史街区", "price": 0, "rating": 4.4, "description": "中华巴洛克建筑群"},
        ],
    },
    "香港": {
        "province": "香港",
        "hotels": [
            {"name": "香港半岛酒店", "type": "豪华型", "price_per_night": 4500, "rating": 4.9, "facilities": ["WiFi", "泳池", "SPA", "维港景"], "address": "尖沙咀梳士巴利道22号"},
            {"name": "香港九龙青旅", "type": "经济型", "price_per_night": 200, "rating": 4.3, "facilities": ["WiFi"], "address": "油尖旺区"},
        ],
        "restaurants": [
            {"name": "添好运", "cuisine": "港式点心", "avg_price": 68, "rating": 4.7, "specialties": ["酥皮叉烧包", "虾饺", "肠粉"], "address": "中环威灵顿街"},
            {"name": "一兰拉面", "cuisine": "日式", "avg_price": 88, "rating": 4.6, "specialties": ["豚骨拉面", "溏心蛋"], "address": "铜锣湾"},
            {"name": "兰芳园", "cuisine": "港式", "avg_price": 55, "rating": 4.5, "specialties": ["丝袜奶茶", "猪扒包"], "address": "中环结志街"},
        ],
        "attractions": [
            {"name": "维多利亚港", "type": "城市地标", "price": 0, "rating": 4.9, "description": "世界三大夜景，幻彩咏香江"},
            {"name": "太平山顶", "type": "城市景观", "price": 88, "rating": 4.8, "description": "俯瞰港岛全景"},
            {"name": "迪士尼乐园", "type": "主题公园", "price": 639, "rating": 4.7, "description": "全球最小迪士尼，童话世界"},
            {"name": "海洋公园", "type": "主题公园", "price": 498, "rating": 4.6, "description": "香港本土主题乐园"},
            {"name": "旺角", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "女人街，波鞋街"},
            {"name": "中环", "type": "现代都市", "price": 0, "rating": 4.5, "description": "金融中心，石板街"},
            {"name": "黄大仙祠", "type": "佛教圣地", "price": 0, "rating": 4.5, "description": "香港最著名的庙宇"},
        ],
    },
    "澳门": {
        "province": "澳门",
        "hotels": [
            {"name": "澳门威尼斯人度假村", "type": "豪华型", "price_per_night": 2500, "rating": 4.9, "facilities": ["WiFi", "泳池", "赌场", "购物中心"], "address": "路氹金光大道"},
            {"name": "澳门青旅", "type": "经济型", "price_per_night": 150, "rating": 4.3, "facilities": ["WiFi"], "address": "大三巴附近"},
        ],
        "restaurants": [
            {"name": "安德鲁蛋挞", "cuisine": "葡式", "avg_price": 12, "rating": 4.8, "specialties": ["葡式蛋挞"], "address": "路环"},
            {"name": "大利来猪扒包", "cuisine": "澳门小吃", "avg_price": 35, "rating": 4.6, "specialties": ["猪扒包", "木糠布丁"], "address": "氹仔"},
            {"name": "黄枝记", "cuisine": "澳门小吃", "avg_price": 30, "rating": 4.5, "specialties": ["云吞面", "竹升面"], "address": "议事亭前地"},
        ],
        "attractions": [
            {"name": "大三巴牌坊", "type": "世界文化遗产", "price": 0, "rating": 4.8, "description": "澳门标志性建筑"},
            {"name": "威尼斯人度假村", "type": "度假区", "price": 0, "rating": 4.7, "description": "室内运河购物中心"},
            {"name": "妈阁庙", "type": "世界文化遗产", "price": 0, "rating": 4.5, "description": "澳门最古老的庙宇"},
            {"name": "新葡京酒店", "type": "度假区", "price": 0, "rating": 4.5, "description": "澳门地标建筑"},
            {"name": "官也街", "type": "美食街区", "price": 0, "rating": 4.5, "description": "澳门美食一条街"},
            {"name": "路环村", "type": "历史街区", "price": 0, "rating": 4.4, "description": "澳门最美的渔村"},
            {"name": "8字摩天轮", "type": "娱乐设施", "price": 100, "rating": 4.5, "description": "新濠天地8字摩天轮"},
        ],
    },
    "无锡": {
        "province": "江苏",
        "hotels": [
            {"name": "无锡太湖华邑酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "太湖景"], "address": "滨湖区太湖大道"},
            {"name": "无锡崇安寺青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "梁溪区崇安寺"},
        ],
        "restaurants": [
            {"name": "王兴记", "cuisine": "无锡小吃", "avg_price": 35, "rating": 4.6, "specialties": ["小笼包", "馄饨", "无锡排骨"], "address": "中山路"},
            {"name": "三凤桥", "cuisine": "无锡菜", "avg_price": 78, "rating": 4.5, "specialties": ["酱排骨", "响油鳝糊", "脆鳝"], "address": "中山路255号"},
        ],
        "attractions": [
            {"name": "鼋头渚", "type": "自然风光", "price": 90, "rating": 4.8, "description": "太湖佳绝处，樱花圣地"},
            {"name": "灵山大佛", "type": "佛教文化", "price": 210, "rating": 4.7, "description": "88米青铜大佛，九龙灌浴"},
            {"name": "拈花湾", "type": "度假区", "price": 120, "rating": 4.6, "description": "禅意小镇，光影秀"},
            {"name": "惠山古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "祠堂文化聚集地"},
            {"name": "南长街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "古运河畔，清名桥"},
            {"name": "蠡园", "type": "园林古迹", "price": 30, "rating": 4.4, "description": "范蠡西施传说"},
            {"name": "太湖湿地公园", "type": "自然生态", "price": 60, "rating": 4.4, "description": "太湖边生态湿地"},
        ],
    },
    "郑州": {
        "province": "河南",
        "hotels": [
            {"name": "郑州绿地JW万豪酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "金水区"},
            {"name": "郑州二七广场青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "二七区二七广场"},
        ],
        "restaurants": [
            {"name": "萧记三鲜烩面", "cuisine": "河南菜", "avg_price": 35, "rating": 4.6, "specialties": ["烩面", "胡辣汤", "烧饼"], "address": "多家分店"},
            {"name": "合记烩面", "cuisine": "河南小吃", "avg_price": 25, "rating": 4.5, "specialties": ["羊肉烩面", "牛肉烩面"], "address": "顺河路"},
        ],
        "attractions": [
            {"name": "少林寺", "type": "世界文化遗产", "price": 80, "rating": 4.8, "description": "天下武功出少林，武术表演"},
            {"name": "龙门石窟", "type": "世界文化遗产", "price": 90, "rating": 4.9, "description": "中国三大石窟之一（洛阳）"},
            {"name": "二七纪念塔", "type": "城市地标", "price": 0, "rating": 4.5, "description": "郑州地标"},
            {"name": "河南博物院", "type": "博物馆", "price": 0, "rating": 4.7, "description": "中国八大博物馆之一"},
            {"name": "黄河风景名胜区", "type": "自然风光", "price": 60, "rating": 4.5, "description": "黄河母亲像，炎黄二帝"},
            {"name": "郑州商城遗址", "type": "历史文化", "price": 0, "rating": 4.4, "description": "3600年前的商城"},
            {"name": "只有河南·戏剧幻城", "type": "主题公园", "price": 290, "rating": 4.6, "description": "沉浸式戏剧聚落"},
        ],
    },
    "济南": {
        "province": "山东",
        "hotels": [
            {"name": "济南香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "历下区泺源大街"},
            {"name": "济南泉城广场青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "历下区泉城广场"},
        ],
        "restaurants": [
            {"name": "燕喜堂", "cuisine": "鲁菜", "avg_price": 88, "rating": 4.6, "specialties": ["糖醋鲤鱼", "九转大肠", "爆炒腰花"], "address": "泉城路"},
            {"name": "油旋", "cuisine": "济南小吃", "avg_price": 10, "rating": 4.5, "specialties": ["油旋", "甜沫", "把子肉"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "趵突泉", "type": "自然奇观", "price": 40, "rating": 4.8, "description": "天下第一泉，泉城标志"},
            {"name": "大明湖", "type": "自然风光", "price": 0, "rating": 4.7, "description": "泉城明珠，夏雨荷传说"},
            {"name": "千佛山", "type": "自然风光", "price": 30, "rating": 4.5, "description": "济南三大名胜之一"},
            {"name": "泉城广场", "type": "城市地标", "price": 0, "rating": 4.5, "description": "济南城市客厅"},
            {"name": "宽厚里", "type": "历史街区", "price": 0, "rating": 4.5, "description": "济南版宽窄巷子"},
            {"name": "芙蓉街", "type": "美食街区", "price": 0, "rating": 4.5, "description": "济南美食一条街"},
            {"name": "灵岩寺", "type": "佛教圣地", "price": 60, "rating": 4.5, "description": "海内第一名塑"},
        ],
    },
    "拉萨": {
        "province": "西藏",
        "hotels": [
            {"name": "拉萨瑞吉度假酒店", "type": "豪华型", "price_per_night": 1800, "rating": 4.9, "facilities": ["WiFi", "供氧", "SPA", "藏式装修"], "address": "城关区江苏路"},
            {"name": "拉萨东措青旅", "type": "经济型", "price_per_night": 59, "rating": 4.4, "facilities": ["WiFi", "公共厨房"], "address": "城关区北京东路"},
        ],
        "restaurants": [
            {"name": "玛吉阿米", "cuisine": "藏餐", "avg_price": 88, "rating": 4.7, "specialties": ["酥油茶", "糌粑", "牦牛肉"], "address": "城关区八廓街"},
            {"name": "娜玛瑟德", "cuisine": "尼泊尔菜", "avg_price": 65, "rating": 4.6, "specialties": ["咖喱", "手抓饭", "奶茶"], "address": "城关区大昭寺附近"},
        ],
        "attractions": [
            {"name": "布达拉宫", "type": "世界文化遗产", "price": 200, "rating": 4.9, "description": "藏传佛教圣地，世界海拔最高的宫殿"},
            {"name": "大昭寺", "type": "世界文化遗产", "price": 85, "rating": 4.8, "description": "藏传佛教最神圣的寺庙"},
            {"name": "八廓街", "type": "历史街区", "price": 0, "rating": 4.7, "description": "转经道，藏族风情街"},
            {"name": "纳木错", "type": "自然风光", "price": 120, "rating": 4.9, "description": "世界最高的大湖，圣湖"},
            {"name": "色拉寺", "type": "佛教圣地", "price": 50, "rating": 4.6, "description": "辩经场，下午三点辩经"},
            {"name": "罗布林卡", "type": "园林古迹", "price": 60, "rating": 4.5, "description": "达赖喇嘛的夏宫"},
            {"name": "药王山", "type": "自然风光", "price": 0, "rating": 4.5, "description": "50元人民币背景拍摄地"},
        ],
    },
    "大连": {
        "province": "辽宁",
        "hotels": [
            {"name": "大连一方城堡酒店", "type": "豪华型", "price_per_night": 1500, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "海景"], "address": "中山区滨海西路"},
            {"name": "大连星海广场青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "沙河口区星海广场附近"},
        ],
        "restaurants": [
            {"name": "品海楼", "cuisine": "海鲜", "avg_price": 128, "rating": 4.7, "specialties": ["海胆", "鲍鱼", "海参"], "address": "中山区"},
            {"name": "铁板鱿鱼", "cuisine": "大连小吃", "avg_price": 15, "rating": 4.5, "specialties": ["铁板鱿鱼", "烤冷面", "焖子"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "星海广场", "type": "城市地标", "price": 0, "rating": 4.7, "description": "亚洲最大的城市广场"},
            {"name": "金石滩", "type": "国家度假区", "price": 100, "rating": 4.7, "description": "黄金海岸，地质奇观"},
            {"name": "老虎滩海洋公园", "type": "主题公园", "price": 210, "rating": 4.6, "description": "亚洲最大海洋公园"},
            {"name": "棒棰岛", "type": "海滩风光", "price": 20, "rating": 4.6, "description": "国宾浴场，海水最清澈"},
            {"name": "旅顺口", "type": "历史文化", "price": 0, "rating": 4.5, "description": "军港之城，日俄监狱"},
            {"name": "威尼斯水城", "type": "现代都市", "price": 0, "rating": 4.5, "description": "大连版威尼斯"},
            {"name": "滨海路", "type": "城市景观", "price": 0, "rating": 4.6, "description": "大连最美滨海公路"},
        ],
    },
    "沈阳": {
        "province": "辽宁",
        "hotels": [
            {"name": "沈阳君悦酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA"], "address": "和平区青年大街"},
            {"name": "沈阳中街青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "沈河区中街"},
        ],
        "restaurants": [
            {"name": "老边饺子", "cuisine": "东北菜", "avg_price": 65, "rating": 4.6, "specialties": ["煸馅饺子", "熏肉大饼", "酸菜白肉"], "address": "沈河区中街"},
            {"name": "李连贵熏肉大饼", "cuisine": "东北小吃", "avg_price": 30, "rating": 4.5, "specialties": ["熏肉大饼", "大酱骨"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "沈阳故宫", "type": "世界文化遗产", "price": 50, "rating": 4.8, "description": "中国仅存的两大皇宫建筑群之一"},
            {"name": "张氏帅府", "type": "历史文化", "price": 50, "rating": 4.7, "description": "张作霖、张学良父子故居"},
            {"name": "九一八历史博物馆", "type": "红色旅游", "price": 0, "rating": 4.7, "description": "勿忘国耻"},
            {"name": "棋盘山", "type": "自然风光", "price": 20, "rating": 4.5, "description": "沈阳最大风景区"},
            {"name": "北陵公园", "type": "城市公园", "price": 6, "rating": 4.5, "description": "清昭陵，皇太极陵墓"},
            {"name": "沈阳中街", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "中国第一条商业步行街"},
            {"name": "刘老根大舞台", "type": "演艺娱乐", "price": 180, "rating": 4.4, "description": "二人转表演"},
        ],
    },
    "泉州": {
        "province": "福建",
        "hotels": [
            {"name": "泉州迎宾馆", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "丰泽区东海大街"},
            {"name": "泉州西街青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "鲤城区西街"},
        ],
        "restaurants": [
            {"name": "侯阿婆肉粽", "cuisine": "泉州小吃", "avg_price": 15, "rating": 4.7, "specialties": ["肉粽", "烧肉粽", "四果汤"], "address": "鲤城区东街"},
            {"name": "好成财牛排", "cuisine": "闽南菜", "avg_price": 55, "rating": 4.6, "specialties": ["牛肉羹", "牛排", "咸饭"], "address": "鲤城区"},
        ],
        "attractions": [
            {"name": "开元寺", "type": "佛教圣地", "price": 0, "rating": 4.8, "description": "福建最大佛教寺院，东西塔"},
            {"name": "清净寺", "type": "世界文化遗产", "price": 3, "rating": 4.7, "description": "中国最古老的伊斯兰教寺院"},
            {"name": "洛阳桥", "type": "世界文化遗产", "price": 0, "rating": 4.7, "description": "中国四大古桥之一"},
            {"name": "崇武古城", "type": "历史文化", "price": 45, "rating": 4.6, "description": "中国现存最完整的花岗岩海防城堡"},
            {"name": "清源山", "type": "自然风光", "price": 55, "rating": 4.6, "description": "老君岩，道教圣地"},
            {"name": "西街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "泉州最古老的街道"},
            {"name": "闽台缘博物馆", "type": "博物馆", "price": 0, "rating": 4.5, "description": "闽台关系历史"},
        ],
    },
    "烟台": {
        "province": "山东",
        "hotels": [
            {"name": "烟台希尔顿酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "海景"], "address": "莱山区滨海路"},
            {"name": "烟台海滨青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "芝罘区海滨"},
        ],
        "restaurants": [
            {"name": "蓬莱小面", "cuisine": "烟台小吃", "avg_price": 15, "rating": 4.6, "specialties": ["蓬莱小面", "烟台焖子", "鲅鱼水饺"], "address": "多家分店"},
            {"name": "渔人码头", "cuisine": "海鲜", "avg_price": 128, "rating": 4.6, "specialties": ["海鲜", "烧烤", "啤酒"], "address": "莱山区"},
        ],
        "attractions": [
            {"name": "蓬莱阁", "type": "历史文化", "price": 100, "rating": 4.8, "description": "人间仙境，八仙过海传说"},
            {"name": "长岛", "type": "海岛风光", "price": 120, "rating": 4.7, "description": "海上仙山，最美海岛"},
            {"name": "烟台山", "type": "历史文化", "price": 50, "rating": 4.6, "description": "近代建筑群，领事馆旧址"},
            {"name": "养马岛", "type": "海岛风光", "price": 0, "rating": 4.5, "description": "天马行空，网红海岛"},
            {"name": "张裕葡萄酒博物馆", "type": "工业旅游", "price": 50, "rating": 4.5, "description": "百年酒庄"},
            {"name": "金沙滩", "type": "海滩风光", "price": 0, "rating": 4.5, "description": "中国北方第一滩"},
            {"name": "南山大佛", "type": "佛教圣地", "price": 120, "rating": 4.5, "description": "世界最大锡青铜坐佛"},
        ],
    },
    "洛阳": {
        "province": "河南",
        "hotels": [
            {"name": "洛阳钼都利豪国际饭店", "type": "豪华型", "price_per_night": 780, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "洛龙区开元大道"},
            {"name": "洛阳老城青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "老城区丽景门"},
        ],
        "restaurants": [
            {"name": "洛阳水席", "cuisine": "洛阳菜", "avg_price": 88, "rating": 4.7, "specialties": ["牡丹燕菜", "连汤肉片", "焦炸丸子"], "address": "老城区"},
            {"name": "不翻汤", "cuisine": "洛阳小吃", "avg_price": 10, "rating": 4.6, "specialties": ["不翻汤", "浆面条", "糊涂面"], "address": "老城区十字街"},
        ],
        "attractions": [
            {"name": "龙门石窟", "type": "世界文化遗产", "price": 90, "rating": 4.9, "description": "中国三大石窟之一，卢舍那大佛"},
            {"name": "白马寺", "type": "佛教圣地", "price": 35, "rating": 4.7, "description": "中国第一古刹"},
            {"name": "洛阳博物馆", "type": "博物馆", "price": 0, "rating": 4.7, "description": "河洛文化，唐三彩"},
            {"name": "老君山", "type": "自然风光", "price": 100, "rating": 4.8, "description": "道教圣地，云海金顶"},
            {"name": "白云山", "type": "自然风光", "price": 75, "rating": 4.6, "description": "中原第一高峰"},
            {"name": "关林", "type": "历史文化", "price": 30, "rating": 4.5, "description": "关公首级埋葬处"},
            {"name": "丽景门", "type": "历史街区", "price": 0, "rating": 4.5, "description": "洛阳古城门，老城十字街"},
        ],
    },
    "金华": {
        "province": "浙江",
        "hotels": [
            {"name": "金华万达嘉华酒店", "type": "豪华型", "price_per_night": 680, "rating": 4.6, "facilities": ["WiFi", "泳池", "健身房"], "address": "婺城区万达广场"},
            {"name": "横店影视城酒店", "type": "主题酒店", "price_per_night": 580, "rating": 4.5, "facilities": ["WiFi", "影视体验"], "address": "东阳市横店"},
        ],
        "restaurants": [
            {"name": "金华煲庄", "cuisine": "金华菜", "avg_price": 78, "rating": 4.6, "specialties": ["金华煲", "金华火腿", "金华汤包"], "address": "婺城区"},
            {"name": "兰溪牛肉面", "cuisine": "面食", "avg_price": 20, "rating": 4.5, "specialties": ["牛肉面", "鸡子粿"], "address": "兰溪市"},
        ],
        "attractions": [
            {"name": "横店影视城", "type": "主题公园", "price": 320, "rating": 4.7, "description": "中国好莱坞，影视拍摄基地"},
            {"name": "双龙洞", "type": "自然奇观", "price": 80, "rating": 4.6, "description": "叶圣陶笔下的双龙洞"},
            {"name": "诸葛八卦村", "type": "古镇风情", "price": 90, "rating": 4.6, "description": "诸葛亮后裔聚居地"},
            {"name": "牛头山", "type": "自然风光", "price": 80, "rating": 4.5, "description": "江南小九寨"},
            {"name": "古子城", "type": "历史街区", "price": 0, "rating": 4.5, "description": "金华古城核心区"},
            {"name": "八咏楼", "type": "历史文化", "price": 0, "rating": 4.4, "description": "李清照题词处"},
            {"name": "横店广州街·香港街", "type": "主题公园", "price": 0, "rating": 4.5, "description": "影视体验区"},
        ],
    },
    "扬州": {
        "province": "江苏",
        "hotels": [
            {"name": "扬州迎宾馆", "type": "豪华型", "price_per_night": 980, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA", "园林"], "address": "邗江区瘦西湖路"},
            {"name": "扬州东关街青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "广陵区东关街"},
        ],
        "restaurants": [
            {"name": "趣园", "cuisine": "淮扬菜", "avg_price": 128, "rating": 4.8, "specialties": ["翡翠烧卖", "五丁包", "大煮干丝"], "address": "邗江区"},
            {"name": "粗茶淡饭", "cuisine": "扬州小吃", "avg_price": 35, "rating": 4.6, "specialties": ["藕粉圆", "四喜汤圆", "扬州炒饭"], "address": "广陵区东关街"},
        ],
        "attractions": [
            {"name": "瘦西湖", "type": "风景名胜", "price": 100, "rating": 4.9, "description": "天下西湖，三十有六，惟瘦西湖"},
            {"name": "个园", "type": "园林古迹", "price": 45, "rating": 4.7, "description": "中国四大名园之一，四季假山"},
            {"name": "何园", "type": "园林古迹", "price": 45, "rating": 4.7, "description": "晚清第一园"},
            {"name": "大明寺", "type": "佛教圣地", "price": 30, "rating": 4.6, "description": "鉴真东渡出发地"},
            {"name": "东关街", "type": "历史街区", "price": 0, "rating": 4.6, "description": "扬州最繁华的商业街"},
            {"name": "文昌阁", "type": "历史文化", "price": 0, "rating": 4.5, "description": "扬州地标建筑"},
            {"name": "京杭大运河", "type": "世界文化遗产", "price": 0, "rating": 4.5, "description": "世界最长的人工运河"},
        ],
    },
}


def _get_city_data(city: str) -> Dict[str, Any]:
    """获取城市数据，如果没有则生成默认数据"""
    # 合并所有数据库，V4 > V3 > V2 > V1 > 核心
    all_dbs = [
        EXTENDED_CITY_DB_V4,
        EXTENDED_CITY_DB_V3,
        EXTENDED_CITY_DB_V2,
        EXTENDED_CITY_DB,
        DESTINATION_DB,
    ]

    # 1. 精确匹配（按优先级）
    for db in all_dbs:
        if city in db:
            return db[city]

    # 2. 模糊匹配（按优先级）
    for db in all_dbs:
        for key in db:
            if key in city or city in key:
                return db[key]

    # 7. 生成默认数据（增加餐厅和景点数量）
    return {
        "province": city,
        "hotels": [
            {"name": f"{city}国际大酒店", "type": "高档型", "price_per_night": 580, "rating": 4.6, "facilities": ["WiFi", "停车场", "餐厅", "健身房"]},
            {"name": f"{city}如家酒店", "type": "舒适型", "price_per_night": 280, "rating": 4.3, "facilities": ["WiFi", "停车场", "早餐"]},
            {"name": f"{city}青年旅舍", "type": "经济型", "price_per_night": 98, "rating": 4.2, "facilities": ["WiFi", "公共厨房"]},
        ],
        "restaurants": [
            {"name": f"{city}特色餐厅", "cuisine": "地方菜", "avg_price": 78, "rating": 4.6, "specialties": ["招牌菜1", "招牌菜2", "招牌菜3"]},
            {"name": f"{city}老字号小吃", "cuisine": "小吃", "avg_price": 38, "rating": 4.5, "specialties": ["特色小吃1", "特色小吃2"]},
            {"name": f"{city}美食广场", "cuisine": "综合", "avg_price": 55, "rating": 4.4, "specialties": ["各地美食"]},
            {"name": f"{city}夜市小吃", "cuisine": "夜市", "avg_price": 30, "rating": 4.4, "specialties": ["烧烤", "小龙虾", "啤酒"]},
            {"name": f"{city}火锅店", "cuisine": "火锅", "avg_price": 88, "rating": 4.5, "specialties": ["鸳鸯锅", "毛肚", "鸭肠"]},
            {"name": f"{city}面馆", "cuisine": "面食", "avg_price": 25, "rating": 4.4, "specialties": ["牛肉面", "馄饨", "水饺"]},
        ],
        "attractions": [
            {"name": f"{city}著名景点1", "type": "风景名胜", "price": 60, "rating": 4.8, "description": f"{city}最著名的景点"},
            {"name": f"{city}著名景点2", "type": "历史文化", "price": 45, "rating": 4.7, "description": f"{city}历史文化景点"},
            {"name": f"{city}著名景点3", "type": "自然风光", "price": 30, "rating": 4.6, "description": f"{city}自然风光景点"},
            {"name": f"{city}公园", "type": "休闲公园", "price": 0, "rating": 4.5, "description": f"{city}市民休闲公园"},
            {"name": f"{city}博物馆", "type": "博物馆", "price": 0, "rating": 4.4, "description": f"{city}地方博物馆"},
            {"name": f"{city}古街", "type": "历史街区", "price": 0, "rating": 4.5, "description": f"{city}传统商业街"},
            {"name": f"{city}广场", "type": "城市地标", "price": 0, "rating": 4.4, "description": f"{city}市中心广场"},
            {"name": f"{city}寺庙", "type": "佛教圣地", "price": 20, "rating": 4.4, "description": f"{city}著名寺庙"},
            {"name": f"{city}大学", "type": "高校参观", "price": 0, "rating": 4.3, "description": f"{city}知名大学"},
            {"name": f"{city}步行街", "type": "购物商圈", "price": 0, "rating": 4.4, "description": f"{city}商业中心"},
            {"name": f"{city}湿地公园", "type": "自然生态", "price": 30, "rating": 4.4, "description": f"{city}生态湿地"},
            {"name": f"{city}古镇", "type": "古镇风情", "price": 50, "rating": 4.5, "description": f"{city}周边古镇"},
            {"name": f"{city}夜景", "type": "城市景观", "price": 0, "rating": 4.5, "description": f"{city}最美夜景"},
            {"name": f"{city}美食街", "type": "美食街区", "price": 0, "rating": 4.4, "description": f"{city}美食聚集地"},
            {"name": f"{city}主题乐园", "type": "主题公园", "price": 150, "rating": 4.4, "description": f"{city}主题乐园"},
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
    """
    搜索酒店 - 优先调用飞猪API，失败时使用本地知识库
    """
    # 1. 优先调用真实API
    api_result = fliggy_api.search_hotels(city, check_in, check_out, count)
    if api_result:
        return json.dumps(api_result, ensure_ascii=False, indent=2)

    # 2. API失败，使用本地知识库兜底
    print(f"[INFO] 使用本地酒店数据: {city}")
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


def search_restaurants(city: str, count: int = 6) -> str:
    """
    搜索餐厅 - 优先调用飞猪/口碑API，失败时使用本地知识库
    """
    # 1. 优先调用真实API
    api_result = fliggy_api.search_restaurants(city, count)
    if api_result:
        return json.dumps(api_result, ensure_ascii=False, indent=2)

    # 2. API失败，使用本地知识库兜底
    print(f"[INFO] 使用本地餐厅数据: {city}")
    city_data = _get_city_data(city)
    restaurants = city_data["restaurants"][:count]

    # 补充完整字段
    for i, restaurant in enumerate(restaurants):
        restaurant.setdefault("city", city)
        restaurant.setdefault("business_hours", "10:00-22:00")
        restaurant.setdefault("review_count", random.randint(200, 8000))
        restaurant.setdefault("images", [f"https://example.com/restaurant{i+1}.jpg"])

    return json.dumps(restaurants, ensure_ascii=False, indent=2)


def search_attractions(city: str, count: int = 12) -> str:
    """
    搜索景点 - 优先调用飞猪API，失败时使用本地知识库
    """
    # 1. 优先调用真实API
    api_result = fliggy_api.search_attractions(city, count)
    if api_result:
        return json.dumps(api_result, ensure_ascii=False, indent=2)

    # 2. API失败，使用本地知识库兜底
    print(f"[INFO] 使用本地景点数据: {city}")
    city_data = _get_city_data(city)
    attractions = city_data["attractions"][:count]

    return json.dumps(attractions, ensure_ascii=False, indent=2)


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
            "description": "搜索餐厅信息，获取餐厅名称、菜系、价格、评分等信息，包含早餐、午餐、晚餐推荐",
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
    {
        "type": "function",
        "function": {
            "name": "search_attractions",
            "description": "搜索景点信息，获取景点名称、类型、门票价格、评分、描述等信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如'大理'"},
                    "count": {"type": "integer", "description": "返回景点数量，默认为7", "default": 7},
                },
                "required": ["city"],
            },
        },
    },
]

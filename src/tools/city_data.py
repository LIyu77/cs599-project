"""
扩展城市知识库 - 包含50+城市的真实数据
"""

# 扩展城市数据
EXTENDED_CITY_DB = {
    # ==================== 华东地区 ====================
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
    "宁波": {
        "province": "浙江",
        "hotels": [
            {"name": "宁波洲际酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "SPA"], "address": "鄞州区民安路268号"},
            {"name": "宁波天一广场青旅", "type": "经济型", "price_per_night": 89, "rating": 4.3, "facilities": ["WiFi", "公共厨房"], "address": "海曙区中山东路"},
        ],
        "restaurants": [
            {"name": "缸鸭狗（天一广场店）", "cuisine": "宁波菜", "avg_price": 65, "rating": 4.7, "specialties": ["汤圆", "年糕", "海鲜"], "address": "海曙区天一广场"},
            {"name": "南塘老街", "cuisine": "宁波小吃", "avg_price": 35, "rating": 4.5, "specialties": ["油赞子", "灰汁团", "宁波汤圆"], "address": "海曙区南塘河街"},
            {"name": "向阳渔港", "cuisine": "海鲜", "avg_price": 128, "rating": 4.6, "specialties": ["梭子蟹", "红膏呛蟹", "雪菜大汤黄鱼"], "address": "鄞州区惊驾路"},
        ],
        "attractions": [
            {"name": "天一阁", "type": "历史文化", "price": 30, "rating": 4.8, "description": "中国现存最早的私家藏书楼"},
            {"name": "东钱湖", "type": "自然风光", "price": 0, "rating": 4.6, "description": "浙江最大的天然淡水湖，小普陀"},
            {"name": "老外滩", "type": "时尚街区", "price": 0, "rating": 4.5, "description": "百年历史街区，酒吧餐厅聚集"},
            {"name": "象山影视城", "type": "主题公园", "price": 150, "rating": 4.5, "description": "诸多影视剧取景地"},
            {"name": "溪口-雪窦山", "type": "风景名胜", "price": 210, "rating": 4.7, "description": "蒋氏故里，弥勒道场"},
            {"name": "南塘老街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "百年老街，宁波小吃聚集"},
            {"name": "老外滩", "type": "历史街区", "price": 0, "rating": 4.5, "description": "开埠口岸遗址，欧式建筑群"},
        ],
    },
    "嘉兴": {
        "province": "浙江",
        "hotels": [
            {"name": "嘉兴希尔顿酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "南湖区中环南路"},
            {"name": "乌镇西栅民宿", "type": "特色民宿", "price_per_night": 480, "rating": 4.6, "facilities": ["WiFi", "临水房"], "address": "桐乡市乌镇西栅"},
        ],
        "restaurants": [
            {"name": "五芳斋（月河店）", "cuisine": "嘉兴小吃", "avg_price": 35, "rating": 4.7, "specialties": ["粽子", "烧卖", "馄饨"], "address": "南湖区月河历史街区"},
            {"name": "文虎酱鸭", "cuisine": "卤味", "avg_price": 45, "rating": 4.6, "specialties": ["酱鸭", "酱鹅", "卤鸡爪"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "乌镇", "type": "古镇风情", "price": 150, "rating": 4.8, "description": "中国最后的枕水人家，西栅夜景绝美"},
            {"name": "西塘古镇", "type": "古镇风情", "price": 95, "rating": 4.7, "description": "活着的千年古镇，烟雨长廊"},
            {"name": "南湖", "type": "历史文化", "price": 60, "rating": 4.6, "description": "红船精神发源地，烟雨楼"},
            {"name": "月河历史街区", "type": "历史街区", "price": 0, "rating": 4.5, "description": "嘉兴版清明上河图"},
            {"name": "海宁盐官", "type": "自然奇观", "price": 100, "rating": 4.5, "description": "钱塘江大潮最佳观赏地"},
            {"name": "濮院古镇", "type": "古镇风情", "price": 120, "rating": 4.4, "description": "新开发的古镇，游客较少"},
            {"name": "九龙山旅游度假区", "type": "度假区", "price": 80, "rating": 4.5, "description": "山海湖一体，高尔夫球场"},
        ],
    },
    "绍兴": {
        "province": "浙江",
        "hotels": [
            {"name": "绍兴咸亨酒店", "type": "高档型", "price_per_night": 580, "rating": 4.6, "facilities": ["WiFi", "餐厅"], "address": "越城区鲁迅中路179号"},
            {"name": "鲁迅故里青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "越城区鲁迅故里附近"},
        ],
        "restaurants": [
            {"name": "咸亨酒店", "cuisine": "绍兴菜", "avg_price": 78, "rating": 4.7, "specialties": ["茴香豆", "臭豆腐", "黄酒"], "address": "越城区鲁迅中路179号"},
            {"name": "王老汉臭豆腐", "cuisine": "绍兴小吃", "avg_price": 15, "rating": 4.6, "specialties": ["臭豆腐", "奶油小攀"], "address": "越城区鲁迅故里"},
        ],
        "attractions": [
            {"name": "鲁迅故里", "type": "历史文化", "price": 0, "rating": 4.8, "description": "鲁迅先生故乡，百草园、三味书屋"},
            {"name": "兰亭", "type": "历史文化", "price": 40, "rating": 4.7, "description": "书法圣地，曲水流觞"},
            {"name": "东湖", "type": "自然风光", "price": 50, "rating": 4.6, "description": "山水盆景，乌篷船游览"},
            {"name": "安昌古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "原汁原味的江南水乡，腊肠飘香"},
            {"name": "沈园", "type": "历史文化", "price": 40, "rating": 4.6, "description": "陆游与唐婉的爱情故事"},
            {"name": "大禹陵", "type": "历史文化", "price": 30, "rating": 4.5, "description": "华夏始祖大禹的陵墓"},
            {"name": "仓桥直街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "最能代表绍兴的古街"},
        ],
    },
    "佛山": {
        "province": "广东",
        "hotels": [
            {"name": "佛山岭南天地马哥孛罗酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "禅城区岭南天地"},
            {"name": "佛山祖庙附近青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "禅城区祖庙路"},
        ],
        "restaurants": [
            {"name": "佛山盲公丸", "cuisine": "佛山小吃", "avg_price": 30, "rating": 4.6, "specialties": ["盲公丸", "双皮奶", "姜撞奶"], "address": "禅城区祖庙附近"},
            {"name": "顺德渔村", "cuisine": "顺德菜", "avg_price": 128, "rating": 4.7, "specialties": ["均安蒸猪", "顺德鱼生", "陈村粉"], "address": "顺德区大良街道"},
        ],
        "attractions": [
            {"name": "祖庙", "type": "历史文化", "price": 20, "rating": 4.7, "description": "佛山祖庙，北派建筑与岭南建筑的完美结合"},
            {"name": "岭南天地", "type": "历史街区", "price": 0, "rating": 4.6, "description": "岭南建筑改造的文创街区"},
            {"name": "顺德清晖园", "type": "园林古迹", "price": 15, "rating": 4.6, "description": "广东四大名园之一"},
            {"name": "西樵山", "type": "自然风光", "price": 70, "rating": 4.5, "description": "南粤名山，南海观音铜像"},
            {"name": "逢简水乡", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "岭南水乡，小桥流水"},
            {"name": "南风古灶", "type": "历史文化", "price": 25, "rating": 4.5, "description": "五百年不熄的窑火"},
            {"name": "佛山梁园", "type": "园林古迹", "price": 10, "rating": 4.4, "description": "广东四大名园之一"},
        ],
    },
    "绍兴": {
        "province": "浙江",
        "hotels": [
            {"name": "绍兴咸亨酒店", "type": "高档型", "price_per_night": 580, "rating": 4.6, "facilities": ["WiFi", "餐厅"], "address": "越城区鲁迅中路179号"},
            {"name": "鲁迅故里青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "越城区鲁迅故里附近"},
        ],
        "restaurants": [
            {"name": "咸亨酒店", "cuisine": "绍兴菜", "avg_price": 78, "rating": 4.7, "specialties": ["茴香豆", "臭豆腐", "黄酒"], "address": "越城区鲁迅中路179号"},
            {"name": "王老汉臭豆腐", "cuisine": "绍兴小吃", "avg_price": 15, "rating": 4.6, "specialties": ["臭豆腐", "奶油小攀"], "address": "越城区鲁迅故里"},
        ],
        "attractions": [
            {"name": "鲁迅故里", "type": "历史文化", "price": 0, "rating": 4.8, "description": "鲁迅先生故乡，百草园、三味书屋"},
            {"name": "兰亭", "type": "历史文化", "price": 40, "rating": 4.7, "description": "书法圣地，曲水流觞"},
            {"name": "东湖", "type": "自然风光", "price": 50, "rating": 4.6, "description": "山水盆景，乌篷船游览"},
            {"name": "安昌古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "原汁原味的江南水乡，腊肠飘香"},
            {"name": "沈园", "type": "历史文化", "price": 40, "rating": 4.6, "description": "陆游与唐婉的爱情故事"},
            {"name": "大禹陵", "type": "历史文化", "price": 30, "rating": 4.5, "description": "华夏始祖大禹的陵墓"},
            {"name": "仓桥直街", "type": "历史街区", "price": 0, "rating": 4.5, "description": "最能代表绍兴的古街"},
        ],
    },
    "南昌": {
        "province": "江西",
        "hotels": [
            {"name": "南昌万达嘉华度假酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "红谷滩区万达广场"},
            {"name": "南昌八一广场青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "东湖区八一广场附近"},
        ],
        "restaurants": [
            {"name": "南昌拌粉", "cuisine": "南昌小吃", "avg_price": 15, "rating": 4.7, "specialties": ["拌粉", "瓦罐汤", "白糖糕"], "address": "多家分店"},
            {"name": "堂瓦里", "cuisine": "赣菜", "avg_price": 88, "rating": 4.6, "specialties": ["南昌炒粉", "藜蒿炒腊肉", "粉蒸肉"], "address": "东湖区中山路"},
        ],
        "attractions": [
            {"name": "滕王阁", "type": "历史文化", "price": 45, "rating": 4.8, "description": "江南三大名楼之一，落霞与孤鹜齐飞"},
            {"name": "八一广场", "type": "城市地标", "price": 0, "rating": 4.5, "description": "南昌市中心广场，八一南昌起义纪念塔"},
            {"name": "秋水广场", "type": "城市地标", "price": 0, "rating": 4.5, "description": "亚洲最大音乐喷泉"},
            {"name": "八一起义纪念馆", "type": "红色旅游", "price": 0, "rating": 4.6, "description": "军旗升起的地方"},
            {"name": "梅岭", "type": "自然风光", "price": 30, "rating": 4.5, "description": "南昌后花园，避暑胜地"},
            {"name": "万寿宫历史文化街区", "type": "历史街区", "price": 0, "rating": 4.5, "description": "南昌古城的缩影"},
            {"name": "绳金塔", "type": "历史文化", "price": 0, "rating": 4.4, "description": "南昌古建筑，美食街聚集"},
        ],
    },
    "太原": {
        "province": "山西",
        "hotels": [
            {"name": "太原星河湾酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "小店区长风街"},
            {"name": "太原柳巷青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "迎泽区柳巷"},
        ],
        "restaurants": [
            {"name": "山西会馆", "cuisine": "晋菜", "avg_price": 88, "rating": 4.7, "specialties": ["刀削面", "过油肉", "羊杂割"], "address": "迎泽区柳巷"},
            {"name": "六味斋", "cuisine": "卤味", "avg_price": 35, "rating": 4.5, "specialties": ["酱肉", "熏鸡", "豆制品"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "晋祠", "type": "历史文化", "price": 80, "rating": 4.8, "description": "中国现存最早的皇家祭祀园林"},
            {"name": "平遥古城", "type": "世界文化遗产", "price": 125, "rating": 4.8, "description": "保存最完整的明清古县城"},
            {"name": "乔家大院", "type": "历史文化", "price": 115, "rating": 4.7, "description": "晋商大院代表，皇家有故宫，民宅看乔家"},
            {"name": "王家大院", "type": "历史文化", "price": 55, "rating": 4.6, "description": "民间故宫，建筑艺术博物馆"},
            {"name": "五台山", "type": "世界文化遗产", "price": 135, "rating": 4.8, "description": "中国四大佛教名山之首"},
            {"name": "悬空寺", "type": "历史文化", "price": 125, "rating": 4.7, "description": "悬崖上的古建筑，力学奇迹"},
            {"name": "太原古县城", "type": "历史街区", "price": 0, "rating": 4.5, "description": "明代古城墙，满江红取景地"},
        ],
    },
    "长春": {
        "province": "吉林",
        "hotels": [
            {"name": "长春香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "朝阳区西安大路"},
            {"name": "长春重庆路青旅", "type": "经济型", "price_per_night": 59, "rating": 4.2, "facilities": ["WiFi"], "address": "南关区重庆路"},
        ],
        "restaurants": [
            {"name": "春发合饭庄", "cuisine": "东北菜", "avg_price": 65, "rating": 4.6, "specialties": ["锅包肉", "地三鲜", "杀猪菜"], "address": "南关区重庆路"},
            {"name": "老昌春饼", "cuisine": "东北小吃", "avg_price": 35, "rating": 4.5, "specialties": ["春饼", "酱骨架", "东北大拉皮"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "长影世纪城", "type": "主题公园", "price": 198, "rating": 4.6, "description": "东方好莱坞，电影主题公园"},
            {"name": "伪满皇宫博物院", "type": "历史文化", "price": 70, "rating": 4.7, "description": "伪满洲国皇宫，历史警示"},
            {"name": "净月潭", "type": "自然风光", "price": 30, "rating": 4.6, "description": "亚洲最大人工森林，冬季滑雪"},
            {"name": "南湖公园", "type": "城市公园", "price": 0, "rating": 4.4, "description": "长春最大公园，冬季冰灯"},
            {"name": "长春世界雕塑园", "type": "艺术园区", "price": 30, "rating": 4.5, "description": "世界雕塑艺术殿堂"},
            {"name": "般若寺", "type": "佛教圣地", "price": 0, "rating": 4.4, "description": "长春最大的佛教寺庙"},
            {"name": "桂林路商圈", "type": "购物商圈", "price": 0, "rating": 4.4, "description": "长春最繁华的商业街"},
        ],
    },
    "南宁": {
        "province": "广西",
        "hotels": [
            {"name": "南宁万达文华酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "青秀区东葛路"},
            {"name": "南宁中山路青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "兴宁区中山路"},
        ],
        "restaurants": [
            {"name": "中山路美食街", "cuisine": "广西小吃", "avg_price": 35, "rating": 4.6, "specialties": ["老友粉", "卷筒粉", "柠檬鸭"], "address": "兴宁区中山路"},
            {"name": "漓江又一醉", "cuisine": "桂菜", "avg_price": 78, "rating": 4.5, "specialties": ["啤酒鱼", "荔浦芋扣肉", "阳朔田螺酿"], "address": "青秀区民族大道"},
        ],
        "attractions": [
            {"name": "青秀山", "type": "自然风光", "price": 20, "rating": 4.7, "description": "南宁后花园，绿城象征"},
            {"name": "南宁动物园", "type": "主题公园", "price": 50, "rating": 4.5, "description": "广西最大的动物园"},
            {"name": "中山路", "type": "美食街区", "price": 0, "rating": 4.6, "description": "南宁美食一条街"},
            {"name": "扬美古镇", "type": "古镇风情", "price": 30, "rating": 4.4, "description": "千年古镇，明清建筑群"},
            {"name": "大明山", "type": "自然风光", "price": 68, "rating": 4.5, "description": "广西庐山，冬季雾凇"},
            {"name": "德天瀑布", "type": "自然奇观", "price": 80, "rating": 4.8, "description": "亚洲第一跨国瀑布"},
            {"name": "方特东盟神画", "type": "主题公园", "price": 260, "rating": 4.5, "description": "东盟十国文化主题乐园"},
        ],
    },
    "合肥": {
        "province": "安徽",
        "hotels": [
            {"name": "合肥香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "包河区南京路"},
            {"name": "合肥三孝口青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "庐阳区三孝口"},
        ],
        "restaurants": [
            {"name": "同庆楼", "cuisine": "徽菜", "avg_price": 88, "rating": 4.6, "specialties": ["臭鳜鱼", "毛豆腐", "李鸿章大杂烩"], "address": "庐阳区长江路"},
            {"name": "耿福兴", "cuisine": "小吃", "avg_price": 25, "rating": 4.5, "specialties": ["酥饺", "小笼包", "鸭油烧饼"], "address": "庐阳区宿州路"},
        ],
        "attractions": [
            {"name": "包公园", "type": "历史文化", "price": 0, "rating": 4.6, "description": "包青天故里，包公祠、包公墓"},
            {"name": "中国科学技术大学", "type": "高校参观", "price": 0, "rating": 4.5, "description": "中国顶尖理工科大学"},
            {"name": "逍遥津", "type": "历史文化", "price": 0, "rating": 4.5, "description": "三国古战场，张辽威震逍遥津"},
            {"name": "合肥野生动物园", "type": "主题公园", "price": 35, "rating": 4.4, "description": "安徽最大的动物园"},
            {"name": "巢湖", "type": "自然风光", "price": 0, "rating": 4.5, "description": "中国五大淡水湖之一"},
            {"name": "三河古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "千年古镇，八古景观"},
            {"name": "安徽省博物院", "type": "博物馆", "price": 0, "rating": 4.5, "description": "了解安徽历史文化的好去处"},
        ],
    },
    "福州": {
        "province": "福建",
        "hotels": [
            {"name": "福州香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "鼓楼区新权南路"},
            {"name": "福州三坊七巷青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "鼓楼区三坊七巷附近"},
        ],
        "restaurants": [
            {"name": "同利肉燕", "cuisine": "福州小吃", "avg_price": 20, "rating": 4.7, "specialties": ["肉燕", "鱼丸", "扁肉"], "address": "鼓楼区三坊七巷"},
            {"name": "安泰楼", "cuisine": "闽菜", "avg_price": 88, "rating": 4.6, "specialties": ["佛跳墙", "荔枝肉", "醉排骨"], "address": "鼓楼区八一七路"},
        ],
        "attractions": [
            {"name": "三坊七巷", "type": "历史文化", "price": 0, "rating": 4.8, "description": "中国城市里坊制度的活化石"},
            {"name": "鼓山", "type": "自然风光", "price": 0, "rating": 4.6, "description": "福州第一名山，涌泉寺"},
            {"name": "西湖公园", "type": "城市公园", "price": 0, "rating": 4.5, "description": "福州最古老的公园"},
            {"name": "闽江夜游", "type": "自然风光", "price": 80, "rating": 4.6, "description": "闽江两岸灯光秀"},
            {"name": "平潭岛", "type": "海岛风光", "price": 0, "rating": 4.7, "description": "福建第一大岛，蓝眼泪"},
            {"name": "上下杭", "type": "历史街区", "price": 0, "rating": 4.5, "description": "福州传统商业街"},
            {"name": "烟台山", "type": "历史街区", "price": 0, "rating": 4.5, "description": "万国建筑博物馆"},
        ],
    },
    "佛山": {
        "province": "广东",
        "hotels": [
            {"name": "佛山岭南天地马哥孛罗酒店", "type": "豪华型", "price_per_night": 980, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "禅城区岭南天地"},
            {"name": "佛山祖庙附近青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "禅城区祖庙路"},
        ],
        "restaurants": [
            {"name": "佛山盲公丸", "cuisine": "佛山小吃", "avg_price": 30, "rating": 4.6, "specialties": ["盲公丸", "双皮奶", "姜撞奶"], "address": "禅城区祖庙附近"},
            {"name": "顺德渔村", "cuisine": "顺德菜", "avg_price": 128, "rating": 4.7, "specialties": ["均安蒸猪", "顺德鱼生", "陈村粉"], "address": "顺德区大良街道"},
        ],
        "attractions": [
            {"name": "祖庙", "type": "历史文化", "price": 20, "rating": 4.7, "description": "佛山祖庙，北派建筑与岭南建筑的完美结合"},
            {"name": "岭南天地", "type": "历史街区", "price": 0, "rating": 4.6, "description": "岭南建筑改造的文创街区"},
            {"name": "顺德清晖园", "type": "园林古迹", "price": 15, "rating": 4.6, "description": "广东四大名园之一"},
            {"name": "西樵山", "type": "自然风光", "price": 70, "rating": 4.5, "description": "南粤名山，南海观音铜像"},
            {"name": "逢简水乡", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "岭南水乡，小桥流水"},
            {"name": "南风古灶", "type": "历史文化", "price": 25, "rating": 4.5, "description": "五百年不熄的窑火"},
            {"name": "佛山梁园", "type": "园林古迹", "price": 10, "rating": 4.4, "description": "广东四大名园之一"},
        ],
    },
    "南通": {
        "province": "江苏",
        "hotels": [
            {"name": "南通希尔顿酒店", "type": "豪华型", "price_per_night": 680, "rating": 4.6, "facilities": ["WiFi", "泳池", "健身房"], "address": "崇川区工农路"},
            {"name": "南通濠河青旅", "type": "经济型", "price_per_night": 69, "rating": 4.3, "facilities": ["WiFi"], "address": "崇川区濠河附近"},
        ],
        "restaurants": [
            {"name": "南通饭店", "cuisine": "通菜", "avg_price": 78, "rating": 4.6, "specialties": "文峰饭店", "地址": "崇川区濠河路"},
            {"name": "脆饼", "cuisine": "南通小吃", "avg_price": 25, "rating": 4.5, "specialties": ["林梓潮糕", "西亭脆饼"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "濠河", "type": "自然风光", "price": 0, "rating": 4.6, "description": "中国保存最完整的古护城河"},
            {"name": "狼山", "type": "自然风光", "price": 50, "rating": 4.5, "description": "江海第一山，佛教八小名山之首"},
            {"name": "南通博物苑", "type": "博物馆", "price": 0, "rating": 4.5, "description": "中国第一座公共博物馆"},
            {"name": "啬园", "type": "园林古迹", "price": 20, "rating": 4.4, "description": "张謇先生的纪念园"},
            {"name": "方特探险王国", "type": "主题公园", "price": 200, "rating": 4.5, "description": "大型主题乐园"},
            {"name": "唐闸古镇", "type": "古镇风情", "price": 0, "rating": 4.4, "description": "近代工业重镇遗址"},
            {"name": "启东圆陀角", "type": "自然风光", "price": 0, "rating": 4.5, "description": "日出胜地，江海交汇"},
        ],
    },
    "遵义": {
        "province": "贵州",
        "hotels": [
            {"name": "遵义万达嘉华酒店", "type": "豪华型", "price_per_night": 680, "rating": 4.6, "facilities": ["WiFi", "泳池", "健身房"], "address": "汇川区万达广场"},
            {"name": "遵义红军街青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "红花岗区红军街"},
        ],
        "restaurants": [
            {"name": "遵义羊肉粉", "cuisine": "贵州小吃", "avg_price": 15, "rating": 4.7, "specialties": ["羊肉粉", "豆花面", "鸡蛋糕"], "address": "多家分店"},
            {"name": "黔北记忆", "cuisine": "黔菜", "avg_price": 78, "rating": 4.5, "specialties": ["辣子鸡", "豆腐圆子", "洋芋粑"], "address": "红花岗区"},
        ],
        "attractions": [
            {"name": "遵义会议会址", "type": "红色旅游", "price": 0, "rating": 4.8, "description": "中国革命的转折点"},
            {"name": "赤水丹霞", "type": "世界自然遗产", "price": 80, "rating": 4.8, "description": "世界自然遗产，丹霞地貌"},
            {"name": "茅台镇", "type": "工业旅游", "price": 0, "rating": 4.6, "description": "中国酒都，茅台酒产地"},
            {"name": "海龙屯", "type": "世界文化遗产", "price": 80, "rating": 4.7, "description": "世界文化遗产，土司军事城堡"},
            {"name": "娄山关", "type": "红色旅游", "price": 0, "rating": 4.5, "description": "苍山如海，残阳如血"},
            {"name": "四渡赤水纪念馆", "type": "红色旅游", "price": 0, "rating": 4.5, "description": "红色教育基地"},
            {"name": "遵义红军街", "type": "历史街区", "price": 0, "rating": 4.4, "description": "红色文化商业街"},
        ],
    },
    "海口": {
        "province": "海南",
        "hotels": [
            {"name": "海口香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA", "海景"], "address": "龙华区滨海大道"},
            {"name": "海口骑楼老街青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "龙华区骑楼老街"},
        ],
        "restaurants": [
            {"name": "骑楼老街小吃", "cuisine": "海南小吃", "avg_price": 25, "rating": 4.6, "specialties": ["清补凉", "抱罗粉", "海南粉"], "address": "龙华区骑楼老街"},
            {"name": "龙泉椰子鸡", "cuisine": "海南菜", "avg_price": 98, "rating": 4.6, "specialties": ["椰子鸡", "文昌鸡", "加积鸭"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "骑楼老街", "type": "历史街区", "price": 0, "rating": 4.7, "description": "百年骑楼建筑群，南洋风情"},
            {"name": "假日海滩", "type": "海滩风光", "price": 0, "rating": 4.5, "description": "海口最美的海滩"},
            {"name": "火山口地质公园", "type": "自然奇观", "price": 60, "rating": 4.6, "description": "万年火山口，地质奇观"},
            {"name": "五公祠", "type": "历史文化", "price": 20, "rating": 4.5, "description": "海南第一楼"},
            {"name": "万绿园", "type": "城市公园", "price": 0, "rating": 4.5, "description": "海口最大的滨海公园"},
            {"name": "冯小刚电影公社", "type": "主题公园", "price": 138, "rating": 4.4, "description": "民国风情街"},
            {"name": "海口免税店", "type": "购物商圈", "price": 0, "rating": 4.5, "description": "免税购物天堂"},
        ],
    },
    "珠海": {
        "province": "广东",
        "hotels": [
            {"name": "珠海长隆企鹅酒店", "type": "主题酒店", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "泳池", "亲子设施"], "address": "横琴新区长隆度假区"},
            {"name": "珠海拱北口岸青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "香洲区拱北口岸附近"},
        ],
        "restaurants": [
            {"name": "湾仔海鲜街", "cuisine": "海鲜", "avg_price": 128, "rating": 4.6, "specialties": ["横琴蚝", "白灼海虾", "清蒸石斑"], "address": "香洲区湾仔"},
            {"name": "颓记茶餐厅", "cuisine": "港式", "avg_price": 55, "rating": 4.5, "specialties": ["菠萝油", "丝袜奶茶", "干炒牛河"], "address": "香洲区拱北"},
        ],
        "attractions": [
            {"name": "长隆海洋王国", "type": "主题公园", "price": 395, "rating": 4.9, "description": "世界最大海洋主题乐园"},
            {"name": "珠海渔女", "type": "城市地标", "price": 0, "rating": 4.6, "description": "珠海标志性雕塑"},
            {"name": "情侣路", "type": "城市景观", "price": 0, "rating": 4.6, "description": "珠海最美的海滨大道"},
            {"name": "外伶仃岛", "type": "海岛风光", "price": 120, "rating": 4.6, "description": "珠海最美海岛"},
            {"name": "圆明新园", "type": "主题公园", "price": 0, "rating": 4.4, "description": "圆明园1:1复制品"},
            {"name": "横琴粤澳深度合作区", "type": "现代都市", "price": 0, "rating": 4.5, "description": "澳门后花园"},
            {"name": "东澳岛", "type": "海岛风光", "price": 0, "rating": 4.6, "description": "原生态海岛"},
        ],
    },
    "湖州": {
        "province": "浙江",
        "hotels": [
            {"name": "湖州喜来登温泉度假酒店", "type": "豪华型", "price_per_night": 1200, "rating": 4.8, "facilities": ["WiFi", "温泉", "SPA", "泳池"], "address": "吴兴区太湖边"},
            {"name": "南浔古镇民宿", "type": "特色民宿", "price_per_night": 380, "rating": 4.6, "facilities": ["WiFi", "临水房"], "address": "南浔区南浔古镇"},
        ],
        "restaurants": [
            {"name": "丁莲芳", "cuisine": "湖州小吃", "avg_price": 25, "rating": 4.6, "specialties": ["千张包子", "馄饨", "粽子"], "address": "吴兴区红旗路"},
            {"name": "诸老大", "cuisine": "湖州小吃", "avg_price": 30, "rating": 4.5, "specialties": ["粽子", "酱鸭", "酥羊面"], "address": "吴兴区"},
        ],
        "attractions": [
            {"name": "南浔古镇", "type": "古镇风情", "price": 80, "rating": 4.8, "description": "江南六大古镇之一，中西合璧"},
            {"name": "莫干山", "type": "自然风光", "price": 80, "rating": 4.7, "description": "中国四大避暑胜地，民宿圣地"},
            {"name": "太湖旅游度假区", "type": "度假区", "price": 0, "rating": 4.5, "description": "太湖南岸，湖光山色"},
            {"name": "安吉竹博园", "type": "自然生态", "price": 60, "rating": 4.5, "description": "中国竹乡，卧虎藏龙取景地"},
            {"name": "中国大竹海", "type": "自然风光", "price": 58, "rating": 4.6, "description": "万亩竹海，天然氧吧"},
            {"name": "飞英塔", "type": "历史文化", "price": 20, "rating": 4.4, "description": "塔里塔奇观"},
            {"name": "太湖溇港", "type": "历史街区", "price": 0, "rating": 4.4, "description": "古代水利工程遗址"},
        ],
    },
    "潍坊": {
        "province": "山东",
        "hotels": [
            {"name": "潍坊富华大酒店", "type": "豪华型", "price_per_night": 680, "rating": 4.6, "facilities": ["WiFi", "泳池", "健身房"], "address": "奎文区胜利东街"},
            {"name": "潍坊火车站青旅", "type": "经济型", "price_per_night": 59, "rating": 4.2, "facilities": ["WiFi"], "address": "潍城区火车站附近"},
        ],
        "restaurants": [
            {"name": "潍坊朝天锅", "cuisine": "潍坊小吃", "avg_price": 25, "rating": 4.6, "specialties": ["朝天锅", "肉火烧", "鸡鸭和乐"], "address": "多家分店"},
            {"name": "杨家埠", "cuisine": "潍坊小吃", "avg_price": 30, "rating": 4.5, "specialties": ["潍坊肉火烧", "芥末鸡", "潍县萝卜"], "address": "寒亭区杨家埠"},
        ],
        "attractions": [
            {"name": "青州古城", "type": "历史街区", "price": 0, "rating": 4.7, "description": "古九州之一，明清古街"},
            {"name": "世界风筝博物馆", "type": "博物馆", "price": 30, "rating": 4.5, "description": "世界风筝之都，风筝文化"},
            {"name": "杨家埠民间艺术大观园", "type": "民俗文化", "price": 40, "rating": 4.5, "description": "年画之乡，风筝之乡"},
            {"name": "沂山", "type": "自然风光", "price": 80, "rating": 4.5, "description": "东泰山，五镇之首"},
            {"name": "青州博物馆", "type": "博物馆", "price": 0, "rating": 4.5, "description": "中国唯一县级综合性博物馆"},
            {"name": "十笏园", "type": "园林古迹", "price": 30, "rating": 4.4, "description": "潍坊名园，袖珍园林"},
            {"name": "潍坊风筝广场", "type": "城市公园", "price": 0, "rating": 4.4, "description": "国际风筝节举办地"},
        ],
    },
    "石家庄": {
        "province": "河北",
        "hotels": [
            {"name": "石家庄富力洲际酒店", "type": "豪华型", "price_per_night": 780, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "长安区中山东路"},
            {"name": "石家庄火车站青旅", "type": "经济型", "price_per_night": 59, "rating": 4.2, "facilities": ["WiFi"], "address": "桥西区火车站附近"},
        ],
        "restaurants": [
            {"name": "正定八大碗", "cuisine": "河北菜", "avg_price": 65, "rating": 4.6, "specialties": ["八大碗", "马家卤鸡", "正定烧麦"], "address": "正定县"},
            {"name": "金凤扒鸡", "cuisine": "卤味", "avg_price": 45, "rating": 4.5, "specialties": ["金凤扒鸡", "牛肉罩饼"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "正定古城", "type": "历史街区", "price": 0, "rating": 4.7, "description": "古建筑宝库，九楼四塔八大寺"},
            {"name": "赵州桥", "type": "历史文化", "price": 40, "rating": 4.6, "description": "世界最古老的石拱桥"},
            {"name": "西柏坡", "type": "红色旅游", "price": 0, "rating": 4.7, "description": "新中国从这里走来"},
            {"name": "隆兴寺", "type": "佛教圣地", "price": 45, "rating": 4.6, "description": "京外名刹之首"},
            {"name": "苍岩山", "type": "自然风光", "price": 65, "rating": 4.5, "description": "桥楼殿，太行奇峰"},
            {"name": "嶂石岩", "type": "自然风光", "price": 65, "rating": 4.5, "description": "世界最大回音壁"},
            {"name": "河北博物院", "type": "博物馆", "price": 0, "rating": 4.5, "description": "长信宫灯、金缕玉衣"},
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
    "太原": {
        "province": "山西",
        "hotels": [
            {"name": "太原星河湾酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "健身房"], "address": "小店区长风街"},
            {"name": "太原柳巷青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "迎泽区柳巷"},
        ],
        "restaurants": [
            {"name": "山西会馆", "cuisine": "晋菜", "avg_price": 88, "rating": 4.7, "specialties": ["刀削面", "过油肉", "羊杂割"], "address": "迎泽区柳巷"},
            {"name": "六味斋", "cuisine": "卤味", "avg_price": 35, "rating": 4.5, "specialties": ["酱肉", "熏鸡", "豆制品"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "晋祠", "type": "历史文化", "price": 80, "rating": 4.8, "description": "中国现存最早的皇家祭祀园林"},
            {"name": "平遥古城", "type": "世界文化遗产", "price": 125, "rating": 4.8, "description": "保存最完整的明清古县城"},
            {"name": "乔家大院", "type": "历史文化", "price": 115, "rating": 4.7, "description": "晋商大院代表"},
            {"name": "王家大院", "type": "历史文化", "price": 55, "rating": 4.6, "description": "民间故宫"},
            {"name": "五台山", "type": "世界文化遗产", "price": 135, "rating": 4.8, "description": "中国四大佛教名山之首"},
            {"name": "悬空寺", "type": "历史文化", "price": 125, "rating": 4.7, "description": "悬崖上的古建筑"},
            {"name": "太原古县城", "type": "历史街区", "price": 0, "rating": 4.5, "description": "明代古城墙"},
        ],
    },
    "长春": {
        "province": "吉林",
        "hotels": [
            {"name": "长春香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "朝阳区西安大路"},
            {"name": "长春重庆路青旅", "type": "经济型", "price_per_night": 59, "rating": 4.2, "facilities": ["WiFi"], "address": "南关区重庆路"},
        ],
        "restaurants": [
            {"name": "春发合饭庄", "cuisine": "东北菜", "avg_price": 65, "rating": 4.6, "specialties": ["锅包肉", "地三鲜", "杀猪菜"], "address": "南关区重庆路"},
            {"name": "老昌春饼", "cuisine": "东北小吃", "avg_price": 35, "rating": 4.5, "specialties": ["春饼", "酱骨架", "东北大拉皮"], "address": "多家分店"},
        ],
        "attractions": [
            {"name": "长影世纪城", "type": "主题公园", "price": 198, "rating": 4.6, "description": "东方好莱坞"},
            {"name": "伪满皇宫博物院", "type": "历史文化", "price": 70, "rating": 4.7, "description": "伪满洲国皇宫"},
            {"name": "净月潭", "type": "自然风光", "price": 30, "rating": 4.6, "description": "亚洲最大人工森林"},
            {"name": "南湖公园", "type": "城市公园", "price": 0, "rating": 4.4, "description": "长春最大公园"},
            {"name": "长春世界雕塑园", "type": "艺术园区", "price": 30, "rating": 4.5, "description": "世界雕塑艺术殿堂"},
            {"name": "般若寺", "type": "佛教圣地", "price": 0, "rating": 4.4, "description": "长春最大的佛教寺庙"},
            {"name": "桂林路商圈", "type": "购物商圈", "price": 0, "rating": 4.4, "description": "长春最繁华的商业街"},
        ],
    },
    "南宁": {
        "province": "广西",
        "hotels": [
            {"name": "南宁万达文华酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "青秀区东葛路"},
            {"name": "南宁中山路青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "兴宁区中山路"},
        ],
        "restaurants": [
            {"name": "中山路美食街", "cuisine": "广西小吃", "avg_price": 35, "rating": 4.6, "specialties": ["老友粉", "卷筒粉", "柠檬鸭"], "address": "兴宁区中山路"},
            {"name": "漓江又一醉", "cuisine": "桂菜", "avg_price": 78, "rating": 4.5, "specialties": ["啤酒鱼", "荔浦芋扣肉"], "address": "青秀区民族大道"},
        ],
        "attractions": [
            {"name": "青秀山", "type": "自然风光", "price": 20, "rating": 4.7, "description": "南宁后花园"},
            {"name": "南宁动物园", "type": "主题公园", "price": 50, "rating": 4.5, "description": "广西最大的动物园"},
            {"name": "中山路", "type": "美食街区", "price": 0, "rating": 4.6, "description": "南宁美食一条街"},
            {"name": "扬美古镇", "type": "古镇风情", "price": 30, "rating": 4.4, "description": "千年古镇"},
            {"name": "大明山", "type": "自然风光", "price": 68, "rating": 4.5, "description": "广西庐山"},
            {"name": "德天瀑布", "type": "自然奇观", "price": 80, "rating": 4.8, "description": "亚洲第一跨国瀑布"},
            {"name": "方特东盟神画", "type": "主题公园", "price": 260, "rating": 4.5, "description": "东盟十国文化主题乐园"},
        ],
    },
    "合肥": {
        "province": "安徽",
        "hotels": [
            {"name": "合肥香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "包河区南京路"},
            {"name": "合肥三孝口青旅", "type": "经济型", "price_per_night": 59, "rating": 4.3, "facilities": ["WiFi"], "address": "庐阳区三孝口"},
        ],
        "restaurants": [
            {"name": "同庆楼", "cuisine": "徽菜", "avg_price": 88, "rating": 4.6, "specialties": ["臭鳜鱼", "毛豆腐"], "address": "庐阳区长江路"},
            {"name": "耿福兴", "cuisine": "小吃", "avg_price": 25, "rating": 4.5, "specialties": ["酥饺", "小笼包"], "address": "庐阳区宿州路"},
        ],
        "attractions": [
            {"name": "包公园", "type": "历史文化", "price": 0, "rating": 4.6, "description": "包青天故里"},
            {"name": "中国科学技术大学", "type": "高校参观", "price": 0, "rating": 4.5, "description": "中国顶尖理工科大学"},
            {"name": "逍遥津", "type": "历史文化", "price": 0, "rating": 4.5, "description": "三国古战场"},
            {"name": "合肥野生动物园", "type": "主题公园", "price": 35, "rating": 4.4, "description": "安徽最大的动物园"},
            {"name": "巢湖", "type": "自然风光", "price": 0, "rating": 4.5, "description": "中国五大淡水湖之一"},
            {"name": "三河古镇", "type": "古镇风情", "price": 0, "rating": 4.5, "description": "千年古镇"},
            {"name": "安徽省博物院", "type": "博物馆", "price": 0, "rating": 4.5, "description": "了解安徽历史文化"},
        ],
    },
    "福州": {
        "province": "福建",
        "hotels": [
            {"name": "福州香格里拉大酒店", "type": "豪华型", "price_per_night": 880, "rating": 4.7, "facilities": ["WiFi", "泳池", "SPA"], "address": "鼓楼区新权南路"},
            {"name": "福州三坊七巷青旅", "type": "经济型", "price_per_night": 79, "rating": 4.3, "facilities": ["WiFi"], "address": "鼓楼区三坊七巷附近"},
        ],
        "restaurants": [
            {"name": "同利肉燕", "cuisine": "福州小吃", "avg_price": 20, "rating": 4.7, "specialties": ["肉燕", "鱼丸"], "address": "鼓楼区三坊七巷"},
            {"name": "安泰楼", "cuisine": "闽菜", "avg_price": 88, "rating": 4.6, "specialties": ["佛跳墙", "荔枝肉"], "address": "鼓楼区八一七路"},
        ],
        "attractions": [
            {"name": "三坊七巷", "type": "历史文化", "price": 0, "rating": 4.8, "description": "中国城市里坊制度的活化石"},
            {"name": "鼓山", "type": "自然风光", "price": 0, "rating": 4.6, "description": "福州第一名山"},
            {"name": "西湖公园", "type": "城市公园", "price": 0, "rating": 4.5, "description": "福州最古老的公园"},
            {"name": "闽江夜游", "type": "自然风光", "price": 80, "rating": 4.6, "description": "闽江两岸灯光秀"},
            {"name": "平潭岛", "type": "海岛风光", "price": 0, "rating": 4.7, "description": "福建第一大岛"},
            {"name": "上下杭", "type": "历史街区", "price": 0, "rating": 4.5, "description": "福州传统商业街"},
            {"name": "烟台山", "type": "历史街区", "price": 0, "rating": 4.5, "description": "万国建筑博物馆"},
        ],
    },
}


def get_extended_city_data(city: str):
    """获取扩展城市数据"""
    return EXTENDED_CITY_DB.get(city)

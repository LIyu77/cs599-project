"""
系统测试文件
"""

import os
import sys
import json
from datetime import datetime, timedelta

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import TravelState, create_initial_state, create_travel_graph
from memory import get_memory_manager
from tools import search_flights, search_trains, search_hotels, search_restaurants
from tools import geocode, search_poi, get_weather


def test_tools():
    """测试工具函数"""
    print("🧪 测试工具函数...")

    # 测试飞猪API工具
    print("\n1. 测试飞猪API工具:")
    flights = search_flights("北京", "上海", "2024-01-15")
    print(f"   航班查询结果: {len(json.loads(flights))} 个航班")

    trains = search_trains("北京", "上海", "2024-01-15")
    print(f"   火车查询结果: {len(json.loads(trains))} 个车次")

    hotels = search_hotels("上海", "2024-01-15", "2024-01-18", 3)
    print(f"   酒店查询结果: {len(json.loads(hotels))} 家酒店")

    restaurants = search_restaurants("上海", 3)
    print(f"   餐厅查询结果: {len(json.loads(restaurants))} 家餐厅")

    # 测试高德API工具
    print("\n2. 测试高德API工具:")
    geocode_result = geocode("北京市天安门", "北京")
    print(f"   地理编码结果: {json.loads(geocode_result)['status']}")

    poi_result = search_poi("故宫", "北京", "", 3)
    print(f"   POI搜索结果: {len(json.loads(poi_result))} 个兴趣点")

    weather_result = get_weather("北京")
    print(f"   天气查询结果: {json.loads(weather_result)['status']}")

    print("✅ 工具函数测试完成")


def test_memory():
    """测试记忆模块"""
    print("\n🧪 测试记忆模块...")

    memory_manager = get_memory_manager()

    # 测试添加偏好
    print("\n1. 测试添加偏好:")
    preference = {
        "destination": "大理",
        "budget": 5000,
        "travel_style": "休闲",
        "accommodation": "民宿"
    }
    success = memory_manager.add_preference("test_user", preference)
    print(f"   添加偏好: {'成功' if success else '失败'}")

    # 测试搜索偏好
    print("\n2. 测试搜索偏好:")
    results = memory_manager.search_preferences("test_user", "大理旅行", 3)
    print(f"   搜索结果: {len(results)} 条记录")

    # 测试获取历史
    print("\n3. 测试获取历史:")
    history = memory_manager.get_user_history("test_user")
    print(f"   历史记录: {len(history)} 条")

    # 测试注入偏好
    print("\n4. 测试注入偏好:")
    pref_text = memory_manager.inject_preferences_to_prompt("test_user", "大理旅行")
    print(f"   注入文本长度: {len(pref_text)} 字符")

    # 测试统计信息
    print("\n5. 测试统计信息:")
    stats = memory_manager.get_collection_stats()
    print(f"   集合统计: {stats}")

    print("✅ 记忆模块测试完成")


def test_agents():
    """测试智能体"""
    print("\n🧪 测试智能体...")

    from agents import (
        DestinationAgent,
        TransportAgent,
        AccommodationAgent,
        BudgetAgent
    )

    # 创建测试状态
    state = create_initial_state(
        destination="大理",
        departure="北京",
        date="2024-01-15",
        days=3,
        budget=5000,
        user_id="test_user"
    )

    state_dict = state.to_dict()

    # 测试目的地Agent
    print("\n1. 测试目的地Agent:")
    destination_agent = DestinationAgent()
    try:
        result = destination_agent.run(state_dict)
        print(f"   目的地Agent: 成功")
        print(f"   结果键: {list(result.get('destination_info', {}).keys())}")
    except Exception as e:
        print(f"   目的地Agent: 失败 - {e}")

    # 测试交通Agent
    print("\n2. 测试交通Agent:")
    transport_agent = TransportAgent()
    try:
        result = transport_agent.run(state_dict)
        print(f"   交通Agent: 成功")
        print(f"   结果键: {list(result.get('transport_info', {}).keys())}")
    except Exception as e:
        print(f"   交通Agent: 失败 - {e}")

    # 测试食宿Agent
    print("\n3. 测试食宿Agent:")
    accommodation_agent = AccommodationAgent()
    try:
        result = accommodation_agent.run(state_dict)
        print(f"   食宿Agent: 成功")
        print(f"   结果键: {list(result.get('accommodation_info', {}).keys())}")
    except Exception as e:
        print(f"   食宿Agent: 失败 - {e}")

    print("✅ 智能体测试完成")


def test_graph():
    """测试工作流"""
    print("\n🧪 测试工作流...")

    # 创建初始状态
    state = create_initial_state(
        destination="大理",
        departure="北京",
        date="2024-01-15",
        days=3,
        budget=5000,
        user_id="test_user"
    )

    # 创建并运行工作流
    graph = create_travel_graph()

    print("\n1. 运行工作流:")
    try:
        result = graph.run(state)
        print(f"   工作流状态: {result.current_step}")
        print(f"   执行日志数量: {len(result.execution_log)}")
        print(f"   错误数量: {len(result.errors)}")

        # 检查结果
        print("\n2. 检查结果:")
        print(f"   目的地信息: {'有' if result.destination_info else '无'}")
        print(f"   交通信息: {'有' if result.transport_info else '无'}")
        print(f"   住宿信息: {'有' if result.accommodation_info else '无'}")
        print(f"   预算分析: {'有' if result.budget_analysis else '无'}")
        print(f"   经济型方案: {'有' if result.economic_plan else '无'}")
        print(f"   品质型方案: {'有' if result.quality_plan else '无'}")
        print(f"   高效型方案: {'有' if result.efficient_plan else '无'}")

        # 打印部分结果
        if result.budget_analysis:
            print(f"\n3. 预算分析:")
            print(f"   总费用: ¥{result.budget_analysis.get('total', 0):.0f}")
            print(f"   是否超支: {result.budget_analysis.get('is_over_budget', False)}")

        print("✅ 工作流测试完成")

    except Exception as e:
        print(f"   工作流测试失败: {e}")
        import traceback
        traceback.print_exc()


def test_full_system():
    """测试完整系统"""
    print("\n🧪 测试完整系统...")

    try:
        # 运行所有测试
        test_tools()
        test_memory()
        test_agents()
        test_graph()

        print("\n" + "="*60)
        print("🎉 所有测试完成！")
        print("="*60)

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主测试函数"""
    print("="*60)
    print("🌍 多智能体旅行规划系统 - 测试套件")
    print("="*60)

    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        if test_name == "tools":
            test_tools()
        elif test_name == "memory":
            test_memory()
        elif test_name == "agents":
            test_agents()
        elif test_name == "graph":
            test_graph()
        elif test_name == "full":
            test_full_system()
        else:
            print(f"未知测试: {test_name}")
            print("可用测试: tools, memory, agents, graph, full")
    else:
        # 默认运行完整测试
        test_full_system()


if __name__ == '__main__':
    main()

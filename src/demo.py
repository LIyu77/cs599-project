"""
演示脚本 - 展示系统功能
"""

import os
import sys
import json
from datetime import datetime, timedelta

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import create_initial_state, create_travel_graph
from memory import get_memory_manager


def demo_basic():
    """基础演示"""
    print("="*60)
    print("🌍 多智能体旅行规划系统 - 基础演示")
    print("="*60)

    # 创建初始状态
    print("\n1. 创建旅行规划任务...")
    state = create_initial_state(
        destination="大理",
        departure="北京",
        date=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        days=4,
        budget=6000,
        user_id="demo_user"
    )

    print(f"   目的地: {state.destination}")
    print(f"   出发地: {state.departure}")
    print(f"   日期: {state.date}")
    print(f"   天数: {state.days}天")
    print(f"   预算: ¥{state.budget}")

    # 运行工作流
    print("\n2. 运行工作流...")
    graph = create_travel_graph()
    result = graph.run(state)

    # 显示结果摘要
    print("\n3. 结果摘要:")
    print(f"   状态: {result.current_step}")
    print(f"   执行步骤: {len(result.execution_log)}")
    print(f"   错误数量: {len(result.errors)}")

    # 显示预算分析
    if result.budget_analysis:
        print("\n4. 预算分析:")
        expenses = result.budget_analysis.get('expenses', {})
        print(f"   交通: ¥{expenses.get('transport', 0):.0f}")
        print(f"   住宿: ¥{expenses.get('accommodation', 0):.0f}")
        print(f"   餐饮: ¥{expenses.get('dining', 0):.0f}")
        print(f"   景点: ¥{expenses.get('attractions', 0):.0f}")
        print(f"   总计: ¥{result.budget_analysis.get('total', 0):.0f}")

    # 显示方案
    print("\n5. 生成方案:")
    plans = result.get_all_plans()
    for plan_type, plan in plans.items():
        if plan:
            print(f"   {plan_type}: {plan.get('plan_name', 'N/A')} - ¥{plan.get('total_budget', 0):.0f}")

    print("\n✅ 演示完成！")
    return result


def demo_memory():
    """记忆功能演示"""
    print("\n" + "="*60)
    print("💾 记忆功能演示")
    print("="*60)

    memory_manager = get_memory_manager()

    # 模拟用户历史
    print("\n1. 添加用户历史偏好...")
    preferences = [
        {"destination": "大理", "budget": 5000, "travel_style": "休闲"},
        {"destination": "丽江", "budget": 6000, "travel_style": "摄影"},
        {"destination": "三亚", "budget": 8000, "travel_style": "度假"},
    ]

    for i, pref in enumerate(preferences, 1):
        success = memory_manager.add_preference(f"demo_user_{i}", pref)
        print(f"   用户{i}: {'成功' if success else '失败'}")

    # 检索偏好
    print("\n2. 检索用户偏好...")
    results = memory_manager.search_preferences("demo_user_1", "大理旅行", 3)
    print(f"   找到 {len(results)} 条相关记录")

    for i, result in enumerate(results, 1):
        print(f"   {i}. {result['text']}")

    # 获取统计信息
    print("\n3. 记忆库统计:")
    stats = memory_manager.get_collection_stats()
    print(f"   集合名称: {stats.get('collection_name', 'N/A')}")
    print(f"   文档数量: {stats.get('total_documents', 0)}")

    print("\n✅ 记忆功能演示完成！")


def demo_tools():
    """工具功能演示"""
    print("\n" + "="*60)
    print("🛠️ 工具功能演示")
    print("="*60)

    from tools import search_flights, search_trains, search_hotels, search_restaurants
    from tools import geocode, search_poi, get_weather

    # 演示飞猪API
    print("\n1. 飞猪API演示:")
    print("   查询北京到上海的航班...")
    flights = json.loads(search_flights("北京", "上海", "2024-01-15"))
    print(f"   找到 {len(flights)} 个航班")
    if flights:
        print(f"   最便宜: ¥{flights[0]['price']} - {flights[0]['airline']}")

    print("\n   查询北京到上海的火车...")
    trains = json.loads(search_trains("北京", "上海", "2024-01-15"))
    print(f"   找到 {len(trains)} 个车次")
    if trains:
        print(f"   最便宜: ¥{trains[0]['price']} - {trains[0]['train_no']}")

    # 演示高德API
    print("\n2. 高德API演示:")
    print("   地理编码: 北京市天安门")
    geocode_result = json.loads(geocode("北京市天安门", "北京"))
    if geocode_result.get('geocodes'):
        location = geocode_result['geocodes'][0].get('location', '')
        print(f"   坐标: {location}")

    print("\n   搜索景点: 故宫")
    pois = json.loads(search_poi("故宫", "北京", "", 3))
    print(f"   找到 {len(pois)} 个景点")
    if pois:
        print(f"   第一个: {pois[0]['name']} - 评分{pois[0]['rating']}")

    print("\n   查询天气: 北京")
    weather = json.loads(get_weather("北京"))
    if weather.get('lives'):
        print(f"   天气: {weather['lives'][0]['weather']}")
        print(f"   温度: {weather['lives'][0]['temperature']}°C")

    print("\n✅ 工具功能演示完成！")


def demo_full():
    """完整演示"""
    print("="*60)
    print("🌍 多智能体旅行规划系统 - 完整演示")
    print("="*60)

    try:
        # 运行所有演示
        demo_tools()
        demo_memory()
        result = demo_basic()

        # 保存结果
        print("\n" + "="*60)
        print("💾 保存演示结果")
        print("="*60)

        filename = f"demo_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"结果已保存到: {filename}")

        print("\n" + "="*60)
        print("🎉 完整演示结束！")
        print("="*60)

    except Exception as e:
        print(f"\n❌ 演示失败: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    if len(sys.argv) > 1:
        demo_name = sys.argv[1]
        if demo_name == "basic":
            demo_basic()
        elif demo_name == "memory":
            demo_memory()
        elif demo_name == "tools":
            demo_tools()
        elif demo_name == "full":
            demo_full()
        else:
            print(f"未知演示: {demo_name}")
            print("可用演示: basic, memory, tools, full")
    else:
        # 默认运行完整演示
        demo_full()


if __name__ == '__main__':
    main()

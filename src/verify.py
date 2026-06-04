"""
验证脚本 - 检查所有模块是否能正常导入
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def verify_imports():
    """验证所有模块导入"""
    print("[INFO] 验证模块导入...")
    try:
        from config import get_config, SystemConfig
        print("[OK] 配置模块导入成功")
        from tools import search_flights, search_trains, search_hotels, search_restaurants
        from tools import geocode, search_poi, get_weather
        print("[OK] 工具模块导入成功")
        from memory import MemoryManager
        print("[OK] 记忆模块导入成功")
        from agents import (
            BaseAgent, DestinationAgent, TransportAgent,
            AccommodationAgent, BudgetAgent,
            EconomicPlanAgent, QualityPlanAgent, EfficientPlanAgent
        )
        print("[OK] 智能体模块导入成功")
        from utils import TravelState, create_initial_state, TravelGraph, create_travel_graph
        print("[OK] 工具模块导入成功")
        print("[PASS] 所有模块导入验证通过!")
        return True
    except ImportError as e:
        print(f"[FAIL] 模块导入失败: {e}")
        return False
    except Exception as e:
        print(f"[FAIL] 验证过程出错: {e}")
        return False


def verify_config():
    """验证配置"""
    print("\n[INFO] 验证配置...")
    try:
        from config import get_config
        config = get_config()
        assert config.api.FLIGGY_API_KEY, "飞猪API密钥未配置"
        assert config.api.AMAP_API_KEY, "高德API密钥未配置"
        assert config.api.ZHIPU_API_KEY, "智谱AI API密钥未配置"
        print("[OK] API配置验证通过")
        assert config.model.ZHIPU_MODEL, "智谱AI模型未配置"
        print("[OK] 模型配置验证通过")
        assert config.travel.DEFAULT_BUDGET_MIN > 0, "默认最小预算无效"
        print("[OK] 旅行配置验证通过")
        print("[PASS] 配置验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 配置验证失败: {e}")
        return False


def verify_tools():
    """验证工具函数"""
    print("\n[INFO] 验证工具函数...")
    try:
        from tools import search_flights, search_trains, search_hotels, search_restaurants
        from tools import geocode, search_poi, get_weather
        import json

        flights = search_flights("北京", "上海", "2024-01-15")
        flights_data = json.loads(flights)
        assert isinstance(flights_data, list) and len(flights_data) > 0
        print("[OK] 航班查询工具验证通过")

        trains = search_trains("北京", "上海", "2024-01-15")
        trains_data = json.loads(trains)
        assert isinstance(trains_data, list) and len(trains_data) > 0
        print("[OK] 火车查询工具验证通过")

        hotels = search_hotels("上海", "2024-01-15", "2024-01-18", 3)
        hotels_data = json.loads(hotels)
        assert isinstance(hotels_data, list) and len(hotels_data) > 0
        print("[OK] 酒店查询工具验证通过")

        restaurants = search_restaurants("上海", 3)
        restaurants_data = json.loads(restaurants)
        assert isinstance(restaurants_data, list) and len(restaurants_data) > 0
        print("[OK] 餐厅查询工具验证通过")

        geocode_result = geocode("北京市天安门", "北京")
        geocode_data = json.loads(geocode_result)
        assert geocode_data.get('status') == '1'
        print("[OK] 地理编码工具验证通过")

        poi_result = search_poi("故宫", "北京", "", 3)
        poi_data = json.loads(poi_result)
        assert isinstance(poi_data, list) and len(poi_data) > 0
        print("[OK] POI搜索工具验证通过")

        weather_result = get_weather("北京")
        weather_data = json.loads(weather_result)
        assert weather_data.get('status') == '1'
        print("[OK] 天气查询工具验证通过")

        print("[PASS] 工具函数验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 工具函数验证失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_agents():
    """验证智能体"""
    print("\n[INFO] 验证智能体...")
    try:
        from agents import (
            DestinationAgent, TransportAgent, AccommodationAgent,
            BudgetAgent, EconomicPlanAgent, QualityPlanAgent, EfficientPlanAgent
        )

        for AgentClass, expected_name in [
            (DestinationAgent, "目的地查询Agent"),
            (TransportAgent, "交通规划Agent"),
            (AccommodationAgent, "食宿筛选Agent"),
            (BudgetAgent, "预算核算Agent"),
            (EconomicPlanAgent, "经济型方案Agent"),
            (QualityPlanAgent, "品质型方案Agent"),
            (EfficientPlanAgent, "高效型方案Agent"),
        ]:
            agent = AgentClass()
            assert agent.name == expected_name, f"{expected_name}名称错误: {agent.name}"
            print(f"[OK] {expected_name} 验证通过")

        print("[PASS] 智能体验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 智能体验证失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_state():
    """验证状态管理"""
    print("\n[INFO] 验证状态管理...")
    try:
        from utils import TravelState, create_initial_state

        state = create_initial_state(
            destination="大理", departure="北京",
            date="2024-01-15", days=3, budget=5000, user_id="test_user"
        )
        assert state.destination == "大理"
        assert state.departure == "北京"
        assert state.days == 3
        assert state.budget == 5000
        print("[OK] 初始状态创建验证通过")

        state_dict = state.to_dict()
        assert isinstance(state_dict, dict) and state_dict['destination'] == "大理"
        print("[OK] 状态转换验证通过")

        state.update_step("test", "测试步骤")
        assert state.current_step == "test" and len(state.execution_log) > 0
        print("[OK] 状态更新验证通过")

        print("[PASS] 状态管理验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 状态管理验证失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_memory():
    """验证记忆模块"""
    print("\n[INFO] 验证记忆模块...")
    try:
        from memory import MemoryManager
        memory_manager = MemoryManager()
        print("[OK] 记忆管理器创建成功")

        stats = memory_manager.get_collection_stats()
        assert 'collection_name' in stats and 'total_documents' in stats
        print("[OK] 集合统计验证通过")

        print("[PASS] 记忆模块验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 记忆模块验证失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_graph():
    """验证工作流图"""
    print("\n[INFO] 验证工作流图...")
    try:
        from utils import TravelGraph, create_travel_graph
        graph = create_travel_graph()
        assert graph is not None
        for attr in ['destination_agent', 'transport_agent', 'accommodation_agent',
                      'budget_agent', 'economic_agent', 'quality_agent', 'efficient_agent']:
            assert hasattr(graph, attr), f"缺少{attr}"
        print("[OK] 工作流图创建验证通过")
        print("[PASS] 工作流图验证通过!")
        return True
    except Exception as e:
        print(f"[FAIL] 工作流图验证失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_verifications():
    """运行所有验证"""
    print("=" * 60)
    print(" 多智能体旅行规划系统 - 系统验证")
    print("=" * 60)

    checks = [
        ("模块导入", verify_imports),
        ("配置验证", verify_config),
        ("工具函数", verify_tools),
        ("智能体", verify_agents),
        ("状态管理", verify_state),
        ("记忆模块", verify_memory),
        ("工作流图", verify_graph),
    ]

    results = []
    for name, func in checks:
        results.append((name, func()))

    print("\n" + "=" * 60)
    print(" 验证总结")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    failed = sum(1 for _, r in results if not r)

    for name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"  {name}: {status}")

    print(f"\n总计: {len(results)} 项 | 通过: {passed} 项 | 失败: {failed} 项")

    if failed == 0:
        print("\n 所有验证通过! 系统准备就绪。")
        return True
    else:
        print(f"\n 有 {failed} 项验证失败，请检查相关模块。")
        return False


def main():
    if len(sys.argv) > 1:
        verify_name = sys.argv[1]
        dispatch = {
            "imports": verify_imports, "config": verify_config,
            "tools": verify_tools, "agents": verify_agents,
            "state": verify_state, "memory": verify_memory,
            "graph": verify_graph, "all": run_all_verifications,
        }
        if verify_name in dispatch:
            dispatch[verify_name]()
        else:
            print(f"未知验证: {verify_name}")
            print(f"可用验证: {', '.join(dispatch.keys())}")
    else:
        run_all_verifications()


if __name__ == '__main__':
    main()

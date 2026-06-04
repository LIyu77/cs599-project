"""
主程序 - 多智能体旅行规划系统
"""

import os
import sys
import json
import argparse
from typing import Dict, Any
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import TravelState, create_initial_state, create_travel_graph
from memory import get_memory_manager


def print_banner():
    """打印系统横幅"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║              🌍 多智能体旅行规划系统 🌍                      ║
║                                                              ║
║  基于LangGraph的智能旅行方案生成系统                          ║
║  支持经济型、品质型、高效型三种方案                            ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_plan(plan: Dict[str, Any], plan_type: str):
    """
    打印方案详情

    Args:
        plan: 方案数据
        plan_type: 方案类型
    """
    if not plan:
        print(f"\n[FAIL] {plan_type}方案生成失败")
        return

    print(f"\n{'='*60}")
    print(f"[PLAN] {plan.get('plan_name', plan_type + '方案')}")
    print(f"{'='*60}")
    print(f"类型: {plan.get('plan_type', plan_type)}")
    print(f"预算: ¥{plan.get('total_budget', 0):.0f}")

    # 交通方案
    transport = plan.get('transport', {})
    if transport:
        choice = transport.get('choice', {})
        print(f"\n[TRANSPORT] 交通方案:")
        if choice:
            print(f"   - {choice.get('train_no', choice.get('flight_no', 'N/A'))}")
            print(f"   - {choice.get('departure', '')} -> {choice.get('destination', '')}")
            print(f"   - 时长: {choice.get('duration', 'N/A')}")
            print(f"   - 价格: ¥{choice.get('price', 0)}")
        print(f"   理由: {transport.get('reason', '')}")

    # 住宿方案
    accommodation = plan.get('accommodation', {})
    if accommodation:
        choice = accommodation.get('choice', {})
        print(f"\n[HOTEL] 住宿方案:")
        if choice:
            print(f"   - {choice.get('name', 'N/A')}")
            print(f"   - 类型: {choice.get('type', 'N/A')}")
            print(f"   - 评分: {choice.get('rating', 'N/A')}")
            print(f"   - 价格: ¥{choice.get('price_per_night', 0)}/晚")
        print(f"   理由: {accommodation.get('reason', '')}")

    # 餐厅推荐
    dining = plan.get('dining', {})
    if dining:
        choices = dining.get('choices', [])
        print(f"\n[FOOD] 餐厅推荐:")
        for i, restaurant in enumerate(choices, 1):
            print(f"   {i}. {restaurant.get('name', 'N/A')}")
            print(f"      - 菜系: {restaurant.get('cuisine', 'N/A')}")
            print(f"      - 人均: ¥{restaurant.get('avg_price', 0)}")
            print(f"      - 评分: {restaurant.get('rating', 'N/A')}")
        print(f"   理由: {dining.get('reason', '')}")

    # 景点推荐
    attractions = plan.get('attractions', {})
    if attractions:
        choices = attractions.get('choices', [])
        print(f"\n[ATTRACTION] 景点推荐:")
        for i, attraction in enumerate(choices, 1):
            print(f"   {i}. {attraction.get('name', 'N/A')}")
            print(f"      - 类型: {attraction.get('type', 'N/A')}")
            print(f"      - 评分: {attraction.get('rating', 'N/A')}")
            print(f"      - 门票: ¥{attraction.get('price', 0)}")
        print(f"   理由: {attractions.get('reason', '')}")

    # 行程安排
    itinerary = plan.get('itinerary', [])
    if itinerary:
        print(f"\n[ITINERARY] 行程安排:")
        for day in itinerary:
            print(f"\n   {day.get('date', f"第{day.get('day', 0)}天")}:")
            for activity in day.get('activities', []):
                print(f"   {activity.get('time', '')}: {activity.get('activity', '')}")
                if activity.get('location'):
                    print(f"      地点: {activity.get('location', '')}")

    # 特色亮点
    if 'highlights' in plan:
        print(f"\n[HIGHLIGHT] 方案亮点:")
        for highlight in plan['highlights']:
            print(f"   • {highlight}")

    # 省钱贴士
    if 'tips' in plan:
        print(f"\n[TIP] 省钱贴士:")
        for tip in plan['tips']:
            print(f"   • {tip}")

    # 时间节省技巧
    if 'time_saving_tips' in plan:
        print(f"\n⏰ 时间节省技巧:")
        for tip in plan['time_saving_tips']:
            print(f"   • {tip}")

    print(f"\n{'='*60}")


def print_budget_analysis(budget_analysis: Dict[str, Any]):
    """
    打印预算分析

    Args:
        budget_analysis: 预算分析数据
    """
    if not budget_analysis:
        return

    print(f"\n{'='*60}")
    print(f"[BUDGET] 预算分析")
    print(f"{'='*60}")

    expenses = budget_analysis.get('expenses', {})
    if expenses:
        print(f"费用明细:")
        print(f"   - 交通: ¥{expenses.get('transport', 0):.0f}")
        print(f"   - 住宿: ¥{expenses.get('accommodation', 0):.0f}")
        print(f"   - 餐饮: ¥{expenses.get('dining', 0):.0f}")
        print(f"   - 景点: ¥{expenses.get('attractions', 0):.0f}")
        print(f"   - 其他: ¥{expenses.get('others', 0):.0f}")

    total = budget_analysis.get('total', 0)
    budget = budget_analysis.get('budget', 0)
    is_over = budget_analysis.get('is_over_budget', False)

    print(f"\n总费用: ¥{total:.0f}")
    print(f"用户预算: ¥{budget:.0f}")

    if is_over:
        over_amount = budget_analysis.get('over_amount', 0)
        print(f"[WARNING] 超出预算: ¥{over_amount:.0f}")
    else:
        print(f"[OK] 在预算内，剩余: ¥{budget - total:.0f}")

    suggestions = budget_analysis.get('suggestions', [])
    if suggestions:
        print(f"\n💡 建议:")
        for suggestion in suggestions:
            print(f"   • {suggestion}")

    print(f"{'='*60}")


def run_interactive():
    """交互式运行"""
    print_banner()

    # 获取用户输入
    print("\n请输入旅行信息：")
    destination = input("目的地（如：大理）: ").strip()
    if not destination:
        destination = "大理"

    departure = input("出发地（如：北京，直接回车使用默认）: ").strip()
    if not departure:
        departure = "北京"

    date = input("出发日期（YYYY-MM-DD，直接回车使用明天）: ").strip()
    if not date:
        from datetime import datetime, timedelta
        tomorrow = datetime.now() + timedelta(days=1)
        date = tomorrow.strftime("%Y-%m-%d")

    days_str = input("旅行天数（直接回车使用3天）: ").strip()
    days = int(days_str) if days_str.isdigit() else 3

    budget_str = input("预算（元，直接回车使用5000元）: ").strip()
    budget = float(budget_str) if budget_str.replace('.', '').isdigit() else 5000

    user_id = input("用户ID（直接回车使用默认）: ").strip()
    if not user_id:
        user_id = "default_user"

    print(f"\n[START] 开始规划旅行: {departure} -> {destination}")
    print(f"[INFO] 日期: {date}, 天数: {days}天, 预算: ¥{budget}")

    # 创建初始状态
    state = create_initial_state(
        destination=destination,
        departure=departure,
        date=date,
        days=days,
        budget=budget,
        user_id=user_id
    )

    # 创建并运行工作流
    graph = create_travel_graph()

    print("\n⏳ 正在规划中，请稍候...")
    result = graph.run(state)

    # 打印结果
    print(f"\n[DONE] 规划完成！")
    print(f"执行日志:")
    for log in result.execution_log[-5:]:  # 显示最后5条日志
        print(f"   {log}")

    # 打印预算分析
    print_budget_analysis(result.budget_analysis)

    # 打印三套方案
    print("\n" + "="*60)
    print("📊 三套旅行方案")
    print("="*60)

    print_plan(result.economic_plan, "经济型")
    print_plan(result.quality_plan, "品质型")
    print_plan(result.efficient_plan, "高效型")

    # 保存结果
    save_result = input("\n是否保存结果到文件？(y/n): ").strip().lower()
    if save_result == 'y':
        filename = f"travel_plan_{destination}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"[OK] 结果已保存到: {filename}")


def run_api_server():
    """运行API服务器"""
    from flask import Flask, request, jsonify, send_from_directory
    import os

    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)

    @app.route('/')
    def index():
        """前端页面"""
        return send_from_directory(template_dir, 'index.html')

    @app.route('/api/plan', methods=['POST'])
    def create_plan():
        """创建旅行规划"""
        try:
            data = request.json

            # 提取参数
            destination = data.get('destination', '')
            departure = data.get('departure', '北京')
            date = data.get('date', '')
            days = data.get('days', 3)
            budget = data.get('budget', 5000)
            user_id = data.get('user_id', 'default_user')

            if not destination:
                return jsonify({'error': '请提供目的地'}), 400

            # 创建初始状态
            state = create_initial_state(
                destination=destination,
                departure=departure,
                date=date,
                days=days,
                budget=budget,
                user_id=user_id
            )

            # 运行工作流
            graph = create_travel_graph()
            result = graph.run(state)

            # 返回结果
            return jsonify({
                'success': True,
                'data': result.to_dict()
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/memory/<user_id>', methods=['GET'])
    def get_user_memory(user_id: str):
        """获取用户记忆"""
        try:
            memory_manager = get_memory_manager()
            history = memory_manager.get_user_history(user_id)

            return jsonify({
                'success': True,
                'data': history
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/memory/<user_id>', methods=['DELETE'])
    def clear_user_memory(user_id: str):
        """清除用户记忆"""
        try:
            memory_manager = get_memory_manager()
            success = memory_manager.clear_user_data(user_id)

            return jsonify({
                'success': success,
                'message': '用户记忆已清除' if success else '清除失败'
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/health', methods=['GET'])
    def health_check():
        """健康检查"""
        return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

    # 启动服务器
    print("[START] 启动API服务器...")
    print("[API] API端点: http://localhost:5000")
    print("[INFO] 可用接口:")
    print("   - POST /api/plan - 创建旅行规划")
    print("   - GET /api/memory/<user_id> - 获取用户记忆")
    print("   - DELETE /api/memory/<user_id> - 清除用户记忆")
    print("   - GET /api/health - 健康检查")

    app.run(host='0.0.0.0', port=5000, debug=True)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='多智能体旅行规划系统')
    parser.add_argument('--mode', choices=['interactive', 'api'], default='interactive',
                       help='运行模式: interactive(交互式) 或 api(API服务器)')

    args = parser.parse_args()

    if args.mode == 'interactive':
        run_interactive()
    elif args.mode == 'api':
        run_api_server()


if __name__ == '__main__':
    main()

# CS599 多智能体旅行规划系统

## 项目简介
基于 LangGraph 的智能旅行方案生成系统，支持经济型、品质型、高效型三种方案。

## 方向
方向一：Agentic AI 原生开发

## 技术栈
- AI IDE: Claude Code
- LLM: 智谱AI
- 框架：LangGraph
- 向量数据库：ChromaDB
- 容器：Docker
- Web框架：Flask
- Embedding模型：智谱AI Embedding-2
- 编程语言：Python 3.13

## 目录结构
```
src/
├── agents/                    # 智能体模块
│   ├── base_agent.py         # 智能体基类
│   ├── destination_agent.py  # 目的地查询Agent
│   ├── transport_agent.py    # 交通规划Agent
│   ├── accommodation_agent.py # 食宿筛选Agent
│   ├── budget_agent.py       # 预算核算Agent
│   ├── economic_plan_agent.py # 经济型方案Agent
│   ├── quality_plan_agent.py # 品质型方案Agent
│   └── efficient_plan_agent.py # 高效型方案Agent
├── memory/                    # 记忆模块
│   └── memory_manager.py     # Chroma向量数据库 + 智谱AI Embedding
├── tools/                     # 工具函数层
│   ├── fliggy_tools.py       # 飞猪API工具
│   └── amap_tools.py         # 高德地图API工具
├── utils/                     # 工具模块
│   ├── state.py              # 状态定义
│   └── graph.py              # LangGraph图定义
├── templates/                 # 前端模板
│   └── index.html            # Web前端
├── config.py                  # 配置文件
├── main.py                    # 主程序
├── requirements.txt           # 依赖列表
└── README.md                  # 项目说明
```

## 环境搭建
1. 依赖安装
```bash
pip install -r requirements.txt
```

2. 环境变量配置
```bash
export FLIGGY_API_KEY="your_fliggy_api_key"
export AMAP_API_KEY="your_amap_api_key"
export ZHIPU_API_KEY="your_zhipu_api_key"
```

3. 启动步骤
```bash
# 交互式模式
python main.py --mode interactive

# API服务器模式
python main.py --mode api
```

## 项目状态
- [x] Proposal
- [x] MVP
- [x] Final

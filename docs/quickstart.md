# 快速开始指南

## 安装

1. 复制 skill 到 OpenClaw skills 目录
2. 确保 Python 3.12+ 可用
3. 无需额外依赖（使用标准库）

## 使用方式

### 方式一：自然语言（推荐）

直接在 Discord 输入：

```
创建一个 AA 结算助手项目
```

```
查看 aa-settlement 状态
```

```
给 aa-settlement 添加导出功能
```

### 方式二：命令行

```bash
# 创建项目
python scripts/project_manager.py create aa-settlement "AA结算助手"

# 查看状态
python scripts/project_manager.py status aa-settlement

# 标记任务完成（Agent 调用）
python scripts/orchestrator.py done aa-settlement aa-settlement-prd "PRD已完成"
```

## 文件结构

```
multi-agent-dev-team/
├── SKILL.md                 # 技能说明
├── config/
│   └── agents.yaml         # Agent 配置
├── scripts/
│   ├── orchestrator.py     # 核心编排器
│   └── project_manager.py  # 项目经理助手
├── templates/
│   └── prompts/            # 各角色系统提示词
│       ├── director.txt
│       ├── pm.txt
│       ├── designer.txt
│       ├── backend.txt
│       ├── frontend.txt
│       └── qa.txt
└── docs/
    └── examples.md         # 使用示例
```

## 工作流说明

### 完整流程（有设计）

```
用户需求
    ↓
项目总监创建项目
    ↓
产品经理写 PRD ────────────→ #project-pm 线程
    ↓
设计师出设计稿 ────────────→ #project-design 线程
    ↓
前后端并行开发 ─┬──────────→ #project-backend 线程
                └──────────→ #project-frontend 线程
    ↓
测试验收 ──────────────────→ #project-qa 线程
    ↓
项目总监汇总汇报（主线程）
```

### 精简流程（无设计）

```
用户需求
    ↓
项目总监创建项目（--skip-design）
    ↓
产品经理写 PRD
    ↓
前后端并行开发
    ↓
测试验收
    ↓
项目总监汇总汇报
```

## 线程命名规则

- 主项目：#{project-name}
- 产品经理：#{project-name}-pm
- 设计师：#{project-name}-design
- 后端开发：#{project-name}-backend
- 前端开发：#{project-name}-frontend
- 测试：#{project-name}-qa
- 独立任务：#{project-name}-{task-id}

## 注意事项

1. 项目数据保存在 /workspace/projects/{name}/
2. 每个角色在自己的线程工作，互不干扰
3. 项目总监始终在主线程汇报
4. 任务完成后 Agent 需主动通知项目总监

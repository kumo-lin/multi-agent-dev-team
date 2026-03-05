# 多 Agent 开发团队 Skill 安装指南

## 安装前检查

### 1. 现有架构冲突检查

✅ **无冲突发现**：
- 现有 agents：post-agent, reflection-agent, script-agent（功能不重叠）
- 无 cron 任务（无调度冲突）
- 目录结构独立（互不干扰）

### 2. 新增 Agent 清单

| Agent | 角色 | 模型 | 用途 |
|-------|------|------|------|
| director | 项目总监 | kimi/kimi-k2.5 | 总协调 |
| pm | 产品经理 | kimi/kimi-k2.5 | PRD、需求 |
| designer | 设计师 | kimi/kimi-k2.5 | UI/UX |
| backend | 后端 | deepseek/deepseek-v3.2 | API、数据库 |
| frontend | 前端 | deepseek/deepseek-v3.2 | 页面实现 |
| qa | 测试 | deepseek/deepseek-v3.2 | 验收 |

## 安装步骤

### 步骤 1：Skill 已就绪

Skill 已位于：
```
~/.openclaw/workspace/skills/multi-agent-dev-team/
```

### 步骤 2：创建工作目录

```bash
mkdir -p ~/.openclaw/workspace/projects
mkdir -p ~/.openclaw/workspace/.orchestrator
```

### 步骤 3：配置环境变量（可选）

添加到 `~/.openclaw/config.yaml`：

```yaml
skills:
  multi_agent_dev_team:
    enabled: true
    config_path: ~/.openclaw/workspace/skills/multi-agent-dev-team/config/skill.yaml
```

### 步骤 4：验证安装

```bash
# 测试编排器
python3 ~/.openclaw/workspace/skills/multi-agent-dev-team/scripts/orchestrator.py --help

# 测试频道绑定
python3 ~/.openclaw/workspace/skills/multi-agent-dev-team/scripts/channel_binding.py list
```

## 使用方式

### 启动项目

在任意 Discord 频道输入：
```
@openclaw 创建一个 AA 结算助手
```

该频道即成为项目绑定频道。

### 项目沟通

所有项目相关询问必须在创建该项目的频道进行：
- ✅ `#aa-settlement` 频道：查看状态 / 添加功能 / 讨论需求
- ❌ 其他频道：提示"请回到 #aa-settlement 频道"

### 查看所有绑定

```bash
python3 ~/.openclaw/workspace/skills/multi-agent-dev-team/scripts/channel_binding.py list
```

## 目录结构

```
~/.openclaw/workspace/
├── skills/multi-agent-dev-team/     # Skill 代码
│   ├── SKILL.md
│   ├── config/
│   │   ├── agents.yaml              # 旧配置（保留兼容）
│   │   └── skill.yaml               # 主配置
│   ├── scripts/
│   │   ├── orchestrator.py          # 核心编排
│   │   ├── project_manager.py       # 项目经理
│   │   └── channel_binding.py       # 频道绑定
│   ├── templates/prompts/           # 各角色提示词
│   └── docs/
│
├── projects/                         # 项目存储（运行时创建）
│   └── {project-name}/
│       ├── config.json
│       ├── prd.md
│       ├── design/
│       ├── tasks/
│       └── results/
│
└── .orchestrator/                    # 编排器数据
    └── channel_projects.json         # 频道-项目映射
```

## 模型配置

在 `config/skill.yaml` 中已配置：

```yaml
agents:
  director: { model: kimi/kimi-k2.5 }
  pm: { model: kimi/kimi-k2.5 }
  designer: { model: kimi/kimi-k2.5 }
  backend: { model: deepseek/deepseek-v3.2 }
  frontend: { model: deepseek/deepseek-v3.2 }
  qa: { model: deepseek/deepseek-v3.2 }
```

## 故障排查

### Agent 无响应

1. 检查 subagent 状态：
```bash
openclaw subagents list
```

2. 检查项目状态：
```bash
python3 scripts/orchestrator.py status {project}
```

### 频道绑定失效

1. 检查绑定映射：
```bash
python3 scripts/channel_binding.py list
```

2. 重新绑定（如需要）：
```bash
python3 scripts/channel_binding.py bind {project} {channel} {channel_id}
```

## 与现有系统的关系

```
┌─────────────────────────────────────────┐
│           主 Agent（你对话的对象）         │
│         当前 model: kimi/kimi-k2.5       │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┴──────────┐
    │                     │
    ▼                     ▼
┌─────────┐         ┌──────────┐
│现有系统  │         │新 Skill  │
├─────────┤         ├──────────┤
│post     │         │director  │
│reflection│        │pm        │
│script   │         │designer  │
│         │         │backend   │
│         │         │frontend  │
│         │         │qa        │
└─────────┘         └──────────┘
```

## 升级路径

1. **立即生效**：Skill 文件已就绪，立即可用
2. **渐进迁移**：新项目用新 Skill，旧项目保持现有流程
3. **完全切换**：所有新项目统一使用多 Agent 模式

## 注意事项

1. 项目创建后频道绑定不可更改
2. 主 Agent 始终保持在原频道与用户对话
3. Worker Agent 通过独立线程汇报
4. 项目数据持久化在 workspace/projects/

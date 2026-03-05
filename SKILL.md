---
name: multi-agent-dev-team
description: 6角色AI开发团队（项目总监/产品经理/设计师/后端/前端/测试），消息驱动自动工作流，无需Cron定时触发。
---

# Multi-Agent Development Team

一个完整的6角色AI开发团队架构，实现从需求到验收的全自动工作流。

## 核心特性

- **6角色分工**：项目总监、产品经理、设计师、后端开发、前端开发、测试
- **模型分工**：产品/设计角色用 Kimi 2.5，开发/测试角色用 DeepSeek v3.2
- **自动工作流**：消息驱动，无需Cron定时触发
- **频道隔离**：支持多项目并行，每个项目独立频道
- **关键节点通知**：只在阻塞/完成/需决策时打扰用户

## 快速开始

### 1. 安装 Skill

```bash
# 通过 ClawHub 安装
clawhub install multi-agent-dev-team

# 或手动安装
git clone https://github.com/your-repo/multi-agent-dev-team.git
cp -r multi-agent-dev-team ~/.openclaw/workspace/skills/
```

### 2. 配置 OpenClaw

编辑 `~/.openclaw/openclaw.json`，添加以下配置：

```json
{
  "agents": {
    "defaults": {
      "model": "kimi/kimi-k2.5",
      "memorySearch": {
        "enabled": true,
        "provider": "local",
        "fallback": "none",
        "sync": {
          "onSessionStart": true,
          "onSearch": true,
          "watch": true
        }
      },
      "heartbeat": {
        "every": "2m",
        "target": "none",
        "model": "kimi/kimi-k2.5"
      },
      "maxConcurrent": 3,
      "subagents": {
        "maxConcurrent": 8,
        "maxSpawnDepth": 2,
        "maxChildrenPerAgent": 8,
        "runTimeoutSeconds": 1200
      }
    },
    "list": [
      {
        "id": "main",
        "model": {
          "primary": "kimi/kimi-k2.5",
          "fallbacks": ["deepseek/deepseek-chat"]
        },
        "subagents": {
          "allowAgents": ["pm-lead", "pm-product", "designer-lead", "backend-lead", "frontend-lead", "qa-lead"]
        }
      },
      {
        "id": "pm-lead",
        "name": "项目总监",
        "workspace": "/home/node/.openclaw/workspace/agents/pm-lead",
        "agentDir": "/home/node/.openclaw/agents/pm-lead/agent",
        "model": {
          "primary": "kimi/kimi-k2.5",
          "fallbacks": ["deepseek/deepseek-chat"]
        },
        "subagents": {
          "allowAgents": ["pm-product", "designer-lead", "backend-lead", "frontend-lead", "qa-lead"]
        }
      },
      {
        "id": "pm-product",
        "name": "产品经理",
        "workspace": "/home/node/.openclaw/workspace/agents/pm-product",
        "agentDir": "/home/node/.openclaw/agents/pm-product/agent",
        "model": {
          "primary": "kimi/kimi-k2.5",
          "fallbacks": ["deepseek/deepseek-chat"]
        },
        "subagents": {
          "allowAgents": ["designer-lead", "backend-lead", "frontend-lead", "qa-lead"]
        }
      },
      {
        "id": "designer-lead",
        "name": "设计师",
        "workspace": "/home/node/.openclaw/workspace/agents/designer-lead",
        "agentDir": "/home/node/.openclaw/agents/designer-lead/agent",
        "model": {
          "primary": "kimi/kimi-k2.5",
          "fallbacks": ["deepseek/deepseek-chat"]
        },
        "subagents": {
          "allowAgents": ["backend-lead", "frontend-lead", "qa-lead"]
        }
      },
      {
        "id": "backend-lead",
        "name": "后端开发",
        "workspace": "/home/node/.openclaw/workspace/agents/backend-lead",
        "agentDir": "/home/node/.openclaw/agents/backend-lead/agent",
        "model": {
          "primary": "deepseek/deepseek-chat",
          "fallbacks": ["kimi/kimi-k2.5"]
        },
        "subagents": {
          "allowAgents": ["frontend-lead", "qa-lead"]
        }
      },
      {
        "id": "frontend-lead",
        "name": "前端开发",
        "workspace": "/home/node/.openclaw/workspace/agents/frontend-lead",
        "agentDir": "/home/node/.openclaw/agents/frontend-lead/agent",
        "model": {
          "primary": "deepseek/deepseek-chat",
          "fallbacks": ["kimi/kimi-k2.5"]
        },
        "subagents": {
          "allowAgents": ["qa-lead"]
        }
      },
      {
        "id": "qa-lead",
        "name": "测试",
        "workspace": "/home/node/.openclaw/workspace/agents/qa-lead",
        "agentDir": "/home/node/.openclaw/agents/qa-lead/agent",
        "model": {
          "primary": "deepseek/deepseek-chat",
          "fallbacks": ["kimi/kimi-k2.5"]
        },
        "subagents": {
          "allowAgents": []
        }
      }
    ]
  }
}
```

### 3. 配置模型提供商

确保已配置 Kimi 和 DeepSeek 模型：

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek": {
        "baseUrl": "https://api.deepseek.com/v1",
        "apiKey": "YOUR_DEEPSEEK_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "deepseek-chat",
            "name": "DeepSeek v3.2",
            "reasoning": false,
            "input": ["text"],
            "contextWindow": 128000,
            "maxTokens": 8192
          }
        ]
      },
      "kimi": {
        "baseUrl": "https://api.moonshot.cn/v1",
        "apiKey": "YOUR_KIMI_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "kimi-k2.5",
            "name": "Kimi 2.5",
            "reasoning": false,
            "input": ["text", "image"],
            "contextWindow": 131072,
            "maxTokens": 65536
          }
        ]
      }
    }
  }
}
```

### 4. 重启 OpenClaw

```bash
openclaw gateway restart
```

## 工作流程

### 启动开发任务

```
用户：开发 [项目名] 的 [功能描述]
    ↓
main 接收 → spawn pm-lead
    ↓
pm-lead 拆解任务 → spawn pm-product
    ↓
pm-product 输出 PRD → spawn designer-lead
    ↓
designer-lead 输出设计 → 并行 spawn:
    ├── backend-lead
    └── frontend-lead
    ↓
两者都完成后 → spawn qa-lead
    ↓
qa-lead 验收完成 → 通知 pm-lead → 通知用户验收
```

### 关键节点通知

| 节点 | 通知内容 | 通知方式 |
|------|----------|----------|
| 任务开始 | "已开始开发 [功能]" | 用户 |
| 阻塞 | "遇到问题：[问题描述]，需要决策" | 用户 |
| 完成 | "[功能] 开发完成，请验收" | 用户 |

## 角色职责

### 项目总监 (pm-lead)
- 进度把控、资源协调
- 质量把关、决策升级
- 验收后通知用户

### 产品经理 (pm-product)
- 需求分析、PRD撰写
- 优先级排序、方案设计
- 使用 product-manager-toolkit skill

### 设计师 (designer-lead)
- UI/UX设计、原型输出
- 设计规范制定
- 参考 Web Development skill

### 后端开发 (backend-lead)
- API设计、数据库设计
- 业务逻辑实现
- Python/FastAPI 优先

### 前端开发 (frontend-lead)
- 页面实现、交互开发
- API对接、性能优化
- HTML/CSS/JavaScript + React/Vue

### 测试 (qa-lead)
- 测试用例编写
- 验收测试执行
- 缺陷跟踪、质量报告

## 文件结构

```
~/.openclaw/workspace/
├── agents/
│   ├── pm-lead/PROMPT.md
│   ├── pm-product/PROMPT.md
│   ├── designer-lead/PROMPT.md
│   ├── backend-lead/PROMPT.md
│   ├── frontend-lead/PROMPT.md
│   └── qa-lead/PROMPT.md
├── TEAM_WORKFLOW.md
├── PROJECT_ISOLATION.md
└── pipeline/state/ (任务状态文件)
```

## 依赖技能

建议同时安装：
- `product-manager-toolkit` - 产品经理工具包
- `web` - Web开发技能（包含设计参考）

## 配置示例

### 频道隔离配置

创建 `PROJECT_ISOLATION.md`：

```markdown
# 项目频道隔离配置

## 规则
1. 每个项目绑定一个 Discord 频道
2. 在某频道下达的指令，只处理该频道对应的项目
3. 跨频道询问时，引导用户回到对应频道

## 示例
- 在 #project-a 中：「开发登录功能」→ 执行
- 在 #general 中：「project-a进度如何？」→ 回复「请回到 #project-a 查看」
```

### 工作流文档

创建 `TEAM_WORKFLOW.md`：

```markdown
# 6角色自动工作流

## 触发方式
无需 Cron，消息驱动自动执行。

## 你的操作
1. 下达任务描述
2. 确认验收

中间过程全自动推进，只在关键节点打扰。
```

## 故障排除

### 常见问题

1. **Agent 不启动**
   - 检查模型 API 密钥配置
   - 检查 agent 配置中的 workspace 路径

2. **通知不发送**
   - 检查 Discord 频道配置
   - 确认 agent 有 message 工具权限

3. **工作流卡住**
   - 检查各 agent 的 Prompt 文件
   - 确认 spawn 权限配置正确

### 调试建议

```bash
# 检查 agent 状态
openclaw agents list

# 检查会话状态
openclaw sessions list

# 查看日志
tail -f ~/.openclaw/logs/openclaw.log
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request。

## 更新日志

### v1.0.0 (2026-03-05)
- 初始版本：6角色开发团队架构
- 消息驱动自动工作流
- 频道隔离支持

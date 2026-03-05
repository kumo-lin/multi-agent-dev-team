# TEAM_WORKFLOW.md - 6角色自动工作流

## 触发方式
**无需 Cron**，消息驱动自动执行。

## 完整工作流

```
用户下达任务
    ↓
main 接收并确认
    ↓
spawn pm-lead
    ↓
pm-lead 拆解任务
    ↓
spawn pm-product
    ↓
pm-product 输出 PRD
    ↓
spawn designer-lead
    ↓
designer-lead 输出设计
    ↓
并行 spawn:
    ├── backend-lead
    └── frontend-lead
    ↓
两者都完成后
    ↓
spawn qa-lead
    ↓
qa-lead 验收完成
    ↓
通知 pm-lead → 通知用户验收
```

## 通知链路（闭环）

| 阶段 | 执行者 | 完成后通知 | 说明 |
|------|--------|-----------|------|
| 需求分析 | pm-product | designer-lead | 输出PRD后启动设计 |
| 设计 | designer-lead | backend-lead + frontend-lead（并行） | 设计完成后并行启动前后端开发 |
| 后端开发 | backend-lead | qa-lead（等待前端） | 后端完成后等待前端，一起进入测试 |
| 前端开发 | frontend-lead | qa-lead（等待后端） | 前端完成后等待后端，一起进入测试 |
| 测试 | **qa-lead** | **pm-lead** | **关键闭环：测试必须通知项目总监** |
| 汇总 | **pm-lead** | **用户** | **关键闭环：项目总监必须通知用户验收** |

## 闭环保障机制

### QA → PM Lead 通知（必须）
```
qa-lead 验收完成后:
  方式1: sessions_send(sessionKey=pm-lead-session, message="QA完成，结果：...")
  方式2: 写状态文件到 pipeline/state/，pm-lead 轮询读取
  方式3: 若无法联系 pm-lead，直接 message 用户
```

### PM Lead → User 通知（必须）
```
pm-lead 收到 QA 完成通知后:
  - 汇总测试结果
  - 使用 message 工具通知用户验收
  - 格式：简短中文，4行（做了什么/改了什么/验证结果/下一步）
```

## 自动执行机制
- 每个 agent 被 spawn 后立即执行
- 完成后自动 spawn 下游 agent 或通知上游
- 无需用户对话触发
- **闭环通知确保任务不遗漏**

## 静默执行规则 (Silent Execution)
**默认回复 NO_REPLY**，只在以下情况发送消息：
- 任务完成
- 遇到阻塞需要决策
- 发现关键缺陷

**禁止发送**："收到"、"正在处理"、进度更新等无意义消息。

## 用户操作
1. **下达任务**：描述要开发的功能
2. **确认验收**：收到 pm-lead 的完成通知后验收

中间过程全自动推进，闭环通知确保不遗漏。

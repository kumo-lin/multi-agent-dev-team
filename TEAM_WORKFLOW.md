# TEAM_WORKFLOW.md - 6角色自动工作流

## 触发方式
**无需 Cron**，消息驱动自动执行。

## 完整工作流

```
用户下达任务
    ↓
main (kimi2.5) 接收并确认
    ↓
spawn pm-lead
    ↓
pm-lead (kimi2.5) 拆解任务
    ↓
spawn pm-product
    ↓
pm-product (kimi2.5) 输出 PRD
    ↓
spawn designer-lead
    ↓
designer-lead (kimi2.5) 输出设计
    ↓
并行 spawn:
    ├── backend-lead (deepseek-v3.2)
    └── frontend-lead (deepseek-v3.2)
    ↓
两者都完成后
    ↓
spawn qa-lead (deepseek-v3.2)
    ↓
qa-lead 验收完成
    ↓
通知 pm-lead → 通知用户验收
```

## 通知链路

| 阶段 | 执行者 | 完成后通知 |
|------|--------|-----------|
| 需求分析 | pm-product | designer-lead |
| 设计 | designer-lead | backend-lead + frontend-lead（并行） |
| 后端开发 | backend-lead | qa-lead（等待前端） |
| 前端开发 | frontend-lead | qa-lead（等待后端） |
| 测试 | qa-lead | pm-lead → 用户 |
| 汇总 | pm-lead | 用户（验收通知） |

## 自动执行机制
- 每个 agent 被 spawn 后立即执行
- 完成后自动 spawn 下游 agent
- 无需用户对话触发
- 只在关键节点（阻塞/完成）通知用户

## 用户操作
1. **下达任务**：描述要开发的功能
2. **确认验收**：收到完成通知后验收

中间过程全自动推进。

# PROJECT_ISOLATION.md - 项目频道隔离配置

## 规则
1. **频道绑定**：每个项目绑定一个 Discord 频道
2. **指令归属**：在某频道下达的指令，只处理该频道对应的项目
3. **跨频道处理**：
   - 若用户在其他频道询问某项目，回复：「请回到 #频道名 讨论此项目」
   - 不跨频道同步任务状态
4. **新项目创建**：
   - 用户创建新 Discord 频道
   - 在新频道下达开发指令
   - 自动绑定该频道为新项目

## 指令示例

**正确做法：**
- 在 #project-a 中：「开发登录功能」→ 执行

**错误做法：**
- 在 #general 中：「project-a进度如何？」→ 回复「请回到 #project-a 查看」

## 配置建议

### Discord 配置
```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "groupPolicy": "allowlist",
      "dmPolicy": "allowlist",
      "allowFrom": ["YOUR_USER_ID"],
      "guilds": {
        "YOUR_GUILD_ID": {
          "requireMention": true
        }
      }
    }
  }
}
```

### 记忆策略
建议在 memory 中存储：
- 项目与频道的绑定关系
- 用户偏好（如时间格式、汇报风格）

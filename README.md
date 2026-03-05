# Multi-Agent Development Team for OpenClaw

> 解放生产力，让人人都可以成为一人公司。
> 
> Liberate productivity, enable everyone to become a one-person company.
> 
> 生産性を解放し、誰もが一人会社になれるようにする。

---

## 🌍 Languages / 语言 / 言語

- [English](#english)
- [中文](#中文)
- [日本語](#日本語)

---

<a name="english"></a>
## 🇺🇸 English

### What is this?

A complete 6-role AI development team architecture for OpenClaw that automates the entire workflow from requirements to delivery.

**No Cron jobs. No manual coordination. Just message-driven execution.**

### The 6 Roles

| Role | Responsibility | Can Delegate To |
|------|----------------|-----------------|
| Project Lead | Progress control, resource coordination | Product Manager, Designer, Backend, Frontend, QA |
| Product Manager | Requirements analysis, PRD writing | Designer, Backend, Frontend, QA |
| Designer | UI/UX design, prototyping | Backend, Frontend, QA |
| Backend Dev | API design, database, business logic | Frontend, QA |
| Frontend Dev | Page implementation, interaction | QA |
| QA Engineer | Test cases, acceptance testing | Project Lead (notify on completion) |

### Workflow & Notification Loop

```
You: "Develop login feature for Project A"
    ↓
main → Project Lead → Product Manager → Designer → Backend & Frontend (parallel) → QA
    ↓
QA completes → Notify Project Lead → Notify you: "Feature ready for review"
```

**Closed-loop notification**: When QA finishes testing, it **must** notify Project Lead, who then notifies you. This ensures no task falls through the cracks.

**Fully automated. You only speak at the start and at the end.**

### Notification Rules (Silent Execution)

**Default: NO_REPLY**

Agents only send messages for:
- ✅ Task completion
- ✅ Blockers that need your decision
- ✅ Critical defects found

**No "received", no "working on it", no progress updates.**

### What Problem Does It Solve?

1. **No more context switching** between different AI tools
2. **No more manual coordination** between "chatbots"
3. **True autonomy** - the team runs itself once given a goal
4. **Channel isolation** - each project runs in its own Discord channel without interference
5. **Closed-loop guarantee** - QA → PM Lead → User, nothing gets lost

### The Experience

- **You say**: "Build a payment system"
- **The system does**:
  1. Product Manager analyzes requirements
  2. Designer creates UI/UX
  3. Backend builds API
  4. Frontend implements interface
  5. QA tests everything
  6. **QA notifies PM Lead → PM Lead notifies you**
- **You receive**: "Payment system complete. 12 test cases passed. Ready for your review."

**That's it. One command, complete product.**

### Vision

> **Liberate productivity. Enable everyone to become a one-person company.**

In the AI era, solo entrepreneurs shouldn't be limited by their technical skills or team size. This tool lets one person command an entire development team, turning ideas into products at unprecedented speed.

---

<a name="中文"></a>
## 🇨🇳 中文

### 这是什么？

一个完整的6角色AI开发团队架构，专为 OpenClaw 设计，实现从需求到交付的全自动工作流。

**无需定时任务。无需人工协调。纯消息驱动执行。**

### 6个角色

| 角色 | 职责 | 可委派给 |
|------|------|----------|
| 项目总监 | 进度把控、资源协调 | 产品经理、设计师、后端、前端、测试 |
| 产品经理 | 需求分析、PRD撰写 | 设计师、后端、前端、测试 |
| 设计师 | UI/UX设计、原型输出 | 后端、前端、测试 |
| 后端开发 | API设计、数据库、业务逻辑 | 前端、测试 |
| 前端开发 | 页面实现、交互开发 | 测试 |
| 测试工程师 | 测试用例、验收测试 | 项目总监（完成时通知） |

### 工作流程与通知闭环

```
你说："为项目A开发登录功能"
    ↓
主控 → 项目总监 → 产品经理 → 设计师 → 后端与前端（并行） → 测试
    ↓
测试完成 → 通知项目总监 → 通知你："功能已完成，请验收"
```

**闭环通知**：测试完成后**必须**通知项目总监，再由项目总监通知你。确保任务不会遗漏。

**全自动。你只需要在开始和结束时说话。**

### 通知规则（静默执行）

**默认：NO_REPLY（不回复）**

Agent只在以下情况发送消息：
- ✅ 任务完成
- ✅ 需要你做决策的阻塞
- ✅ 发现关键缺陷

**不发送"收到"、不发送"正在处理"、不发送进度更新。**

### 解决什么问题？

1. **不再频繁切换**不同的AI工具
2. **不再人工协调**各个"聊天机器人"
3. **真正自主** - 给定目标后团队自行运转
4. **频道隔离** - 每个项目在独立的Discord频道运行，互不干扰
5. **闭环保障** - 测试 → 项目总监 → 用户，任务不遗漏

### 使用体验

- **你说**："做一个支付系统"
- **系统自动**：
  1. 产品经理分析需求
  2. 设计师设计UI/UX
  3. 后端开发API
  4. 前端实现界面
  5. 测试全面验证
  6. **测试通知项目总监 → 项目总监通知你**
- **你收到**："支付系统已完成。12个测试用例通过。请验收。"

**就这些。一个指令，完整产品。**

### 愿景

> **解放生产力，让人人都可以成为一人公司。**

在AI时代，独立创业者不应受限于技术能力或团队规模。这个工具让一个人就能指挥整个开发团队，以前所未有的速度将想法变为产品。

---

<a name="日本語"></a>
## 🇯🇵 日本語

### これは何ですか？

OpenClaw用の完全な6役割AI開発チームアーキテクチャで、要件から納品までのワークフローを完全自動化します。

**Cronジョブなし。手動調整なし。メッセージ駆動型実行。**

### 6つの役割

| 役割 | 責任 | 委任可能先 |
|------|------|------------|
| プロジェクトリード | 進度管理、リソース調整 | プロダクトマネージャー、デザイナー、バックエンド、フロントエンド、QA |
| プロダクトマネージャー | 要件分析、PRD作成 | デザイナー、バックエンド、フロントエンド、QA |
| デザイナー | UI/UXデザイン、プロトタイプ | バックエンド、フロントエンド、QA |
| バックエンド開発 | API設計、データベース、ビジネスロジック | フロントエンド、QA |
| フロントエンド開発 | ページ実装、インタラクション | QA |
| QAエンジニア | テストケース、受け入れテスト | プロジェクトリード（完了時に通知） |

### ワークフローと通知閉ループ

```
あなた：「プロジェクトAにログイン機能を開発して」
    ↓
メイン → プロジェクトリード → プロダクトマネージャー → デザイナー → バックエンド＆フロントエンド（並列） → QA
    ↓
QA完了 → プロジェクトリードに通知 → あなたに通知：「機能が完成しました。レビューしてください」
```

**閉ループ通知**：QAが完了したら**必ず**プロジェクトリードに通知し、プロジェクトリードがあなたに通知します。タスクが漏れることはありません。

**完全自動化。最初と最後だけ話します。**

### 通知ルール（サイレント実行）

**デフォルト：NO_REPLY（返信なし）**

Agentは以下の場合のみメッセージを送信：
- ✅ タスク完了
- ✅ あなたの意思決定が必要なブロック
- ✅ 重大な欠陥を発見

**「了解」や「処理中」や進捗更新は送信しません。**

### 解決する問題

1. **AIツール間の切り替え**が不要
2. **「チャットボット」間の手動調整**が不要
3. **真の自律性** - 目標を与えるとチームが自動的に動作
4. **チャンネル分離** - 各プロジェクトは独自のDiscordチャンネルで実行
5. **閉ループ保証** - QA → プロジェクトリード → ユーザー、タスクは漏れない

### 体験

- **あなたが言う**：「支払いシステムを作って」
- **システムが自動的に**：
  1. プロダクトマネージャーが要件を分析
  2. デザイナーがUI/UXを作成
  3. バックエンドがAPIを構築
  4. フロントエンドがインターフェースを実装
  5. QAがすべてをテスト
  6. **QAがプロジェクトリードに通知 → プロジェクトリードがあなたに通知**
- **あなたが受け取る**：「支払いシステムが完成しました。12のテストケースが通過。レビューしてください。」

**これだけ。1つのコマンドで、完全な製品。**

### ビジョン

> **生産性を解放し、誰もが一人会社になれるようにする。**

AI時代に、個人の起業家は技術スキルやチーム規模に制限されるべきではありません。このツールは1人で開発チーム全体を指揮でき、前例のないスピードでアイデアを製品に変えられます。

---

## 🚀 Quick Start / 快速开始 / クイックスタート

### Installation / 安装 / インストール

```bash
# Via ClawHub
clawhub install multi-agent-dev-team

# Or manual / 或手动 / または手動
mkdir -p ~/.openclaw/workspace/skills/
cd ~/.openclaw/workspace/skills/
git clone https://github.com/hengcheng-lin/multi-agent-dev-team.git
```

### Configuration / 配置 / 設定

1. Copy `config-template.json` to your OpenClaw config
2. Configure your preferred AI models (recommend: strong reasoning model for PM/Design roles, coding-focused model for Dev/QA roles)
3. Replace `YOUR_API_KEY` with your actual API keys
4. Restart OpenClaw: `openclaw gateway restart`

### Usage / 使用 / 使用方法

```
You: "Develop a task management app"
    ↓
System runs automatically...
    ↓
Notification: "Task management app completed. Ready for review."
```

---

## 📁 Structure / 结构 / 構造

```
multi-agent-dev-team/
├── SKILL.md                 # Main documentation
├── README.md               # This file
├── LICENSE                 # MIT License
├── install.sh             # Installation script
├── config-template.json   # Configuration template
├── TEAM_WORKFLOW.md      # Workflow documentation
├── PROJECT_ISOLATION.md  # Channel isolation guide
└── agents/               # Agent prompts
    ├── pm-lead/
    ├── pm-product/
    ├── designer-lead/
    ├── backend-lead/
    ├── frontend-lead/
    └── qa-lead/
```

---

## 🔄 Notification Loop Detail / 通知闭环详情 / 通知閉ループの詳細

### QA → PM Lead → User / 测试 → 项目总监 → 用户 / QA → プロジェクトリード → ユーザー

This is the **critical closed loop** that ensures nothing gets lost:

**English:**
1. QA completes testing
2. QA **must** notify PM Lead (via `sessions_send` or status file)
3. PM Lead receives notification and **must** notify user
4. User receives final completion message

**中文：**
1. 测试完成验收
2. 测试**必须**通知项目总监（通过 `sessions_send` 或状态文件）
3. 项目总监收到通知后**必须**通知用户
4. 用户收到最终完成消息

**日本語：**
1. QAがテストを完了
2. QAは**必ず**プロジェクトリードに通知（`sessions_send`またはステータスファイル経由）
3. プロジェクトリードが通知を受け取り、**必ず**ユーザーに通知
4. ユーザーが最終完了メッセージを受信

---

## 🤝 Contributing / 贡献 / 貢献

Contributions are welcome! Please feel free to submit issues and pull requests.

欢迎提交 Issue 和 Pull Request。

IssuesやPull Requestを歓迎します。

---

## 📜 License / 许可证 / ライセンス

MIT License

---

## 💡 Author's Note / 作者的话 / 作者の言葉

> "I built this because I believe in a future where one person with a vision can create anything. No funding needed. No hiring needed. Just an idea and an AI team that works while you sleep."
> 
> — Hengcheng Lin

> "我创建这个是因为我相信这样一个未来：一个有愿景的人可以创造任何东西。不需要融资，不需要招聘。只需要一个想法和一个在你睡觉时工作的AI团队。"
> 
> — 林恒成

> 「このツールを作ったのは、ビジョンを持つ一人の人間が何でも作れる未来を信じているからです。資金調達も採用も不要。ただアイデアと、あなたが寝ている間に働くAIチームがあればいい。」
> 
> — 林恒成

---

**🌟 Star this repo if you believe in the future of one-person companies!**

**🌟 如果你相信一人公司的未来，请给这个仓库点星！**

**🌟 一人会社の未来を信じるなら、このリポジトリにスターを付けてください！**

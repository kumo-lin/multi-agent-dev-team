# 使用示例

## 示例 0：频道绑定演示

### 场景：在正确频道沟通

**用户在 #aa-settlement 频道**：
```
用户：创建一个 AA 结算助手

项目总监：✅ 项目 aa-settlement 已创建（绑定到 #aa-settlement）
```

**用户继续在 #aa-settlement 频道**：
```
用户：查看状态

项目总监：📊 当前状态...
```

### 场景：跨频道被拒绝

**用户在 #general 频道**：
```
用户：AA 结算助手怎么样了？

项目总监：请回到 #aa-settlement 频道继续讨论 AA 结算助手
```

## 示例 1：创建 AA 结算助手项目

### 用户输入
创建一个 AA 结算助手，支持多项目、成员管理、消费记录、自动结算

### 项目总监会话（主线程）

项目总监：
✅ 项目 aa-settlement 已创建
📋 已派发给产品经理编写 PRD
💬 讨论线程：#aa-settlement-pm

### 产品经理会话（#aa-settlement-pm 线程）

产品经理：
PRD 已完成！

功能模块：
1. 项目管理（P0）- 创建、编辑、删除项目
2. 成员管理（P0）- 添加、编辑、删除成员
3. 消费记录（P0）- 记录消费、分摊设置
4. 结算算法（P0）- 自动计算谁该给谁多少钱
5. 结算结果（P0）- 展示结算方案

详细文档：/workspace/projects/aa-settlement/prd.md

### 项目总监会话（主线程）

项目总监：
📋 PRD 已完成
📐 已派发给设计师
💬 设计讨论：#aa-settlement-design

### 设计师会话（#aa-settlement-design 线程）

设计师：
设计稿已完成！

页面：
- 首页：项目列表
- 项目详情：成员 + 消费记录
- 添加消费：表单页面
- 结算结果：展示页面

设计规范：
- 主色：#1890ff
- 字体：系统默认
- 布局：响应式，移动端优先

详细文档：/workspace/projects/aa-settlement/design/

### 项目总监会话（主线程）

项目总监：
📐 设计稿已完成
💻 前后端开始并行开发

后端开发：#aa-settlement-backend
前端开发：#aa-settlement-frontend

### 后端开发会话（#aa-settlement-backend 线程）

后端开发：
API 开发完成！

接口列表：
- GET /api/projects - 项目列表
- POST /api/projects - 创建项目
- GET /api/projects/{id}/members - 成员列表
- POST /api/projects/{id}/members - 添加成员
- GET /api/projects/{id}/expenses - 消费记录
- POST /api/projects/{id}/expenses - 添加消费
- POST /api/projects/{id}/settle - 结算

测试：全部通过（15/15）

### 前端开发会话（#aa-settlement-frontend 线程）

前端开发：
页面开发完成！

实现页面：
- 首页：项目列表 + 创建按钮
- 项目详情：成员管理 + 消费记录表格
- 添加消费：表单 + 分摊设置
- 结算结果：展示 + 导出

设计还原度：98%

### 项目总监会话（主线程）

项目总监：
💻 开发完成
🧪 已派发给测试验收
💬 测试线程：#aa-settlement-qa

### 测试会话（#aa-settlement-qa 线程）

测试：
验收完成！

测试用例：20 个
通过：20 个
失败：0 个

功能：✅ 全部正常
UI 还原：✅ 98% 符合设计
性能：✅ 响应 < 200ms

测试报告：/workspace/projects/aa-settlement/results/test-report.md

### 项目总监会话（主线程）

项目总监：
🎉 AA 结算助手开发完成！

📊 项目统计
- 总任务：5
- 已完成：5
- 总耗时：2小时32分钟

📁 交付物
- 代码：/workspace/projects/aa-settlement/
- PRD：prd.md
- 设计稿：design/
- 测试报告：results/test-report.md

✅ 功能验收：通过
✅ 设计还原：通过
✅ 测试覆盖：通过

项目已交付，请验收！

---

## 示例 2：跳过设计阶段

用户：开发一个简单的 TODO 应用，跳过设计，直接开发

项目总监：
✅ 项目 todo-app 已创建
💻 跳过设计阶段，直接开始开发

后端开发：#todo-app-backend
前端开发：#todo-app-frontend

---

## 示例 3：查看项目状态

用户：查看 aa-settlement 状态

项目总监：
📊 aa-settlement 项目状态

✅ 产品经理 - 编写 PRD
✅ 设计师 - UI 设计
✅ 后端开发 - API 开发
✅ 前端开发 - 页面开发
🔄 测试 - 验收测试

总任务：5 | 已完成：4 | 进行中：1 | 待开始：0

---

## 示例 4：后端独立任务

用户：给 aa-settlement 添加一个导出 Excel 功能

项目总监：
已添加任务 aa-settlement-export-001
分配给后端开发

后端开发：#aa-settlement-export-001

后端开发（在独立线程）：
导出功能已完成！
- 支持导出项目消费记录
- 支持导出结算结果
- 格式：Excel (.xlsx)

项目总监：
✅ 导出功能已完成
📁 代码已合并到主分支

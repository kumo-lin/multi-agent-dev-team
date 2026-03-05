#!/usr/bin/env python3
"""
项目经理助手 - 主 Agent 调用
用于处理用户指令、协调各角色、汇报进度
"""

import json
import subprocess
import sys
from pathlib import Path

ORCHESTRATOR = Path(__file__).parent / "orchestrator.py"


def run_orchestrator(*args):
    """运行编排器命令"""
    cmd = [sys.executable, str(ORCHESTRATOR)] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return {"error": result.stderr}
    return json.loads(result.stdout)


class ProjectManager:
    """项目经理助手"""
    
    def create_project(self, name: str, description: str, skip_design: bool = False):
        """创建项目"""
        # 1. 创建项目
        result = run_orchestrator("create", name, description)
        if "error" in result:
            return result
        
        # 2. 自动派发给产品经理
        pm_result = run_orchestrator("dispatch-pm", name)
        
        return {
            "action": "create_project",
            "project": name,
            "next_step": "产品经理正在编写 PRD",
            "thread": f"#{name}-pm",
            "message": f"""✅ 项目 {name} 已创建
📋 已派发给产品经理编写 PRD
💬 讨论线程：#{name}-pm

请稍等，PRD 完成后会自动通知你。"""
        }
    
    def on_prd_complete(self, project_name: str, skip_design: bool = False):
        """PRD 完成后的处理"""
        if skip_design:
            # 跳过设计，直接开发
            result = run_orchestrator("dispatch-dev", project_name)
            return {
                "action": "start_development",
                "project": project_name,
                "message": f"""📋 PRD 已完成
💻 已跳过设计阶段，直接开始开发

后端开发：#{project_name}-backend
前端开发：#{project_name}-frontend"""
            }
        else:
            # 正常流程，先设计
            result = run_orchestrator("dispatch-design", project_name)
            return {
                "action": "start_design",
                "project": project_name,
                "message": f"""📋 PRD 已完成
📐 已派发给设计师

设计讨论：#{project_name}-design"""
            }
    
    def on_design_complete(self, project_name: str):
        """设计完成后的处理"""
        result = run_orchestrator("dispatch-dev", project_name)
        return {
            "action": "start_development",
            "project": project_name,
            "message": f"""📐 设计稿已完成
💻 前后端开始并行开发

后端开发：#{project_name}-backend
前端开发：#{project_name}-frontend"""
        }
    
    def on_dev_complete(self, project_name: str):
        """开发完成后的处理"""
        result = run_orchestrator("dispatch-qa", project_name)
        return {
            "action": "start_qa",
            "project": project_name,
            "message": f"""💻 开发完成
🧪 已派发给测试验收

测试线程：#{project_name}-qa"""
        }
    
    def on_qa_complete(self, project_name: str):
        """测试完成后的处理"""
        result = run_orchestrator("status", project_name)
        status = result.get("summary", "")
        
        return {
            "action": "project_complete",
            "project": project_name,
            "message": f"""🎉 项目 {project_name} 开发完成！

📊 {status}
📁 代码位置：/workspace/projects/{project_name}/

所有任务已完成，请验收。"""
        }
    
    def get_status(self, project_name: str):
        """获取项目状态"""
        result = run_orchestrator("status", project_name)
        
        if "error" in result:
            return {"error": result["error"]}
        
        tasks = result.get("tasks", {})
        lines = [f"📊 {project_name} 项目状态\n"]
        
        # 按角色分组
        by_agent = {}
        for task_id, task in tasks.items():
            agent = task["agent"]
            if agent not in by_agent:
                by_agent[agent] = []
            by_agent[agent].append(task)
        
        # 输出
        agent_names = {
            "pm": "产品经理",
            "designer": "设计师",
            "backend": "后端开发",
            "frontend": "前端开发",
            "qa": "测试"
        }
        
        for agent, agent_tasks in by_agent.items():
            name = agent_names.get(agent, agent)
            for task in agent_tasks:
                status_icon = {
                    "done": "✅",
                    "in-progress": "🔄",
                    "pending": "⬜"
                }.get(task["status"], "⬜")
                lines.append(f"{status_icon} {name} - {task['description']}")
        
        lines.append(f"\n{result.get('summary', '')}")
        
        return {
            "action": "status_report",
            "project": project_name,
            "message": "\n".join(lines)
        }


def main():
    """CLI 入口"""
    if len(sys.argv) < 2:
        print("Usage: python project_manager.py <command> [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    pm = ProjectManager()
    
    if cmd == "create":
        name = sys.argv[2]
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        skip_design = "--skip-design" in sys.argv
        result = pm.create_project(name, desc, skip_design)
        print(json.dumps(result, indent=2))
    
    elif cmd == "on-prd-complete":
        name = sys.argv[2]
        skip_design = "--skip-design" in sys.argv
        result = pm.on_prd_complete(name, skip_design)
        print(json.dumps(result, indent=2))
    
    elif cmd == "on-design-complete":
        name = sys.argv[2]
        result = pm.on_design_complete(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "on-dev-complete":
        name = sys.argv[2]
        result = pm.on_dev_complete(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "on-qa-complete":
        name = sys.argv[2]
        result = pm.on_qa_complete(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "status":
        name = sys.argv[2]
        result = pm.get_status(name)
        print(json.dumps(result, indent=2))
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()

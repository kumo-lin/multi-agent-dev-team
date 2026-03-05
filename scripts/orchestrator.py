#!/usr/bin/env python3
"""
多 Agent 开发团队编排器
核心功能：项目管理、任务派发、状态跟踪、自动推进
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# 配置
WORKSPACE_DIR = Path(os.getenv("MADT_WORKSPACE", "/home/node/.openclaw/workspace/projects"))
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)

AGENTS = ["director", "pm", "designer", "backend", "frontend", "qa"]

class Project:
    """项目实体"""
    
    def __init__(self, name: str):
        self.name = name
        self.dir = WORKSPACE_DIR / name
        self.config_file = self.dir / "config.json"
        self.load_or_create()
    
    def load_or_create(self):
        """加载或创建项目"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            self.dir.mkdir(parents=True, exist_ok=True)
            (self.dir / "tasks").mkdir(exist_ok=True)
            (self.dir / "results").mkdir(exist_ok=True)
            (self.dir / "design").mkdir(exist_ok=True)
            
            self.config = {
                "name": self.name,
                "status": "created",
                "created_at": datetime.now().isoformat(),
                "tasks": {},
                "threads": {},
                "skip_roles": [],
                "current_phase": "init",
                "channel_binding": None
            }
            self.save()
    
    def save(self):
        """保存项目配置"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def add_task(self, task_id: str, agent: str, description: str, deps: list = None):
        """添加任务"""
        self.config["tasks"][task_id] = {
            "id": task_id,
            "agent": agent,
            "description": description,
            "deps": deps or [],
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
            "output": None,
            "thread": None
        }
        self.save()
    
    def update_task(self, task_id: str, status: str, output: str = None):
        """更新任务状态"""
        if task_id in self.config["tasks"]:
            self.config["tasks"][task_id]["status"] = status
            if output:
                self.config["tasks"][task_id]["output"] = output
            if status == "done":
                self.config["tasks"][task_id]["completed_at"] = datetime.now().isoformat()
            self.save()
    
    def get_ready_tasks(self) -> list:
        """获取可执行的任务（依赖已完成）"""
        ready = []
        for task_id, task in self.config["tasks"].items():
            if task["status"] != "pending":
                continue
            # 检查依赖
            deps_satisfied = all(
                self.config["tasks"].get(dep, {}).get("status") == "done"
                for dep in task["deps"]
            )
            if deps_satisfied:
                ready.append(task)
        return ready
    
    def set_channel_binding(self, channel: str, channel_id: str):
        """设置频道绑定"""
        self.config["channel_binding"] = {
            "channel": channel,
            "channel_id": channel_id,
            "bound_at": datetime.now().isoformat()
        }
        self.save()
    
    def get_channel_binding(self) -> dict:
        """获取频道绑定信息"""
        return self.config.get("channel_binding")
    
    def get_status_summary(self) -> str:
        """获取状态摘要"""
        tasks = self.config["tasks"]
        total = len(tasks)
        done = sum(1 for t in tasks.values() if t["status"] == "done")
        in_progress = sum(1 for t in tasks.values() if t["status"] == "in-progress")
        pending = total - done - in_progress
        
        return f"总任务: {total} | 已完成: {done} | 进行中: {in_progress} | 待开始: {pending}"


class Orchestrator:
    """编排器核心"""
    
    def __init__(self):
        pass
    
    def create_project(self, name: str, description: str, skip_roles: list = None, channel: str = None, channel_id: str = None) -> dict:
        """创建新项目"""
        project = Project(name)
        project.config["description"] = description
        project.config["skip_roles"] = skip_roles or []
        
        # 绑定频道
        if channel and channel_id:
            project.set_channel_binding(channel, channel_id)
        
        project.save()
        
        return {
            "success": True,
            "project": name,
            "message": f"项目 {name} 已创建",
            "workspace": str(project.dir),
            "channel_binding": {"channel": channel, "channel_id": channel_id} if channel else None
        }
    
    def dispatch_to_pm(self, project_name: str) -> dict:
        """派发给产品经理"""
        project = Project(project_name)
        task_id = f"{project_name}-prd"
        
        project.add_task(
            task_id=task_id,
            agent="pm",
            description=f"为 {project_name} 编写 PRD",
            deps=[]
        )
        
        return {
            "success": True,
            "task_id": task_id,
            "agent": "pm",
            "message": "已派发给产品经理"
        }
    
    def dispatch_to_designer(self, project_name: str) -> dict:
        """派发给设计师"""
        project = Project(project_name)
        task_id = f"{project_name}-design"
        
        project.add_task(
            task_id=task_id,
            agent="designer",
            description=f"为 {project_name} 设计 UI",
            deps=[f"{project_name}-prd"]
        )
        
        return {
            "success": True,
            "task_id": task_id,
            "agent": "designer",
            "message": "已派发给设计师"
        }
    
    def dispatch_development(self, project_name: str) -> dict:
        """派发开发任务（前后端并行）"""
        project = Project(project_name)
        
        # 后端任务
        backend_task = f"{project_name}-backend"
        backend_deps = [f"{project_name}-prd"]
        if f"{project_name}-design" in project.config["tasks"]:
            backend_deps.append(f"{project_name}-design")
        
        project.add_task(
            task_id=backend_task,
            agent="backend",
            description=f"开发 {project_name} 后端 API",
            deps=backend_deps
        )
        
        # 前端任务
        frontend_task = f"{project_name}-frontend"
        frontend_deps = [f"{project_name}-prd"]
        if f"{project_name}-design" in project.config["tasks"]:
            frontend_deps.append(f"{project_name}-design")
        
        project.add_task(
            task_id=frontend_task,
            agent="frontend",
            description=f"开发 {project_name} 前端页面",
            deps=frontend_deps
        )
        
        return {
            "success": True,
            "tasks": [backend_task, frontend_task],
            "message": "已派发前后端开发任务"
        }
    
    def dispatch_qa(self, project_name: str) -> dict:
        """派发测试任务"""
        project = Project(project_name)
        task_id = f"{project_name}-qa"
        
        project.add_task(
            task_id=task_id,
            agent="qa",
            description=f"验收 {project_name}",
            deps=[f"{project_name}-backend", f"{project_name}-frontend"]
        )
        
        return {
            "success": True,
            "task_id": task_id,
            "agent": "qa",
            "message": "已派发给测试"
        }
    
    def get_project_status(self, project_name: str) -> dict:
        """获取项目状态"""
        project = Project(project_name)
        
        return {
            "name": project.name,
            "status": project.config["status"],
            "summary": project.get_status_summary(),
            "tasks": project.config["tasks"],
            "threads": project.config["threads"]
        }
    
    def mark_task_done(self, project_name: str, task_id: str, output: str = None) -> dict:
        """标记任务完成"""
        project = Project(project_name)
        project.update_task(task_id, "done", output)
        
        # 检查是否有新任务可以开始
        ready = project.get_ready_tasks()
        
        return {
            "success": True,
            "task_id": task_id,
            "ready_tasks": [t["id"] for t in ready],
            "message": f"任务 {task_id} 已完成"
        }


def main():
    """CLI 入口"""
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py <command> [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    orch = Orchestrator()
    
    if cmd == "create":
        name = sys.argv[2]
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        result = orch.create_project(name, desc)
        print(json.dumps(result, indent=2))
    
    elif cmd == "dispatch-pm":
        name = sys.argv[2]
        result = orch.dispatch_to_pm(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "dispatch-design":
        name = sys.argv[2]
        result = orch.dispatch_to_designer(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "dispatch-dev":
        name = sys.argv[2]
        result = orch.dispatch_development(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "dispatch-qa":
        name = sys.argv[2]
        result = orch.dispatch_qa(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "status":
        name = sys.argv[2]
        result = orch.get_project_status(name)
        print(json.dumps(result, indent=2))
    
    elif cmd == "done":
        name = sys.argv[2]
        task_id = sys.argv[3]
        output = sys.argv[4] if len(sys.argv) > 4 else None
        result = orch.mark_task_done(name, task_id, output)
        print(json.dumps(result, indent=2))
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
频道绑定管理器
确保项目沟通都在创建该项目的频道内进行
"""

import json
import os
from pathlib import Path

# 配置
ORCHESTRATOR_DIR = Path("/home/node/.openclaw/workspace/.orchestrator")
ORCHESTRATOR_DIR.mkdir(parents=True, exist_ok=True)

CHANNEL_MAP_FILE = ORCHESTRATOR_DIR / "channel_projects.json"


class ChannelBinding:
    """频道绑定管理"""
    
    def __init__(self):
        self.mapping = self._load_mapping()
    
    def _load_mapping(self) -> dict:
        """加载频道-项目映射"""
        if CHANNEL_MAP_FILE.exists():
            with open(CHANNEL_MAP_FILE) as f:
                return json.load(f)
        return {"projects": {}, "channels": {}}
    
    def _save_mapping(self):
        """保存映射"""
        with open(CHANNEL_MAP_FILE, 'w') as f:
            json.dump(self.mapping, f, indent=2)
    
    def bind_project_to_channel(self, project: str, channel: str, channel_id: str):
        """
        绑定项目到频道
        project: 项目名
        channel: 频道名
        channel_id: 频道ID
        """
        self.mapping["projects"][project] = {
            "channel": channel,
            "channel_id": channel_id,
            "created_at": str(__import__('datetime').datetime.now())
        }
        self.mapping["channels"][channel_id] = project
        self._save_mapping()
    
    def get_project_channel(self, project: str) -> dict:
        """获取项目绑定的频道"""
        return self.mapping["projects"].get(project)
    
    def get_channel_project(self, channel_id: str) -> str:
        """获取频道绑定的项目"""
        return self.mapping["channels"].get(channel_id)
    
    def check_communication_valid(self, project: str, current_channel_id: str) -> tuple:
        """
        检查项目沟通是否在正确频道
        返回: (是否有效, 应去频道名, 提示消息)
        """
        binding = self.get_project_channel(project)
        if not binding:
            # 项目未绑定，允许在当前频道
            return True, None, None
        
        if binding["channel_id"] == current_channel_id:
            # 在正确频道
            return True, None, None
        
        # 不在正确频道
        return False, binding["channel"], f"请回到 #{binding['channel']} 频道继续讨论 {project}"
    
    def is_project_bound(self, project: str) -> bool:
        """检查项目是否已绑定频道"""
        return project in self.mapping["projects"]
    
    def list_bindings(self) -> dict:
        """列出所有绑定"""
        return self.mapping["projects"]
    
    def unbind_project(self, project: str):
        """解除项目绑定（项目完成时调用）"""
        if project in self.mapping["projects"]:
            channel_id = self.mapping["projects"][project]["channel_id"]
            del self.mapping["projects"][project]
            if channel_id in self.mapping["channels"]:
                del self.mapping["channels"][channel_id]
            self._save_mapping()


# CLI 接口
def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python channel_binding.py <command> [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    binding = ChannelBinding()
    
    if cmd == "bind":
        project = sys.argv[2]
        channel = sys.argv[3]
        channel_id = sys.argv[4]
        binding.bind_project_to_channel(project, channel, channel_id)
        print(json.dumps({"success": True, "message": f"项目 {project} 绑定到 {channel}"}))
    
    elif cmd == "check":
        project = sys.argv[2]
        current_channel = sys.argv[3]
        valid, target, msg = binding.check_communication_valid(project, current_channel)
        print(json.dumps({
            "valid": valid,
            "target_channel": target,
            "message": msg
        }))
    
    elif cmd == "get":
        project = sys.argv[2]
        info = binding.get_project_channel(project)
        print(json.dumps(info or {}))
    
    elif cmd == "list":
        bindings = binding.list_bindings()
        print(json.dumps(bindings, indent=2))
    
    elif cmd == "unbind":
        project = sys.argv[2]
        binding.unbind_project(project)
        print(json.dumps({"success": True, "message": f"项目 {project} 已解绑"}))
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()

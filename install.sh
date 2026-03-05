#!/bin/bash
# install.sh - Multi-Agent Development Team 安装脚本

set -e

echo "🚀 开始安装 Multi-Agent Development Team..."

# 检查 OpenClaw 目录
OPENCLAW_HOME="$HOME/.openclaw"
if [ ! -d "$OPENCLAW_HOME" ]; then
    echo "❌ OpenClaw 目录不存在: $OPENCLAW_HOME"
    echo "请先安装 OpenClaw"
    exit 1
fi

# 创建技能目录
SKILL_DIR="$OPENCLAW_HOME/workspace/skills/multi-agent-dev-team"
echo "📁 创建技能目录: $SKILL_DIR"
mkdir -p "$SKILL_DIR"

# 复制文件
echo "📄 复制文件..."
cp -r ./* "$SKILL_DIR/" 2>/dev/null || true

# 创建 agent 目录
echo "👥 创建 agent 目录..."
for agent in pm-lead pm-product designer-lead backend-lead frontend-lead qa-lead; do
    mkdir -p "$OPENCLAW_HOME/workspace/agents/$agent"
    mkdir -p "$OPENCLAW_HOME/agents/$agent/agent"
    
    # 复制 Prompt 文件
    if [ -f "$SKILL_DIR/agents/$agent/PROMPT.md" ]; then
        cp "$SKILL_DIR/agents/$agent/PROMPT.md" "$OPENCLAW_HOME/workspace/agents/$agent/PROMPT.md"
    fi
done

# 创建工作流文档
echo "📋 创建工作流文档..."
cp "$SKILL_DIR/TEAM_WORKFLOW.md" "$OPENCLAW_HOME/workspace/TEAM_WORKFLOW.md" 2>/dev/null || true
cp "$SKILL_DIR/PROJECT_ISOLATION.md" "$OPENCLAW_HOME/workspace/PROJECT_ISOLATION.md" 2>/dev/null || true

# 创建状态目录
echo "📊 创建状态目录..."
mkdir -p "$OPENCLAW_HOME/workspace/pipeline/state"

echo ""
echo "✅ 安装完成！"
echo ""
echo "接下来需要："
echo "1. 编辑 $OPENCLAW_HOME/openclaw.json，添加 agents 配置"
echo "2. 确保已配置 Kimi 和 DeepSeek 模型 API 密钥"
echo "3. 重启 OpenClaw: openclaw gateway restart"
echo ""
echo "详细配置请参考: $SKILL_DIR/SKILL.md"

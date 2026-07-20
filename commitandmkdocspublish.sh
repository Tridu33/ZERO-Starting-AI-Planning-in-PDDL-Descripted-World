#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# commitandmkdocspublish.sh
# 提交本地改动 → mkdocs build 验证 → 发布到 gh-pages
# ============================================================

COMMIT_MSG="${1:-}"

# 1. 提交本地改动
echo ">>> 检查本地改动..."
if git diff --quiet && git diff --cached --quiet; then
    echo "没有需要提交的改动，跳过 commit。"
else
    if [ -z "$COMMIT_MSG" ]; then
        # 如果没有传入 commit message，自动生成带时间戳的
        COMMIT_MSG="auto: $(date '+%Y-%m-%d %H:%M:%S')"
        echo ">>> 未提供 commit message，使用自动生成: $COMMIT_MSG"
    fi

    git add -A
    git commit -m "$COMMIT_MSG"
    echo ">>> 本地提交完成。"
fi

# 2. 推送到 main（确保 remote 有最新 commit）
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo ">>> 推送 $CURRENT_BRANCH 到 origin..."
git push origin "$CURRENT_BRANCH"

# 3. mkdocs build 验证
echo ">>> mkdocs build 验证..."
mkdocs build --strict 2>&1 || {
    echo "!!! mkdocs build 失败，请检查后重试。"
    exit 1
}
echo ">>> mkdocs build 成功。"

# 4. 发布到 gh-pages
echo ">>> 部署到 gh-pages..."
mkdocs gh-deploy --force --message "deploy: $(git log -1 --pretty=%B | head -1)"

echo ">>> 完成！本地改动已提交，文档已发布到 gh-pages。"

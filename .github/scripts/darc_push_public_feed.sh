#!/bin/bash
set -e

echo "🛰️ Syncing README.md to project-darc-feed..."

# Root of private repo (2 levels up from script)
PRIVATE_REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REPO_DIR="$PRIVATE_REPO_DIR/mirror-out"
BRANCH="main"
KEY_PATH="$HOME/.ssh/id_rsa"  # ✅ Match GitHub Actions location

# Check key exists
if [ ! -f "$KEY_PATH" ]; then
  echo "❌ ERROR: SSH key not found at $KEY_PATH"
  exit 1
fi

# Clone public repo fresh
rm -rf "$REPO_DIR"
GIT_SSH_COMMAND="ssh -i $KEY_PATH -o StrictHostKeyChecking=no" \
  git clone git@github.com:roninazure/project-darc-feed.git "$REPO_DIR"

# Copy README
cp "$PRIVATE_REPO_DIR/README.md" "$REPO_DIR/README.md"

# Git config
cd "$REPO_DIR"
git config user.name "CodexDaemon"
git config user.email "roninazure@gmail.com"

# Commit & push
git add README.md
git commit -m "🛰️ Auto-sync from private DARC [$(date -u)]" || echo "Nothing to commit."
GIT_SSH_COMMAND="ssh -i $KEY_PATH -o StrictHostKeyChecking=no" git push origin "$BRANCH"

#!/bin/bash
set -e

echo "🛰️ Syncing README.md to project-darc-feed..."

REPO_DIR="$HOME/tmp/project-darc-feed"
PRIVATE_REPO_DIR="$(pwd)"
BRANCH="main"

# Clone if not already
if [ ! -d "$REPO_DIR" ]; then
  git clone git@github.com:roninazure/project-darc-feed.git "$REPO_DIR"
fi

# Sync README
cp "$PRIVATE_REPO_DIR/README.md" "$REPO_DIR/README.md"

# Push to public
cd "$REPO_DIR"
git add README.md
git commit -m "🛰️ Auto-sync from private DARC [$(date -u)]" || echo "Nothing to commit."
GIT_SSH_COMMAND="ssh -i $PRIVATE_REPO_DIR/testkey" git push origin "$BRANCH"

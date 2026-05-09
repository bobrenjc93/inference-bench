#!/bin/bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOURS=4

echo "=== Cleaning builds/ to avoid syncing 27GB ==="
rm -rf "$PROJECT_DIR/builds"

# Write HF token to a temp file for the remote machine to pick up.
# This file is gitignored and deleted after the job.
if [ -f "$HOME/.cache/huggingface/token" ]; then
    cp "$HOME/.cache/huggingface/token" "$PROJECT_DIR/.hf_token"
fi
trap 'rm -f "$PROJECT_DIR/.hf_token"' EXIT

echo "=== Submitting benchmark job to 8xH100 ==="
gpu-dev submit \
  --gpu-type h100 \
  --gpus 8 \
  --hours "$HOURS" \
  --runtime "$PROJECT_DIR" \
  -- bash _remote_benchmark.sh

echo "=== Job complete, results synced back ==="

cd "$PROJECT_DIR"
git add results/
git commit -m "Benchmark run $(date +%Y%m%d_%H%M%S)"
git push
echo "=== Committed and pushed to main ==="

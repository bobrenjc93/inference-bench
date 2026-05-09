#!/bin/bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOURS=4
mkdir -p "$PROJECT_DIR/logs"
LOGFILE="$PROJECT_DIR/logs/benchmark_$(date +%Y%m%d_%H%M%S).log"

echo "Logging to $LOGFILE"

{
echo "=== $(date) Cleaning builds/ ==="
rm -rf "$PROJECT_DIR/builds"

if [ -f "$HOME/.cache/huggingface/token" ]; then
    cp "$HOME/.cache/huggingface/token" "$PROJECT_DIR/.hf_token"
fi
trap 'rm -f "$PROJECT_DIR/.hf_token"' EXIT

echo "=== $(date) Submitting benchmark job to 8xH100 ==="
} >> "$LOGFILE" 2>&1

gpu-dev submit \
  --gpu-type h100 \
  --gpus 8 \
  --hours "$HOURS" \
  --runtime "$PROJECT_DIR" \
  -- bash _remote_benchmark.sh
GPU_EXIT=$?

{
if [ "$GPU_EXIT" -ne 0 ]; then
    echo "=== $(date) gpu-dev submit failed with exit code $GPU_EXIT ==="
    exit "$GPU_EXIT"
fi

echo "=== $(date) Job complete, results synced back ==="

cd "$PROJECT_DIR"
git add results/
git commit -m "Benchmark run $(date +%Y%m%d_%H%M%S)"
git pull --rebase
git push
echo "=== $(date) Committed and pushed to main ==="
} >> "$LOGFILE" 2>&1

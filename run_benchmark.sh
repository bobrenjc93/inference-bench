#!/bin/bash
set -euo pipefail
trap '' PIPE

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOURS=2
TIMEOUT=7200
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

echo "=== $(date) Submitting benchmark job to 8xH100 (timeout=${TIMEOUT}s) ==="
} >> "$LOGFILE" 2>&1

timeout "$TIMEOUT" gpu-dev submit \
  --gpu-type h100 \
  --gpus 8 \
  --hours "$HOURS" \
  --runtime "$PROJECT_DIR" \
  -- bash _remote_benchmark.sh \
  >> "$LOGFILE" 2>&1
GPU_EXIT=$?

{
if [ "$GPU_EXIT" -eq 124 ]; then
    echo "=== $(date) Run timed out after ${TIMEOUT}s ==="
    exit 1
fi

if [ "$GPU_EXIT" -ne 0 ]; then
    echo "=== $(date) gpu-dev submit failed with exit code $GPU_EXIT ==="
    exit "$GPU_EXIT"
fi

echo "=== $(date) Job complete, results synced back ==="

cd "$PROJECT_DIR"
(
    flock -w 300 9 || { echo "=== $(date) Could not acquire git lock ==="; exit 1; }
    git add results/
    git stash --include-untracked
    git pull --rebase
    git stash pop || true
    git add results/
    git commit -m "Benchmark run $(date +%Y%m%d_%H%M%S)"
    git push
    echo "=== $(date) Committed and pushed to main ==="
) 9>"$PROJECT_DIR/.git-push.lock"
} >> "$LOGFILE" 2>&1

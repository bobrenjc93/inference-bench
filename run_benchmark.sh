#!/bin/bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
STAGING_DIR="/tmp/inference-bench-staging-$$"
HOURS=4
mkdir -p "$PROJECT_DIR/logs"
LOGFILE="$PROJECT_DIR/logs/benchmark_$(date +%Y%m%d_%H%M%S).log"

echo "Logging to $LOGFILE"

{
echo "=== $(date) Creating staging copy (excluding builds/) ==="
mkdir -p "$STAGING_DIR"
rsync -a \
  --exclude 'builds/' \
  --exclude '__pycache__/' \
  --exclude '*.pyc' \
  --exclude '.venv/' \
  --exclude '*.egg-info/' \
  "$PROJECT_DIR/" "$STAGING_DIR/"

if [ -f "$HOME/.cache/huggingface/token" ]; then
    cp "$HOME/.cache/huggingface/token" "$STAGING_DIR/.hf_token"
fi

echo "=== $(date) Staging dir: $STAGING_DIR ==="
echo "=== $(date) Submitting benchmark job to 8xH100 ==="
} >> "$LOGFILE" 2>&1

gpu-dev submit \
  --gpu-type h100 \
  --gpus 8 \
  --hours "$HOURS" \
  --runtime "$STAGING_DIR" \
  -- bash _remote_benchmark.sh
GPU_EXIT=$?

{
if [ "$GPU_EXIT" -ne 0 ]; then
    echo "=== $(date) gpu-dev submit failed with exit code $GPU_EXIT ==="
    rm -rf "$STAGING_DIR"
    exit "$GPU_EXIT"
fi

echo "=== $(date) Job complete, syncing results back ==="
rsync -a "$STAGING_DIR/results/" "$PROJECT_DIR/results/"

echo "=== $(date) Cleaning up staging dir ==="
rm -rf "$STAGING_DIR"

cd "$PROJECT_DIR"
git add results/
git commit -m "Benchmark run $(date +%Y%m%d_%H%M%S)"
git push
echo "=== $(date) Committed and pushed to main ==="
} >> "$LOGFILE" 2>&1

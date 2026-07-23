#!/bin/bash
set -euo pipefail
trap '' PIPE

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOURS=6
TIMEOUT=21600
mkdir -p "$PROJECT_DIR/logs"
LOGFILE="$PROJECT_DIR/logs/benchmark_$(date +%Y%m%d_%H%M%S).log"

echo "Logging to $LOGFILE"

{
echo "=== $(date) gpu-dev provided by the osdc fork built in the cron wrapper ==="

echo "=== $(date) Cleaning builds/ ==="
rm -rf "$PROJECT_DIR/builds"

if [ -f "$HOME/.cache/huggingface/token" ]; then
    cp "$HOME/.cache/huggingface/token" "$PROJECT_DIR/.hf_token"
fi
trap 'rm -f "$PROJECT_DIR/.hf_token"' EXIT

echo "=== $(date) Submitting benchmark job to 8xH100 (timeout=${TIMEOUT}s) ==="
} >> "$LOGFILE" 2>&1

# gpu-dev rsyncs the entire --runtime directory with no exclude support.
# .git/ (1.4GB) and results/ (2GB+) were breaking the SSH tunnel during
# upload. Stage only the files the remote needs (~600KB) in a temp dir.
STAGE_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGE_DIR"; rm -f "$PROJECT_DIR/.hf_token"' EXIT
rsync -a \
  --exclude='.git' \
  --exclude='results' \
  --exclude='logs' \
  --exclude='builds' \
  --exclude='.venv' \
  --exclude='__pycache__' \
  "$PROJECT_DIR/" "$STAGE_DIR/"

set +e
timeout "$TIMEOUT" gpu-dev submit \
  --gpu-type h100 \
  --gpus 8 \
  --hours "$HOURS" \
  --runtime "$STAGE_DIR" \
  -- bash _remote_benchmark.sh \
  >> "$LOGFILE" 2>&1
GPU_EXIT=$?
set -e

if [ -d "$STAGE_DIR/results" ]; then
    cp -a "$STAGE_DIR/results/." "$PROJECT_DIR/results/"
fi

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

echo "=== $(date) Regenerating progress plots locally ==="
cd "$PROJECT_DIR"
PYTHONPATH=. python3 scripts/plot_progress.py \
  results/v1/meta-llama--Meta-Llama-3.1-70B-Instruct/8xH100 2>&1 || true

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

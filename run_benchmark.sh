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

echo "=== $(date) Submitting results/v2 benchmark to 4xH100 (timeout=${TIMEOUT}s) ==="
} >> "$LOGFILE" 2>&1

# Scored results/v2 runs require a clean canonical Git checkout. A filtered
# sparse clone keeps that provenance while excluding the large results tree
# from gpu-dev's runtime upload.
STAGE_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGE_DIR"; rm -f "$PROJECT_DIR/.hf_token"' EXIT
git clone --quiet --depth 1 --filter=blob:none --sparse \
  https://github.com/bobrenjc93/inference-bench.git "$STAGE_DIR"
git -C "$STAGE_DIR" sparse-checkout set --no-cone '/*' '!/results/'
if [ -f "$PROJECT_DIR/.hf_token" ]; then
    cp "$PROJECT_DIR/.hf_token" "$STAGE_DIR/.hf_token"
fi

set +e
timeout "$TIMEOUT" gpu-dev submit \
  --gpu-type h100 \
  --gpus 4 \
  --hours "$HOURS" \
  --runtime "$STAGE_DIR" \
  -- bash _remote_benchmark.sh config_v3.yaml \
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

cd "$PROJECT_DIR"

(
    flock -w 300 9 || { echo "=== $(date) Could not acquire git lock ==="; exit 1; }
    git add results/
    git stash --include-untracked
    git pull --rebase
    git stash pop || true
    # Regenerate progress plots AFTER the rebase so they reflect the full run
    # set on main (including runs pushed concurrently by other runs), not just
    # the subset present in this clone. Generating before the pull leaves the
    # committed plot missing runs that landed while this run was executing.
    echo "=== $(date) Regenerating progress plots ==="
    PYTHONPATH=. python3 scripts/plot_progress.py \
      results/v2/meta-llama--Meta-Llama-3.1-70B-Instruct/4xH100 2>&1 || true
    git add results/
    git commit -m "Benchmark run $(date +%Y%m%d_%H%M%S)"
    git push
    echo "=== $(date) Committed and pushed to main ==="
) 9>"$PROJECT_DIR/.git-push.lock"
} >> "$LOGFILE" 2>&1

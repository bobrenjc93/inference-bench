#!/bin/bash
set -euo pipefail
trap '' PIPE

echo "=== Debug torchinferno server startup ==="
echo "Host: $(hostname)"
nvidia-smi -L

unset NCCL_SOCKET_IFNAME
export NCCL_SOCKET_IFNAME=eth0

if [ -f .hf_token ]; then
    export HF_TOKEN="$(cat .hf_token)"
    mkdir -p "$HOME/.cache/huggingface"
    cp .hf_token "$HOME/.cache/huggingface/token"
fi

# Handle both conda and Debian environments
if command -v conda &>/dev/null; then
    echo "Conda env"
    pip install -q openai httpx pyyaml tabulate
else
    echo "Debian env, creating venv"
    sudo apt-get update -qq && sudo apt-get install -y -qq python3-venv 2>/dev/null || true
    python3 -m venv --system-site-packages /tmp/bench-venv
    source /tmp/bench-venv/bin/activate
    pip install -q openai httpx pyyaml tabulate
fi

echo "=== Cloning and building torchinferno ==="
git clone https://github.com/bobrenjc93/TorchInferno.git builds/torchinferno 2>&1 | tail -1
cd builds/torchinferno
python3 -m venv --system-site-packages venv 2>/dev/null || python -m venv --system-site-packages venv
VENV_PY=venv/bin/python
$VENV_PY -m pip install -q --upgrade pip
$VENV_PY -m pip install -q -e ".[serve]" 2>&1 | tail -5
cd ../..

echo "=== Starting torchinferno server ==="
echo "Command: builds/torchinferno/venv/bin/python -m torchinferno.openai_server --model meta-llama/Meta-Llama-3.1-70B-Instruct --tensor-parallel-size 8 --port 8001 --trust-remote-code"

builds/torchinferno/venv/bin/python -m torchinferno.openai_server \
    --model meta-llama/Meta-Llama-3.1-70B-Instruct \
    --tensor-parallel-size 8 \
    --port 8001 \
    --trust-remote-code \
    > builds/torchinferno_server.log 2>&1 &
SERVER_PID=$!
echo "Server PID: $SERVER_PID"

echo "=== Waiting for health ==="
for i in $(seq 1 120); do
    if ! kill -0 $SERVER_PID 2>/dev/null; then
        echo "!!! SERVER CRASHED after $((i*5))s !!!"
        echo "=== FULL SERVER LOG ==="
        cat builds/torchinferno_server.log
        exit 1
    fi

    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8001/v1/models 2>/dev/null || echo "000")
    if [ "$STATUS" = "200" ]; then
        echo "Server ready after $((i*5))s"

        echo "=== Smoke test: single request ==="
        curl -s http://localhost:8001/v1/chat/completions \
            -H "Content-Type: application/json" \
            -d '{"model":"meta-llama/Meta-Llama-3.1-70B-Instruct","messages":[{"role":"user","content":"What is 2+2? Answer with just the number."}],"max_tokens":16}' 2>&1
        echo ""

        echo "=== Server log (last 30 lines) ==="
        tail -30 builds/torchinferno_server.log

        kill $SERVER_PID 2>/dev/null
        exit 0
    fi

    if [ $((i % 12)) -eq 0 ]; then
        echo "  Waiting... $((i*5))s. Log tail:"
        tail -3 builds/torchinferno_server.log 2>/dev/null
    fi
    sleep 5
done

echo "!!! SERVER TIMED OUT (600s) !!!"
echo "=== FULL SERVER LOG ==="
cat builds/torchinferno_server.log
kill $SERVER_PID 2>/dev/null
exit 1

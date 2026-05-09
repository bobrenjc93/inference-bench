#!/bin/bash
set -euo pipefail

echo "=== Remote benchmark starting ==="
echo "Host: $(hostname)"
echo "GPUs: $(nvidia-smi -L 2>/dev/null | wc -l)"
nvidia-smi

echo "=== Network interfaces ==="
ip -brief addr show | grep UP || true

# gpu-dev may inherit NCCL_SOCKET_IFNAME from the local
# machine, but the remote has different interface names.
unset NCCL_SOCKET_IFNAME
export NCCL_SOCKET_IFNAME=eth0

# HuggingFace token for gated model access (Llama etc.).
# run_benchmark.sh copies the token into .hf_token before syncing.
if [ -f .hf_token ]; then
    export HF_TOKEN="$(cat .hf_token)"
    mkdir -p "$HOME/.cache/huggingface"
    cp .hf_token "$HOME/.cache/huggingface/token"
    echo "HF token configured"
fi

echo "=== Installing system dependencies ==="
sudo apt-get update -qq && sudo apt-get install -y -qq \
  protobuf-compiler python3-venv libssl-dev pkg-config 2>/dev/null || true

# conda images may not have apt/sudo — install via conda instead
if command -v conda &>/dev/null; then
    conda install -y -c conda-forge pkg-config openssl protobuf 2>/dev/null || true
fi

# Install protoc from GitHub if not available via apt
if ! command -v protoc &>/dev/null; then
    echo "Installing protoc from GitHub release"
    PROTOC_VERSION="29.3"
    curl -sSL \
      "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip" \
      -o /tmp/protoc.zip
    mkdir -p /tmp/protoc
    unzip -q /tmp/protoc.zip -d /tmp/protoc
    export PATH="/tmp/protoc/bin:$PATH"
fi
echo "protoc: $(protoc --version)"

echo "=== Installing Rust (needed by sglang/outlines_core) ==="
if command -v rustc &>/dev/null; then
    echo "Rust already installed: $(rustc --version)"
else
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
fi
source "$HOME/.cargo/env" 2>/dev/null || true

echo "=== Setting up Python environment ==="
if command -v conda &>/dev/null; then
    echo "Conda detected, using conda python directly"
    pip install openai httpx pyyaml tabulate matplotlib
else
    echo "No conda, creating venv"
    python3 -m venv --system-site-packages /tmp/bench-venv
    source /tmp/bench-venv/bin/activate
    pip install openai httpx pyyaml tabulate matplotlib
fi

echo "=== Running full benchmark (clone + build + bench) ==="
python -m inference_bench --port 8001

echo "=== Benchmark complete ==="

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jun 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     380.2s (6.3m) | `ca2ea3d` |
| vllm         |     492.4s (8.2m) | `27da2a2` |
| sglang       | **261.6s (4.4m)** | `ed71fb8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     145.2 | **144.5** |
| TPOT median (ms)          |            - |  **46.2** |      75.8 |
| E2E median (ms)           |            - | **184.1** |     216.2 |
| Throughput median (tok/s) |            - |   **7.4** |       5.6 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-89117ee3/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 23:18:28] gpu-dev-89117ee3:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **197.8** |  216.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **217.7** |  366.0 |
| Throughput median (tok/s) |            - |   **4.6** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-89117ee3/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 23:18:28] gpu-dev-89117ee3:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **165.0** |  167.3 |
| TPOT median (ms)          |            - |  **51.4** |  101.4 |
| E2E median (ms)           |            - | **211.7** |  264.0 |
| Throughput median (tok/s) |            - |   **6.4** |    5.1 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-89117ee3/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 23:18:28] gpu-dev-89117ee3:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.5** |   80.7 |
| TPOT median (ms)          |            - | **28.7** |   55.8 |
| E2E median (ms)           |            - | **81.9** |  147.0 |
| Throughput median (tok/s) |            - | **14.9** |    9.5 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-89117ee3/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 23:18:28] gpu-dev-89117ee3:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.8 | **68.7** |
| TPOT median (ms)          |            - |  **14.8** |     22.7 |
| E2E median (ms)           |            - | **606.3** |    846.7 |
| Throughput median (tok/s) |            - |  **58.9** |     41.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-89117ee3/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 23:18:28] gpu-dev-89117ee3:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 23:18:28] gpu-dev-89117ee3:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.9** |  135.5 |
| TPOT median (ms)          |            - |  **28.2** |   51.2 |
| E2E median (ms)           |            - | **260.3** |  368.0 |
| Throughput median (tok/s) |            - |  **18.4** |   12.8 |
| Correctness               |            - |       98% |    99% |

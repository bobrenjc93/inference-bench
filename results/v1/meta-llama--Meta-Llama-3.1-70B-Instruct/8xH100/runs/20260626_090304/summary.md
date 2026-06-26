# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     459.7s (7.7m) | `ca2ea3d` |
| vllm         |     561.9s (9.4m) | `d980a3c` |
| sglang       | **283.8s (4.7m)** | `f5708c3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **144.8** |  153.8 |
| TPOT median (ms)          |            - |  **48.1** |   77.2 |
| E2E median (ms)           |            - | **190.4** |  225.7 |
| Throughput median (tok/s) |            - |   **7.5** |    5.4 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7eeaf8d4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     210.5 | **209.4** |
| TPOT median (ms)          |            - |       0.0 |       0.0 |
| E2E median (ms)           |            - | **263.0** |     352.9 |
| Throughput median (tok/s) |            - |   **3.8** |       2.8 |
| Correctness               |            - |      100% |      100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7eeaf8d4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     171.8 | **166.7** |
| TPOT median (ms)          |            - |  **58.7** |     101.1 |
| E2E median (ms)           |            - | **218.7** |     267.4 |
| Throughput median (tok/s) |            - |   **6.2** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7eeaf8d4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.8** |   83.7 |
| TPOT median (ms)          |            - | **29.7** |   45.0 |
| E2E median (ms)           |            - | **84.3** |  138.7 |
| Throughput median (tok/s) |            - | **14.2** |    9.8 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7eeaf8d4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      80.9 | **72.9** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **630.3** |    852.3 |
| Throughput median (tok/s) |            - |  **57.7** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7eeaf8d4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 09:20:28] gpu-dev-7eeaf8d4:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **134.0** |  137.3 |
| TPOT median (ms)          |            - |  **30.3** |   49.1 |
| E2E median (ms)           |            - | **277.3** |  367.4 |
| Throughput median (tok/s) |            - |  **17.9** |   12.9 |
| Correctness               |            - |       98% |    99% |

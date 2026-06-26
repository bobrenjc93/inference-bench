# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     437.3s (7.3m) | `ca2ea3d` |
| vllm         |     554.5s (9.2m) | `abc7154` |
| sglang       | **268.4s (4.5m)** | `8524678` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **139.4** |  144.6 |
| TPOT median (ms)          |            - |  **49.2** |   76.2 |
| E2E median (ms)           |            - | **184.5** |  214.4 |
| Throughput median (tok/s) |            - |   **7.7** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-a2711b44/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 15:20:36] gpu-dev-a2711b44:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **162.0** |  207.0 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **183.6** |  342.5 |
| Throughput median (tok/s) |            - |   **5.4** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-a2711b44/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 15:20:36] gpu-dev-a2711b44:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     161.9 | **154.9** |
| TPOT median (ms)          |            - |  **55.5** |     111.1 |
| E2E median (ms)           |            - | **206.4** |     265.1 |
| Throughput median (tok/s) |            - |   **6.6** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-a2711b44/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 15:20:36] gpu-dev-a2711b44:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.6** |   81.6 |
| TPOT median (ms)          |            - | **29.6** |   42.9 |
| E2E median (ms)           |            - | **80.5** |  135.0 |
| Throughput median (tok/s) |            - | **15.0** |   10.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-a2711b44/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 15:20:36] gpu-dev-a2711b44:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.3 | **71.6** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **603.3** |    845.5 |
| Throughput median (tok/s) |            - |  **58.5** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-a2711b44/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 15:20:36] gpu-dev-a2711b44:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 15:20:36] gpu-dev-a2711b44:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **119.7** |  131.9 |
| TPOT median (ms)          |            - |  **29.8** |   50.5 |
| E2E median (ms)           |            - | **251.6** |  360.5 |
| Throughput median (tok/s) |            - |  **18.7** |   13.3 |
| Correctness               |            - |       99% |    99% |

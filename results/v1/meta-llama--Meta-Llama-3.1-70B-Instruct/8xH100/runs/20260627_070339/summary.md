# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     407.7s (6.8m) | `231e91b` |
| vllm         |     500.1s (8.3m) | `091d139` |
| sglang       | **247.7s (4.1m)** | `e0c0c0a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     146.3 | **143.9** |
| TPOT median (ms)          |            - |  **50.5** |      79.8 |
| E2E median (ms)           |            - | **190.2** |     220.3 |
| Throughput median (tok/s) |            - |   **7.5** |       5.6 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-5e415bcd/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 527.2s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **207.6** |  228.5 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **235.4** |  374.4 |
| Throughput median (tok/s) |            - |   **4.2** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-5e415bcd/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 527.2s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **161.2** |  178.7 |
| TPOT median (ms)          |            - |  **54.9** |  106.7 |
| E2E median (ms)           |            - | **207.9** |  280.3 |
| Throughput median (tok/s) |            - |   **6.6** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-5e415bcd/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 527.2s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.7** |   83.0 |
| TPOT median (ms)          |            - | **31.0** |   59.6 |
| E2E median (ms)           |            - | **85.2** |  149.2 |
| Throughput median (tok/s) |            - | **14.2** |    9.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-5e415bcd/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 527.2s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **75.6** |   80.5 |
| TPOT median (ms)          |            - |  **14.8** |   22.4 |
| E2E median (ms)           |            - | **609.4** |  834.3 |
| Throughput median (tok/s) |            - |  **59.0** |   41.4 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-5e415bcd/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 07:15:40] gpu-dev-5e415bcd:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 527.2s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **130.5** |  142.9 |
| TPOT median (ms)          |            - |  **30.2** |   53.7 |
| E2E median (ms)           |            - | **265.6** |  371.7 |
| Throughput median (tok/s) |            - |  **18.3** |   12.8 |
| Correctness               |            - |       99% |    99% |

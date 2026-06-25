# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:04 PM PT, Jun 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     360.8s (6.0m) | `ca2ea3d` |
| vllm         |     508.8s (8.5m) | `e8e7b59` |
| sglang       | **267.6s (4.5m)** | `e6efe10` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **142.1** |  143.2 |
| TPOT median (ms)          |            - |  **48.0** |   74.0 |
| E2E median (ms)           |            - | **183.8** |  211.7 |
| Throughput median (tok/s) |            - |   **7.7** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-e1f20b22/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1804:1804 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1799:1799 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1798:1798 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1803:1803 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1800:1800 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1797:1797 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1801:1801 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1802:1802 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **206.0** |  212.4 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **232.4** |  371.7 |
| Throughput median (tok/s) |            - |   **4.3** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-e1f20b22/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1804:1804 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1799:1799 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1798:1798 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1803:1803 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1800:1800 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1797:1797 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1801:1801 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1802:1802 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **164.2** |  164.8 |
| TPOT median (ms)          |            - |  **52.1** |  105.0 |
| E2E median (ms)           |            - | **213.1** |  265.8 |
| Throughput median (tok/s) |            - |   **6.5** |    5.2 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-e1f20b22/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1804:1804 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1799:1799 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1798:1798 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1803:1803 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1800:1800 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1797:1797 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1801:1801 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1802:1802 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.7** |   82.6 |
| TPOT median (ms)          |            - | **29.1** |   46.3 |
| E2E median (ms)           |            - | **81.6** |  144.5 |
| Throughput median (tok/s) |            - | **15.2** |    9.7 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-e1f20b22/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1804:1804 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1799:1799 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1798:1798 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1803:1803 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1800:1800 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1797:1797 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1801:1801 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1802:1802 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.1 | **70.0** |
| TPOT median (ms)          |            - |  **14.8** |     22.3 |
| E2E median (ms)           |            - | **604.8** |    832.0 |
| Throughput median (tok/s) |            - |  **58.7** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-e1f20b22/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1804:1804 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1799:1799 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1798:1798 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1803:1803 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1800:1800 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1797:1797 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1801:1801 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 19:19:07] gpu-dev-e1f20b22:1802:1802 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **129.6** |  134.6 |
| TPOT median (ms)          |            - |  **28.8** |   49.5 |
| E2E median (ms)           |            - | **263.1** |  365.1 |
| Throughput median (tok/s) |            - |  **18.5** |   13.0 |
| Correctness               |            - |       99% |    98% |

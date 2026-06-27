# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jun 27 2026

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
| torchinferno |     390.8s (6.5m) | `231e91b` |
| vllm         |     542.1s (9.0m) | `867fd5e` |
| sglang       | **284.2s (4.7m)** | `3306233` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **125.0** |  158.9 |
| TPOT median (ms)          |            - |  **43.1** |   79.4 |
| E2E median (ms)           |            - | **158.5** |  236.4 |
| Throughput median (tok/s) |            - |   **8.2** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-8de2a5c5/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 533.2s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **190.7** |  219.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **214.1** |  374.3 |
| Throughput median (tok/s) |            - |   **4.7** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-8de2a5c5/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 533.2s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     168.1 | **166.9** |
| TPOT median (ms)          |            - |  **54.9** |     101.7 |
| E2E median (ms)           |            - | **213.2** |     266.6 |
| Throughput median (tok/s) |            - |   **6.4** |       5.1 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-8de2a5c5/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 533.2s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **63.0** |   85.9 |
| TPOT median (ms)          |            - | **31.8** |   33.3 |
| E2E median (ms)           |            - | **86.4** |  131.5 |
| Throughput median (tok/s) |            - | **14.1** |    9.9 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-8de2a5c5/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 533.2s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      73.4 | **69.0** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **621.6** |    838.0 |
| Throughput median (tok/s) |            - |  **58.8** |     41.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-8de2a5c5/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 11:15:45] gpu-dev-8de2a5c5:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 533.2s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.0** |  140.1 |
| TPOT median (ms)          |            - |  **28.9** |   47.3 |
| E2E median (ms)           |            - | **258.8** |  369.4 |
| Throughput median (tok/s) |            - |  **18.4** |   12.9 |
| Correctness               |            - |       99% |    99% |

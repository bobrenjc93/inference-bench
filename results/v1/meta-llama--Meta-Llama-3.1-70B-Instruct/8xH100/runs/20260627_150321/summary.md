# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 27 2026

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
| torchinferno |     413.2s (6.9m) | `231e91b` |
| vllm         |     529.0s (8.8m) | `51a9956` |
| sglang       | **245.7s (4.1m)** | `cfd911a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **148.8** |  151.3 |
| TPOT median (ms)          |            - |  **52.0** |   88.8 |
| E2E median (ms)           |            - | **195.9** |  230.3 |
| Throughput median (tok/s) |            - |   **7.2** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7bccba0e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 511.4s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **200.8** |  220.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **259.0** |  374.2 |
| Throughput median (tok/s) |            - |   **3.9** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7bccba0e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 511.4s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **165.2** |  170.8 |
| TPOT median (ms)          |            - |  **52.9** |  105.4 |
| E2E median (ms)           |            - | **210.8** |  280.3 |
| Throughput median (tok/s) |            - |   **6.4** |    4.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7bccba0e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 511.4s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **63.5** |   83.1 |
| TPOT median (ms)          |            - | **32.1** |   63.9 |
| E2E median (ms)           |            - | **86.4** |  153.0 |
| Throughput median (tok/s) |            - | **14.0** |    9.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7bccba0e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 511.4s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.7 | **71.7** |
| TPOT median (ms)          |            - |  **14.8** |     22.6 |
| E2E median (ms)           |            - | **597.3** |    881.7 |
| Throughput median (tok/s) |            - |  **59.3** |     41.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7bccba0e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 15:15:19] gpu-dev-7bccba0e:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 511.4s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **131.2** |  139.5 |
| TPOT median (ms)          |            - |  **30.4** |   56.2 |
| E2E median (ms)           |            - | **269.9** |  383.9 |
| Throughput median (tok/s) |            - |  **18.1** |   12.7 |
| Correctness               |            - |       98% |    98% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 25 2026

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
| torchinferno |     452.9s (7.5m) | `ca2ea3d` |
| vllm         |     533.4s (8.9m) | `cc79815` |
| sglang       | **265.4s (4.4m)** | `cfc0a0e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **141.7** |  152.1 |
| TPOT median (ms)          |            - |  **50.4** |   81.1 |
| E2E median (ms)           |            - | **188.5** |  226.2 |
| Throughput median (tok/s) |            - |   **7.4** |    5.4 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-32f801e4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 01:20:20] gpu-dev-32f801e4:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **185.8** |  220.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **208.6** |  398.4 |
| Throughput median (tok/s) |            - |   **4.8** |    2.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-32f801e4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 01:20:20] gpu-dev-32f801e4:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **160.6** |  165.7 |
| TPOT median (ms)          |            - |  **54.3** |  101.4 |
| E2E median (ms)           |            - | **199.5** |  264.1 |
| Throughput median (tok/s) |            - |   **6.5** |    5.1 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-32f801e4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 01:20:20] gpu-dev-32f801e4:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.8** |   83.6 |
| TPOT median (ms)          |            - | **29.2** |   48.9 |
| E2E median (ms)           |            - | **82.7** |  146.3 |
| Throughput median (tok/s) |            - | **15.0** |    9.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-32f801e4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 01:20:20] gpu-dev-32f801e4:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.9 | **75.6** |
| TPOT median (ms)          |            - |  **14.9** |     22.4 |
| E2E median (ms)           |            - | **610.2** |    842.8 |
| Throughput median (tok/s) |            - |  **58.3** |     41.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-32f801e4/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 01:20:20] gpu-dev-32f801e4:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 01:20:20] gpu-dev-32f801e4:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.8** |  139.6 |
| TPOT median (ms)          |            - |  **29.7** |   50.8 |
| E2E median (ms)           |            - | **257.9** |  375.6 |
| Throughput median (tok/s) |            - |  **18.4** |   12.7 |
| Correctness               |            - |       99% |    99% |

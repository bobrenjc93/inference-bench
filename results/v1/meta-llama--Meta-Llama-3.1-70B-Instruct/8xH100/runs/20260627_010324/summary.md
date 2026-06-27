# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 26 2026

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
| torchinferno |     459.4s (7.7m) | `a5c5be4` |
| vllm         |    621.4s (10.4m) | `af16446` |
| sglang       | **295.7s (4.9m)** | `09ca4fc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     152.0 | **148.5** |
| TPOT median (ms)          |            - |  **52.3** |      77.3 |
| E2E median (ms)           |            - | **199.6** |     224.5 |
| Throughput median (tok/s) |            - |   **7.2** |       5.4 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-31a05fef/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 01:16:57] gpu-dev-31a05fef:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 589.1s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **185.3** |  216.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **206.1** |  362.1 |
| Throughput median (tok/s) |            - |   **4.9** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-31a05fef/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 01:16:57] gpu-dev-31a05fef:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 589.1s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **162.3** |  162.3 |
| TPOT median (ms)          |            - |  **58.3** |  105.6 |
| E2E median (ms)           |            - | **211.7** |  260.2 |
| Throughput median (tok/s) |            - |   **6.4** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-31a05fef/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 01:16:57] gpu-dev-31a05fef:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 589.1s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.8** |   80.5 |
| TPOT median (ms)          |            - | **27.7** |   44.2 |
| E2E median (ms)           |            - | **80.0** |  140.1 |
| Throughput median (tok/s) |            - | **15.3** |   10.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-31a05fef/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 01:16:57] gpu-dev-31a05fef:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 589.1s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      72.0 | **67.4** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **612.3** |    839.6 |
| Throughput median (tok/s) |            - |  **59.1** |     41.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-31a05fef/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 01:16:57] gpu-dev-31a05fef:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 01:16:57] gpu-dev-31a05fef:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 589.1s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **126.1** |  135.0 |
| TPOT median (ms)          |            - |  **30.6** |   49.9 |
| E2E median (ms)           |            - | **261.9** |  365.3 |
| Throughput median (tok/s) |            - |  **18.6** |   13.0 |
| Correctness               |            - |       98% |    99% |

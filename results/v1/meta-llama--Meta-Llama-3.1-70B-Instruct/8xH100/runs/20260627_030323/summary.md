# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     450.2s (7.5m) | `231e91b` |
| vllm         |    653.9s (10.9m) | `ddd3855` |
| sglang       | **270.7s (4.5m)** | `09ca4fc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **137.4** |  144.3 |
| TPOT median (ms)          |            - |  **51.6** |   79.2 |
| E2E median (ms)           |            - | **185.2** |  216.9 |
| Throughput median (tok/s) |            - |   **7.7** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-63eff9e6/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 03:16:35] gpu-dev-63eff9e6:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 603.1s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **201.6** |  219.9 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **231.3** |  359.6 |
| Throughput median (tok/s) |            - |   **4.3** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-63eff9e6/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 03:16:35] gpu-dev-63eff9e6:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 603.1s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **164.0** |  165.2 |
| TPOT median (ms)          |            - |  **50.3** |  108.2 |
| E2E median (ms)           |            - | **210.2** |  272.7 |
| Throughput median (tok/s) |            - |   **6.5** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-63eff9e6/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 03:16:35] gpu-dev-63eff9e6:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 603.1s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.6** |   80.5 |
| TPOT median (ms)          |            - | **31.4** |   65.1 |
| E2E median (ms)           |            - | **85.2** |  156.6 |
| Throughput median (tok/s) |            - | **14.4** |    9.1 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-63eff9e6/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 03:16:35] gpu-dev-63eff9e6:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 603.1s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **76.4** |   78.4 |
| TPOT median (ms)          |            - |  **14.9** |   22.9 |
| E2E median (ms)           |            - | **620.9** |  840.8 |
| Throughput median (tok/s) |            - |  **58.8** |   40.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-63eff9e6/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=1 rank0_shard_scatter=1
[Llama3TP] loading initial embedding/norm/head tensors
NCCL version 2.29.7+cuda13.2

[2026-06-27 03:16:35] gpu-dev-63eff9e6:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-27 03:16:36] gpu-dev-63eff9e6:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
[Llama3TP] loaded initial embedding/norm/head tensors in 603.1s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.2** |  137.6 |
| TPOT median (ms)          |            - |  **29.7** |   55.1 |
| E2E median (ms)           |            - | **266.6** |  369.3 |
| Throughput median (tok/s) |            - |  **18.3** |   12.6 |
| Correctness               |            - |       98% |    98% |

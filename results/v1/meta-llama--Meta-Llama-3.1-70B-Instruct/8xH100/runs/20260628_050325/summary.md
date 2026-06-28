# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 PM PT, Jun 27 2026

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
| torchinferno |     423.9s (7.1m) | `1f52eaa` |
| vllm         |     490.0s (8.2m) | `a65f93f` |
| sglang       | **282.3s (4.7m)** | `ddc389c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **137.0** |  149.2 |
| TPOT median (ms)          |            - |  **52.4** |   73.6 |
| E2E median (ms)           |            - | **180.3** |  214.7 |
| Throughput median (tok/s) |            - |   **7.7** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-ff27ac67/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=0 rank0_shard_scatter=0
[Llama3TP] loading initial embedding/norm/head tensors
[Llama3TP] loaded initial embedding/norm/head tensors in 345.1s
[Llama3TP] loaded 10/80 layers in 537.8s
[Llama3TP] loaded 20/80 layers in 722.5s
[Llama3TP] loaded 30/80 layers in 887.4s
[Llama3TP] loaded 40/80 layers in 1040.0s
[Llama3TP] loaded 50/80 layers in 1197.0s
[Llama3TP] loaded 60/80 layers in 1391.9s
[Llama3TP] loaded 70/80 layers in 1582.4s
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **173.5** |  204.4 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **235.3** |  334.1 |
| Throughput median (tok/s) |            - |   **4.2** |    3.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-ff27ac67/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=0 rank0_shard_scatter=0
[Llama3TP] loading initial embedding/norm/head tensors
[Llama3TP] loaded initial embedding/norm/head tensors in 345.1s
[Llama3TP] loaded 10/80 layers in 537.8s
[Llama3TP] loaded 20/80 layers in 722.5s
[Llama3TP] loaded 30/80 layers in 887.4s
[Llama3TP] loaded 40/80 layers in 1040.0s
[Llama3TP] loaded 50/80 layers in 1197.0s
[Llama3TP] loaded 60/80 layers in 1391.9s
[Llama3TP] loaded 70/80 layers in 1582.4s
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **161.8** |  175.5 |
| TPOT median (ms)          |            - |  **60.7** |  100.9 |
| E2E median (ms)           |            - | **215.4** |  270.4 |
| Throughput median (tok/s) |            - |   **6.3** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-ff27ac67/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=0 rank0_shard_scatter=0
[Llama3TP] loading initial embedding/norm/head tensors
[Llama3TP] loaded initial embedding/norm/head tensors in 345.1s
[Llama3TP] loaded 10/80 layers in 537.8s
[Llama3TP] loaded 20/80 layers in 722.5s
[Llama3TP] loaded 30/80 layers in 887.4s
[Llama3TP] loaded 40/80 layers in 1040.0s
[Llama3TP] loaded 50/80 layers in 1197.0s
[Llama3TP] loaded 60/80 layers in 1391.9s
[Llama3TP] loaded 70/80 layers in 1582.4s
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.5** |   84.0 |
| TPOT median (ms)          |            - | **30.9** |   43.3 |
| E2E median (ms)           |            - | **85.5** |  144.9 |
| Throughput median (tok/s) |            - | **14.1** |    9.9 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-ff27ac67/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=0 rank0_shard_scatter=0
[Llama3TP] loading initial embedding/norm/head tensors
[Llama3TP] loaded initial embedding/norm/head tensors in 345.1s
[Llama3TP] loaded 10/80 layers in 537.8s
[Llama3TP] loaded 20/80 layers in 722.5s
[Llama3TP] loaded 30/80 layers in 887.4s
[Llama3TP] loaded 40/80 layers in 1040.0s
[Llama3TP] loaded 50/80 layers in 1197.0s
[Llama3TP] loaded 60/80 layers in 1391.9s
[Llama3TP] loaded 70/80 layers in 1582.4s
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.2 | **74.5** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **617.2** |    845.4 |
| Throughput median (tok/s) |            - |  **58.8** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-ff27ac67/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_replicated_broadcast=0 rank0_shard_scatter=0
[Llama3TP] loading initial embedding/norm/head tensors
[Llama3TP] loaded initial embedding/norm/head tensors in 345.1s
[Llama3TP] loaded 10/80 layers in 537.8s
[Llama3TP] loaded 20/80 layers in 722.5s
[Llama3TP] loaded 30/80 layers in 887.4s
[Llama3TP] loaded 40/80 layers in 1040.0s
[Llama3TP] loaded 50/80 layers in 1197.0s
[Llama3TP] loaded 60/80 layers in 1391.9s
[Llama3TP] loaded 70/80 layers in 1582.4s
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **122.2** |  137.5 |
| TPOT median (ms)          |            - |  **31.8** |   48.0 |
| E2E median (ms)           |            - | **266.7** |  361.9 |
| Throughput median (tok/s) |            - |  **18.2** |   13.1 |
| Correctness               |            - |       99% |    99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, Jun 26 2026

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
| torchinferno |     400.1s (6.7m) | `ca2ea3d` |
| vllm         |   1135.8s (18.9m) | `8e39424` |
| sglang       | **279.1s (4.7m)** | `b913480` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **146.0** |  149.0 |
| TPOT median (ms)          |            - |  **50.6** |   74.3 |
| E2E median (ms)           |            - | **189.2** |  219.0 |
| Throughput median (tok/s) |            - |   **7.4** |    5.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-10905350/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 13:20:12] gpu-dev-10905350:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **196.4** |  224.3 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **225.2** |  376.8 |
| Throughput median (tok/s) |            - |   **4.4** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-10905350/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 13:20:12] gpu-dev-10905350:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     161.2 | **159.5** |
| TPOT median (ms)          |            - |  **49.1** |     102.0 |
| E2E median (ms)           |            - | **206.3** |     256.9 |
| Throughput median (tok/s) |            - |   **6.6** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-10905350/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 13:20:12] gpu-dev-10905350:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.4** |   81.3 |
| TPOT median (ms)          |            - | **28.5** |   44.9 |
| E2E median (ms)           |            - | **80.3** |  130.9 |
| Throughput median (tok/s) |            - | **15.2** |   10.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-10905350/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 13:20:12] gpu-dev-10905350:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      74.2 | **71.5** |
| TPOT median (ms)          |            - |  **14.8** |     22.4 |
| E2E median (ms)           |            - | **620.1** |    861.2 |
| Throughput median (tok/s) |            - |  **58.8** |     41.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-10905350/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 13:20:12] gpu-dev-10905350:1797:1797 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1800:1800 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1798:1798 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1801:1801 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1795:1795 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1799:1799 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1796:1796 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 13:20:12] gpu-dev-10905350:1802:1802 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **127.2** |  137.1 |
| TPOT median (ms)          |            - |  **28.6** |   48.7 |
| E2E median (ms)           |            - | **264.2** |  369.0 |
| Throughput median (tok/s) |            - |  **18.5** |   13.0 |
| Correctness               |            - |       98% |    99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 26 2026

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
| torchinferno |     477.5s (8.0m) | `ca2ea3d` |
| vllm         |    600.6s (10.0m) | `d980a3c` |
| sglang       | **259.0s (4.3m)** | `b73e572` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **141.7** |  143.5 |
| TPOT median (ms)          |            - |  **47.7** |   77.5 |
| E2E median (ms)           |            - | **187.4** |  216.8 |
| Throughput median (tok/s) |            - |   **7.7** |    5.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7a7b47de/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **178.5** |  212.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **203.2** |  346.2 |
| Throughput median (tok/s) |            - |   **4.9** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7a7b47de/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **163.6** |  167.1 |
| TPOT median (ms)          |            - |  **57.7** |  107.2 |
| E2E median (ms)           |            - | **210.6** |  275.0 |
| Throughput median (tok/s) |            - |   **6.5** |    4.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7a7b47de/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.0** |   84.1 |
| TPOT median (ms)          |            - | **29.7** |   46.7 |
| E2E median (ms)           |            - | **80.1** |  139.4 |
| Throughput median (tok/s) |            - | **15.4** |    9.9 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7a7b47de/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      72.3 | **68.3** |
| TPOT median (ms)          |            - |  **14.9** |     22.3 |
| E2E median (ms)           |            - | **605.7** |    820.2 |
| Throughput median (tok/s) |            - |  **59.1** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-7a7b47de/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1802:1802 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1805:1805 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1804:1804 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1800:1800 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1798:1798 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:34] gpu-dev-7a7b47de:1799:1799 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1801:1801 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-26 11:20:35] gpu-dev-7a7b47de:1803:1803 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **122.8** |  135.0 |
| TPOT median (ms)          |            - |  **30.0** |   50.7 |
| E2E median (ms)           |            - | **257.4** |  359.5 |
| Throughput median (tok/s) |            - |  **18.7** |   13.1 |
| Correctness               |            - |       98% |    99% |

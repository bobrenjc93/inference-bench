# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jun 25 2026

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
| torchinferno |     375.4s (6.3m) | `ca2ea3d` |
| vllm         |     538.2s (9.0m) | `a2e8ec3` |
| sglang       | **278.8s (4.6m)** | `e4696ed` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **132.9** |  161.9 |
| TPOT median (ms)          |            - |  **50.1** |   90.3 |
| E2E median (ms)           |            - | **177.1** |  244.6 |
| Throughput median (tok/s) |            - |   **7.8** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-4e47a57e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **195.3** |  231.4 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **216.6** |  396.6 |
| Throughput median (tok/s) |            - |   **4.6** |    2.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-4e47a57e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **160.2** |  174.8 |
| TPOT median (ms)          |            - |  **48.3** |  104.9 |
| E2E median (ms)           |            - | **201.8** |  280.1 |
| Throughput median (tok/s) |            - |   **6.6** |    4.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-4e47a57e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.1** |   88.1 |
| TPOT median (ms)          |            - | **29.0** |   54.5 |
| E2E median (ms)           |            - | **79.9** |  156.3 |
| Throughput median (tok/s) |            - | **15.0** |    8.8 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-4e47a57e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **73.8** |   74.9 |
| TPOT median (ms)          |            - |  **14.8** |   22.1 |
| E2E median (ms)           |            - | **620.5** |  845.8 |
| Throughput median (tok/s) |            - |  **58.8** |   41.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
TorchInferno OpenAI server probing tensor-parallel symmetric-memory allreduce
TorchInferno OpenAI server symmetric-memory allreduce enabled after probe (runtime scope)
TorchInferno OpenAI server auto-launching tensor-parallel workers: /workspace/submit-4e47a57e/builds/torchinferno/venv/bin/python -m torch.distributed.run --standalone --nproc-per-node 8 -m torchinferno.openai_server --model /home/dev/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/1605565b47bb9346c5515c34102e054115b4f98b --tensor-parallel-size 8 --port 8001 --trust-remote-code
[Llama3TP] loading checkpoint tensors world_size=8 dtype=bfloat16 rank0_broadcast=0 rank0_shard_scatter=1
NCCL version 2.29.7+cuda13.2

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1801:1801 [5] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1800:1800 [4] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1799:1799 [3] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1797:1797 [1] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1798:1798 [2] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:15] gpu-dev-4e47a57e:1796:1796 [0] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1803:1803 [7] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.

[2026-06-25 21:18:16] gpu-dev-4e47a57e:1802:1802 [6] misc/ibvwrap.cc:173 NCCL WARN lib wrapper not initialized.
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.3** |  146.2 |
| TPOT median (ms)          |            - |  **28.4** |   54.3 |
| E2E median (ms)           |            - | **259.2** |  384.7 |
| Throughput median (tok/s) |            - |  **18.6** |   12.6 |
| Correctness               |            - |       99% |    99% |

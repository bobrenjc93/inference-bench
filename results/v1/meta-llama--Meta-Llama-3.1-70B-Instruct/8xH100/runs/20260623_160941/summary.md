# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jun 23 2026

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
| torchinferno |     485.3s (8.1m) | `7f1989f` |
| vllm         |    598.8s (10.0m) | `275b431` |
| sglang       | **304.2s (5.1m)** | `b5e0965` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **140.5** |  143.5 |
| TPOT median (ms)          |            - |  **46.4** |   81.5 |
| E2E median (ms)           |            - | **180.3** |  217.6 |
| Throughput median (tok/s) |            - |   **7.6** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
95 [0] NCCL INFO ncclCommInitRankConfig comm 0x5569b1095700 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5652ea01e0b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d0d4db5870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-5a74e586:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x5584f55fb130 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-5a74e586:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55df803be060 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.35, alloc 1.43, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
gpu-dev-5a74e586:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x555e9ec39bc0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-5a74e586:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55dbab907f20 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
000 commId 0xfcfc0f4035500669 - Init COMPLETE
2.11, bootstrap 0.14, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.35, alloc 1.32, bootstrap 0.93, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
gpu-dev-5a74e586:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.37, alloc gpu-dev-5a74e586:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.39, alloc gpu-dev-5a74e586:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.35, alloc 1.65, bootstrap 0.60, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
2.21, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
2.19, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.03)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **192.0** |  209.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **221.0** |  344.9 |
| Throughput median (tok/s) |            - |   **4.5** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
95 [0] NCCL INFO ncclCommInitRankConfig comm 0x5569b1095700 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5652ea01e0b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d0d4db5870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-5a74e586:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x5584f55fb130 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-5a74e586:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55df803be060 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.35, alloc 1.43, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
gpu-dev-5a74e586:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x555e9ec39bc0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-5a74e586:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55dbab907f20 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
000 commId 0xfcfc0f4035500669 - Init COMPLETE
2.11, bootstrap 0.14, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.35, alloc 1.32, bootstrap 0.93, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
gpu-dev-5a74e586:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.37, alloc gpu-dev-5a74e586:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.39, alloc gpu-dev-5a74e586:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.35, alloc 1.65, bootstrap 0.60, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
2.21, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
2.19, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.03)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **159.2** |  171.9 |
| TPOT median (ms)          |            - |  **49.3** |  104.9 |
| E2E median (ms)           |            - | **201.2** |  276.5 |
| Throughput median (tok/s) |            - |   **6.8** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
95 [0] NCCL INFO ncclCommInitRankConfig comm 0x5569b1095700 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5652ea01e0b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d0d4db5870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-5a74e586:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x5584f55fb130 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-5a74e586:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55df803be060 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.35, alloc 1.43, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
gpu-dev-5a74e586:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x555e9ec39bc0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-5a74e586:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55dbab907f20 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
000 commId 0xfcfc0f4035500669 - Init COMPLETE
2.11, bootstrap 0.14, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.35, alloc 1.32, bootstrap 0.93, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
gpu-dev-5a74e586:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.37, alloc gpu-dev-5a74e586:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.39, alloc gpu-dev-5a74e586:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.35, alloc 1.65, bootstrap 0.60, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
2.21, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
2.19, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.03)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.7** |   81.2 |
| TPOT median (ms)          |            - | **30.2** |   43.7 |
| E2E median (ms)           |            - | **81.8** |  128.4 |
| Throughput median (tok/s) |            - | **14.8** |   10.3 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
95 [0] NCCL INFO ncclCommInitRankConfig comm 0x5569b1095700 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5652ea01e0b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d0d4db5870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-5a74e586:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x5584f55fb130 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-5a74e586:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55df803be060 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.35, alloc 1.43, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
gpu-dev-5a74e586:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x555e9ec39bc0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-5a74e586:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55dbab907f20 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
000 commId 0xfcfc0f4035500669 - Init COMPLETE
2.11, bootstrap 0.14, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.35, alloc 1.32, bootstrap 0.93, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
gpu-dev-5a74e586:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.37, alloc gpu-dev-5a74e586:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.39, alloc gpu-dev-5a74e586:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.35, alloc 1.65, bootstrap 0.60, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
2.21, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
2.19, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.03)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **70.0** |   87.0 |
| TPOT median (ms)          |            - |  **14.9** |   22.3 |
| E2E median (ms)           |            - | **603.5** |  866.8 |
| Throughput median (tok/s) |            - |  **59.3** |   40.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
95 [0] NCCL INFO ncclCommInitRankConfig comm 0x5569b1095700 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5652ea01e0b0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55d0d4db5870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-5a74e586:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x5584f55fb130 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-5a74e586:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55df803be060 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.35, alloc 1.43, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.02)
gpu-dev-5a74e586:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x555e9ec39bc0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-5a74e586:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55dbab907f20 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
gpu-dev-5a74e586:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc 000 commId 0xfcfc0f4035500669 - Init COMPLETE
000 commId 0xfcfc0f4035500669 - Init COMPLETE
2.11, bootstrap 0.14, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
gpu-dev-5a74e586:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.35, alloc 1.32, bootstrap 0.93, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
gpu-dev-5a74e586:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.37, alloc gpu-dev-5a74e586:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.39, alloc gpu-dev-5a74e586:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.35, alloc 1.65, bootstrap 0.60, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.00)
2.21, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.01)
2.19, bootstrap 0.02, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.99, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.98, rest 0.03)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.3** |  138.5 |
| TPOT median (ms)          |            - |  **28.2** |   50.5 |
| E2E median (ms)           |            - | **257.6** |  366.8 |
| Throughput median (tok/s) |            - |  **18.6** |   12.9 |
| Correctness               |            - |       98% |    98% |

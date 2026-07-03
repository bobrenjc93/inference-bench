# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.6s (0.7m)** | `aca27e5` |
| vllm         |    274.4s (4.6m) | `979f551` |
| sglang       |    162.8s (2.7m) | `860244d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        153.4 | **143.5** |  143.8 |
| TPOT median (ms)          |     **51.5** |      52.5 |   78.1 |
| E2E median (ms)           |        198.7 | **187.7** |  220.7 |
| Throughput median (tok/s) |          6.3 |   **7.6** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **139.9** | 206.6 |  219.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **152.0** | 228.4 |  371.8 |
| Throughput median (tok/s) |      **6.6** |   4.4 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.9 |     171.2 | **156.9** |
| TPOT median (ms)          |         60.3 |  **58.4** |     111.3 |
| E2E median (ms)           |        353.1 | **222.3** |     263.7 |
| Throughput median (tok/s) |          4.1 |   **6.0** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        126.5 | **62.8** |   71.9 |
| TPOT median (ms)          |         36.5 | **30.4** |   60.8 |
| E2E median (ms)           |        151.5 | **86.9** |  143.4 |
| Throughput median (tok/s) |          8.5 | **14.0** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        265.6 |      75.3 | **73.5** |
| TPOT median (ms)          |         20.9 |  **15.1** |     22.2 |
| E2E median (ms)           |        958.2 | **612.0** |    849.6 |
| Throughput median (tok/s) |         36.1 |  **58.0** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.8 | **131.9** |  133.1 |
| TPOT median (ms)          |         33.8 |  **31.3** |   54.5 |
| E2E median (ms)           |        362.7 | **267.4** |  369.8 |
| Throughput median (tok/s) |         12.3 |  **18.0** |   12.9 |
| Correctness               |          98% |       99% |    98% |

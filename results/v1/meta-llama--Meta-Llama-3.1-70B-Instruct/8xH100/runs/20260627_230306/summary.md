# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     395.0s (6.6m) | `d3131f4` |
| vllm         |     508.9s (8.5m) | `9036c89` |
| sglang       | **254.7s (4.2m)** | `073de15` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        249.6 |     148.4 | **143.8** |
| TPOT median (ms)          |     **49.0** |      53.2 |      76.9 |
| E2E median (ms)           |        298.7 | **204.6** |     215.2 |
| Throughput median (tok/s) |          4.8 |   **7.3** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.9 | **197.2** |  207.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        303.1 | **281.2** |  340.2 |
| Throughput median (tok/s) |          3.3 |   **3.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        366.3 | **156.5** |  167.4 |
| TPOT median (ms)          |         60.2 |  **57.2** |  101.2 |
| E2E median (ms)           |        428.5 | **202.8** |  273.0 |
| Throughput median (tok/s) |          3.0 |   **6.7** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        262.1 | **59.3** |   84.0 |
| TPOT median (ms)          |         43.0 | **31.4** |   40.3 |
| E2E median (ms)           |        310.7 | **84.1** |  132.1 |
| Throughput median (tok/s) |          4.0 | **14.3** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        321.8 |      73.4 | **71.2** |
| TPOT median (ms)          |         21.5 |  **14.9** |     22.2 |
| E2E median (ms)           |       1127.0 | **608.7** |    832.5 |
| Throughput median (tok/s) |         33.1 |  **58.8** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.4 | **127.0** |  134.8 |
| TPOT median (ms)          |         34.8 |  **31.3** |   48.1 |
| E2E median (ms)           |        493.6 | **276.3** |  358.6 |
| Throughput median (tok/s) |          9.7 |  **18.1** |   13.1 |
| Correctness               |          99% |       98% |    98% |

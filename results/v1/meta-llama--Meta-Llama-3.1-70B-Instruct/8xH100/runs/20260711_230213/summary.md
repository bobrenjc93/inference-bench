# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.4s (0.6m)** | `312e29e` |
| vllm         |    346.8s (5.8m) | `1ef1c7e` |
| sglang       |    151.2s (2.5m) | `4884f6f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.8 | **68.4** |   81.6 |
| TPOT median (ms)          |     **32.5** |     37.4 |   60.9 |
| E2E median (ms)           |        166.6 | **95.3** |  135.5 |
| Throughput median (tok/s) |          7.0 | **14.0** |    9.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         72.9 | **69.8** |  117.0 |
| TPOT median (ms)          |          0.0 |      0.0 |    0.0 |
| E2E median (ms)           |         91.5 | **87.7** |  204.5 |
| Throughput median (tok/s) |         10.9 | **11.4** |    4.9 |
| Correctness               |         100% |     100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        193.5 |      94.8 | **82.2** |
| TPOT median (ms)          |     **36.0** |      58.6 |     86.0 |
| E2E median (ms)           |        222.6 | **133.2** |    150.1 |
| Throughput median (tok/s) |          5.0 |  **10.1** |      9.0 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.6 | **38.7** |   52.7 |
| TPOT median (ms)          |         35.2 | **29.9** |  419.2 |
| E2E median (ms)           |         75.6 | **59.4** |  492.3 |
| Throughput median (tok/s) |         19.4 | **21.6** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        183.0 |  **49.9** |   50.6 |
| TPOT median (ms)          |         19.2 |  **15.2** |   23.5 |
| E2E median (ms)           |        879.1 | **581.2** |  926.0 |
| Throughput median (tok/s) |         41.3 |  **61.3** |   41.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        129.0 |  **64.3** |   76.8 |
| TPOT median (ms)          |     **24.6** |      28.2 |  117.9 |
| E2E median (ms)           |        287.1 | **191.4** |  381.7 |
| Throughput median (tok/s) |         16.7 |  **23.7** |   13.5 |
| Correctness               |          99% |       98% |    99% |

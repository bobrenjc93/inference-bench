# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     332.9s (5.5m) | `9f91b40` |
| vllm         |   1283.7s (21.4m) | `694d9a8` |
| sglang       | **200.0s (3.3m)** | `88a37d7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.8 |     153.4 | **137.3** |
| TPOT median (ms)          |        148.7 |  **59.5** |      78.1 |
| E2E median (ms)           |        395.8 | **204.6** |     207.9 |
| Throughput median (tok/s) |          3.7 |   **7.2** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        270.1 |     202.6 | **201.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        294.4 | **261.6** |     337.6 |
| Throughput median (tok/s) |          3.4 |   **3.8** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        709.0 |     167.5 | **153.8** |
| TPOT median (ms)          |        110.8 |  **55.9** |     100.5 |
| E2E median (ms)           |        790.2 | **215.9** |     252.6 |
| Throughput median (tok/s) |          1.6 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.0 | **58.0** |   78.7 |
| TPOT median (ms)          |        129.0 | **26.6** |   58.4 |
| E2E median (ms)           |        456.6 | **77.9** |  142.3 |
| Throughput median (tok/s) |          2.8 | **15.9** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        639.3 |  **65.3** |   69.2 |
| TPOT median (ms)          |     **14.7** |      15.0 |   21.8 |
| E2E median (ms)           |       1294.4 | **598.5** |  805.0 |
| Throughput median (tok/s) |         27.5 |  **59.6** |   43.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        451.8 |     129.4 | **128.0** |
| TPOT median (ms)          |         80.7 |  **31.4** |      51.8 |
| E2E median (ms)           |        646.3 | **271.7** |     349.1 |
| Throughput median (tok/s) |          7.8 |  **18.6** |      13.4 |
| Correctness               |          99% |       99% |       99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:08 PM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     352.5s (5.9m) | `c837893` |
| vllm         |   1181.7s (19.7m) | `8474748` |
| sglang       | **188.9s (3.1m)** | `1f185c6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.5 |    163.1 | **134.9** |
| TPOT median (ms)          |        154.0 | **64.3** |      73.8 |
| E2E median (ms)           |        382.8 |    219.9 | **203.2** |
| Throughput median (tok/s) |          4.0 |  **6.5** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        287.5 | **189.6** |  210.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        313.9 | **208.7** |  347.7 |
| Throughput median (tok/s) |          3.2 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        547.7 |     167.5 | **149.4** |
| TPOT median (ms)          |        124.5 |  **58.7** |     105.0 |
| E2E median (ms)           |        673.3 | **216.7** |     247.2 |
| Throughput median (tok/s) |          1.9 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        371.4 | **56.6** |   73.3 |
| TPOT median (ms)          |        132.6 | **27.4** |   64.2 |
| E2E median (ms)           |        469.5 | **77.6** |  152.9 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        734.1 |  **64.9** |   66.8 |
| TPOT median (ms)          |         17.5 |  **14.9** |   22.4 |
| E2E median (ms)           |       1352.1 | **600.9** |  837.0 |
| Throughput median (tok/s) |         23.7 |  **60.1** |   42.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        445.8 |     128.3 | **127.0** |
| TPOT median (ms)          |         85.7 |  **33.1** |      53.1 |
| E2E median (ms)           |        638.3 | **264.8** |     357.6 |
| Throughput median (tok/s) |          7.2 |  **18.7** |      13.1 |
| Correctness               |          99% |       99% |       98% |

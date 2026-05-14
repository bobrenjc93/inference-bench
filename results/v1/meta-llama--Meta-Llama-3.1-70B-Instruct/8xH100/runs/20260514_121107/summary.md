# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:08 AM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     386.0s (6.4m) | `1582769` |
| vllm         |   1187.3s (19.8m) | `1ea9401` |
| sglang       | **162.4s (2.7m)** | `50f4058` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.6 |     153.0 | **134.9** |
| TPOT median (ms)          |        174.1 |  **57.8** |      73.2 |
| E2E median (ms)           |        415.0 | **200.8** |     201.2 |
| Throughput median (tok/s) |          3.6 |   **7.0** |       6.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        252.8 | **187.1** |  208.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        372.5 | **212.4** |  339.9 |
| Throughput median (tok/s) |          2.7 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        647.8 |     172.1 | **159.9** |
| TPOT median (ms)          |        242.8 |  **62.8** |     104.2 |
| E2E median (ms)           |        834.3 | **223.4** |     256.0 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        417.0 | **57.5** |   76.7 |
| TPOT median (ms)          |        255.8 | **26.7** |   62.0 |
| E2E median (ms)           |        639.4 | **78.2** |  149.9 |
| Throughput median (tok/s) |          2.2 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        824.3 |      71.9 | **65.3** |
| TPOT median (ms)          |         18.1 |  **15.0** |     21.9 |
| E2E median (ms)           |       1531.2 | **606.4** |    816.1 |
| Throughput median (tok/s) |         24.4 |  **59.0** |     43.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        486.1 | **128.3** |  129.1 |
| TPOT median (ms)          |        138.2 |  **32.5** |   52.3 |
| E2E median (ms)           |        758.5 | **264.2** |  352.6 |
| Throughput median (tok/s) |          6.9 |  **18.5** |   13.3 |
| Correctness               |          98% |       99% |    99% |

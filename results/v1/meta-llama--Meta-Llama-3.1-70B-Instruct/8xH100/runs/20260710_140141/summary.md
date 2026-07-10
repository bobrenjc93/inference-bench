# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:01 AM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.5s (0.1m)** | `adaa950` |
| vllm         |    82.9s (1.4m) | `85c09e9` |
| sglang       |   102.4s (1.7m) | `2286e25` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        174.0 |      69.6 | **63.8** |
| TPOT median (ms)          |     **34.5** |      39.9 |     89.2 |
| E2E median (ms)           |        203.4 | **100.0** |    129.9 |
| Throughput median (tok/s) |          5.7 |  **13.6** |     10.0 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        135.9 | **60.2** |  103.5 |
| TPOT median (ms)          |          0.0 |      0.0 |    0.0 |
| E2E median (ms)           |        136.1 | **75.4** |  186.0 |
| Throughput median (tok/s) |          7.3 | **13.3** |    5.4 |
| Correctness               |         100% |     100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm |   sglang |
| :------------------------ | -----------: | -------: | -------: |
| TTFT median (ms)          |        255.8 |     72.8 | **68.2** |
| TPOT median (ms)          |     **39.7** |     40.9 |    100.1 |
| E2E median (ms)           |        290.3 | **99.8** |    145.2 |
| Throughput median (tok/s) |          4.1 | **13.3** |      9.0 |
| Correctness               |          98% |      98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         61.7 | **37.9** |   38.2 |
| TPOT median (ms)          |         39.7 | **26.7** |  131.1 |
| E2E median (ms)           |         92.2 | **55.9** |  114.8 |
| Throughput median (tok/s) |         16.2 | **21.7** |   11.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        217.1 |      50.3 | **45.5** |
| TPOT median (ms)          |         21.7 |  **16.8** |     25.3 |
| E2E median (ms)           |       1011.7 | **640.2** |    909.2 |
| Throughput median (tok/s) |         35.7 |  **55.5** |     38.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        168.9 |  **58.2** |   63.8 |
| TPOT median (ms)          |         27.1 |  **24.9** |   69.1 |
| E2E median (ms)           |        346.7 | **194.3** |  297.0 |
| Throughput median (tok/s) |         13.8 |  **23.4** |   15.0 |
| Correctness               |          99% |       99% |    99% |

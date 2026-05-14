# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:06 PM PT, May 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     178.1s (3.0m) | `f2b87fd` |
| vllm         |   1079.3s (18.0m) | `bf0d2dc` |
| sglang       | **163.3s (2.7m)** | `85d9c77` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        308.4 |    163.5 | **136.8** |
| TPOT median (ms)          |        171.7 | **58.2** |      72.5 |
| E2E median (ms)           |        411.1 |    226.7 | **204.9** |
| Throughput median (tok/s) |          3.6 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        283.6 |     204.9 | **200.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        359.9 | **227.5** |     336.2 |
| Throughput median (tok/s) |          2.8 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        854.5 |     173.9 | **149.8** |
| TPOT median (ms)          |        174.4 |  **47.6** |     111.0 |
| E2E median (ms)           |        998.3 | **222.4** |     259.2 |
| Throughput median (tok/s) |          1.2 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        460.1 | **57.8** |   78.7 |
| TPOT median (ms)          |        215.7 | **26.6** |   40.8 |
| E2E median (ms)           |        669.8 | **77.8** |  133.9 |
| Throughput median (tok/s) |          2.1 | **15.5** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        757.9 |      68.5 | **64.2** |
| TPOT median (ms)          |         24.1 |  **15.0** |     22.5 |
| E2E median (ms)           |       1863.8 | **600.4** |    822.8 |
| Throughput median (tok/s) |         17.6 |  **59.0** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        532.9 |     133.7 | **126.0** |
| TPOT median (ms)          |        117.2 |  **29.5** |      49.4 |
| E2E median (ms)           |        860.6 | **271.0** |     351.4 |
| Throughput median (tok/s) |          5.5 |  **18.4** |      13.2 |
| Correctness               |          99% |       98% |       99% |

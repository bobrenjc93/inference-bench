# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     336.0s (5.6m) | `a7e5516` |
| vllm         |     450.3s (7.5m) | `2cac89f` |
| sglang       | **255.5s (4.3m)** | `7942d54` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm | sglang |
| :------------------------ | -----------: | ------: | -----: |
| TTFT median (ms)          |    **136.4** |   140.5 |  142.0 |
| TPOT median (ms)          |     **45.2** |    48.9 |   76.2 |
| E2E median (ms)           |    **179.4** |   183.2 |  213.0 |
| Throughput median (tok/s) |          6.6 | **7.7** |    5.7 |
| Correctness               |          98% |     98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        317.1 | **195.9** |  215.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        433.7 | **220.0** |  360.6 |
| Throughput median (tok/s) |          2.3 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        554.1 |     158.5 | **156.7** |
| TPOT median (ms)          |     **36.5** |      54.9 |     105.4 |
| E2E median (ms)           |        582.4 | **205.5** |     256.6 |
| Throughput median (tok/s) |          2.3 |   **6.6** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        218.0 | **59.1** |   91.8 |
| TPOT median (ms)          |         30.3 | **29.7** |   40.2 |
| E2E median (ms)           |        262.4 | **82.2** |  148.3 |
| Throughput median (tok/s) |          5.5 | **15.1** |    9.2 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        328.1 |      76.4 | **74.8** |
| TPOT median (ms)          |         21.1 |  **14.9** |     23.0 |
| E2E median (ms)           |       1157.3 | **627.5** |    868.7 |
| Throughput median (tok/s) |         32.2 |  **59.0** |     40.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        310.7 | **126.1** |  136.2 |
| TPOT median (ms)          |     **26.6** |      29.7 |   49.0 |
| E2E median (ms)           |        523.0 | **263.7** |  369.4 |
| Throughput median (tok/s) |          9.8 |  **18.6** |   12.7 |
| Correctness               |          99% |       98% |    99% |

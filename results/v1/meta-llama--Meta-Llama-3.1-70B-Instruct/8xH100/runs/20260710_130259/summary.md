# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.1s (0.7m)** | `a4d92f0` |
| vllm         |    365.6s (6.1m) | `fabec87` |
| sglang       |    205.1s (3.4m) | `e9493a0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        152.8 |      79.4 | **76.0** |
| TPOT median (ms)          |     **31.2** |      36.8 |     65.9 |
| E2E median (ms)           |        179.3 | **107.8** |    128.6 |
| Throughput median (tok/s) |          6.4 |  **12.1** |     10.5 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **51.4** | 75.5 |  118.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **52.1** | 92.2 |  193.4 |
| Throughput median (tok/s) |     **19.2** | 10.8 |    5.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        476.5 |      92.5 | **80.5** |
| TPOT median (ms)          |        125.9 |  **37.3** |     71.6 |
| E2E median (ms)           |        580.5 | **126.3** |    135.7 |
| Throughput median (tok/s) |          2.1 |  **10.5** |      9.3 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        133.2 | **35.0** |   49.4 |
| TPOT median (ms)          |         83.6 | **22.7** |  395.6 |
| E2E median (ms)           |        169.2 | **53.4** |  444.1 |
| Throughput median (tok/s) |          8.3 | **25.1** |    3.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        614.5 |  **46.0** |   49.1 |
| TPOT median (ms)          |         67.2 |  **15.1** |   24.7 |
| E2E median (ms)           |       2935.6 | **569.7** |  910.1 |
| Throughput median (tok/s) |         12.2 |  **61.8** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        285.7 |  **65.7** |   74.7 |
| TPOT median (ms)          |         61.6 |  **22.4** |  111.6 |
| E2E median (ms)           |        783.3 | **189.9** |  362.4 |
| Throughput median (tok/s) |          9.6 |  **24.1** |   13.5 |
| Correctness               |          98% |       98% |    99% |

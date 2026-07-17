# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **50.7s (0.8m)** | `96adc9d` |
| vllm         |    392.5s (6.5m) | `867ff69` |
| sglang       |    210.5s (3.5m) | `eaeb779` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.5 |  **77.4** |   78.6 |
| TPOT median (ms)          |     **31.6** |      36.1 |   65.0 |
| E2E median (ms)           |        164.7 | **105.7** |  131.9 |
| Throughput median (tok/s) |          7.0 |  **12.9** |   10.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **52.8** | 68.6 |  126.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **70.0** | 86.1 |  215.0 |
| Throughput median (tok/s) |     **14.3** | 11.6 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        192.9 |      83.0 | **81.4** |
| TPOT median (ms)          |     **35.7** |      40.4 |     80.8 |
| E2E median (ms)           |        221.2 | **116.1** |    142.7 |
| Throughput median (tok/s) |          5.2 |  **11.2** |      9.5 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.8 | **34.7** |   52.3 |
| TPOT median (ms)          |         34.7 | **22.6** |  399.6 |
| E2E median (ms)           |         73.1 | **52.6** |  442.1 |
| Throughput median (tok/s) |         19.4 | **24.9** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.3 |  **45.7** |   50.7 |
| TPOT median (ms)          |         19.3 |  **15.1** |   24.7 |
| E2E median (ms)           |        863.9 | **568.5** |  918.5 |
| Throughput median (tok/s) |         40.9 |  **61.7** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.9 |  **61.9** |   78.0 |
| TPOT median (ms)          |         24.3 |  **22.9** |  114.0 |
| E2E median (ms)           |        278.6 | **185.8** |  370.0 |
| Throughput median (tok/s) |         17.4 |  **24.4** |   13.4 |
| Correctness               |          99% |       98% |    99% |

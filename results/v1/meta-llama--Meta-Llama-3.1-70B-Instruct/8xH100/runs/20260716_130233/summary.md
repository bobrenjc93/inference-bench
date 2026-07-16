# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **50.0s (0.8m)** | `96adc9d` |
| vllm         |    261.2s (4.4m) | `b8168e3` |
| sglang       |    177.4s (3.0m) | `4ad418d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.2 | **71.7** |   79.9 |
| TPOT median (ms)          |     **32.0** |     36.7 |   69.8 |
| E2E median (ms)           |        165.2 | **96.0** |  136.4 |
| Throughput median (tok/s) |          6.9 | **13.9** |    9.8 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.7** | 73.5 |  126.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.7** | 90.5 |  209.0 |
| Throughput median (tok/s) |     **13.4** | 11.0 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        198.9 |  **77.3** |   84.8 |
| TPOT median (ms)          |     **35.3** |      37.4 |   75.6 |
| E2E median (ms)           |        228.6 | **106.7** |  145.1 |
| Throughput median (tok/s) |          5.1 |  **12.4** |    9.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.4 | **35.4** |   52.1 |
| TPOT median (ms)          |         35.0 | **23.2** |  447.5 |
| E2E median (ms)           |         74.2 | **54.0** |  417.8 |
| Throughput median (tok/s) |         19.2 | **24.1** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        183.4 |  **46.9** |   54.5 |
| TPOT median (ms)          |         19.3 |  **15.4** |   24.1 |
| E2E median (ms)           |        862.0 | **573.4** |  904.1 |
| Throughput median (tok/s) |         40.8 |  **60.3** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.7 |  **61.0** |   79.6 |
| TPOT median (ms)          |         24.3 |  **22.5** |  123.4 |
| E2E median (ms)           |        280.9 | **184.1** |  362.5 |
| Throughput median (tok/s) |         17.1 |  **24.4** |   13.4 |
| Correctness               |          99% |       99% |    99% |

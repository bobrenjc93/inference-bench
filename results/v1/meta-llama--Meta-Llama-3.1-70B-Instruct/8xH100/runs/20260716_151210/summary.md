# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:12 AM PT, Jul 16 2026

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
| torchinferno | **37.4s (0.6m)** | `96adc9d` |
| vllm         |    265.2s (4.4m) | `75bdad4` |
| sglang       |    170.0s (2.8m) | `4ad418d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.4 |  **77.3** |   79.3 |
| TPOT median (ms)          |     **30.7** |      37.6 |   65.2 |
| E2E median (ms)           |        165.4 | **106.7** |  133.9 |
| Throughput median (tok/s) |          6.9 |  **12.1** |   10.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **65.0** | 72.6 |  133.0 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **84.9** | 88.5 |  211.3 |
| Throughput median (tok/s) |     **11.8** | 11.3 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.7 |  **81.4** |   84.2 |
| TPOT median (ms)          |     **34.3** |      35.1 |   80.2 |
| E2E median (ms)           |        217.9 | **110.2** |  143.5 |
| Throughput median (tok/s) |          5.1 |  **12.2** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.5 | **35.1** |   52.7 |
| TPOT median (ms)          |         34.7 | **23.0** |  417.6 |
| E2E median (ms)           |         73.5 | **53.3** |  414.7 |
| Throughput median (tok/s) |         19.7 | **24.5** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.6 |  **45.9** |   51.7 |
| TPOT median (ms)          |         18.7 |  **15.3** |   25.1 |
| E2E median (ms)           |        829.2 | **578.2** |  964.2 |
| Throughput median (tok/s) |         41.9 |  **61.5** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.4 |  **62.4** |   80.2 |
| TPOT median (ms)          |         23.7 |  **22.2** |  117.6 |
| E2E median (ms)           |        274.2 | **187.4** |  373.5 |
| Throughput median (tok/s) |         17.1 |  **24.3** |   13.1 |
| Correctness               |          99% |       99% |    99% |

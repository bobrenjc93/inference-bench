# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, Jul 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.2s (0.7m)** | `96adc9d` |
| vllm         |    334.6s (5.6m) | `32e632d` |
| sglang       |    173.1s (2.9m) | `bdc9848` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        147.5 | **70.4** |   77.9 |
| TPOT median (ms)          |     **30.9** |     36.6 |   62.6 |
| E2E median (ms)           |        172.8 | **95.3** |  132.1 |
| Throughput median (tok/s) |          6.7 | **14.2** |   10.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.5** | 69.0 |  122.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **81.8** | 85.8 |  203.0 |
| Throughput median (tok/s) |     **12.2** | 11.7 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.8 |  **85.0** |   85.0 |
| TPOT median (ms)          |         34.2 |  **34.1** |   76.5 |
| E2E median (ms)           |        220.2 | **117.9** |  152.7 |
| Throughput median (tok/s) |          5.0 |  **12.3** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.9 | **34.9** |   51.3 |
| TPOT median (ms)          |         34.7 | **23.2** |  473.4 |
| E2E median (ms)           |         74.8 | **53.5** |  516.9 |
| Throughput median (tok/s) |         19.8 | **24.2** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.8 |  **47.5** |   50.9 |
| TPOT median (ms)          |         18.9 |  **15.6** |   24.6 |
| E2E median (ms)           |        867.1 | **581.3** |  939.8 |
| Throughput median (tok/s) |         41.0 |  **60.0** |   39.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        129.1 |  **61.4** |   77.5 |
| TPOT median (ms)          |         23.7 |  **21.9** |  127.4 |
| E2E median (ms)           |        283.3 | **186.8** |  388.9 |
| Throughput median (tok/s) |         17.0 |  **24.5** |   13.2 |
| Correctness               |          99% |       98% |    99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 15 2026

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
| torchinferno | **42.8s (0.7m)** | `96adc9d` |
| vllm         |    308.9s (5.1m) | `9dd2e72` |
| sglang       |    207.1s (3.5m) | `5af6702` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.0 |  **76.9** |   79.4 |
| TPOT median (ms)          |     **31.6** |      41.8 |   64.4 |
| E2E median (ms)           |        164.6 | **108.8** |  135.1 |
| Throughput median (tok/s) |          7.0 |  **12.2** |    9.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.4** | 69.4 |  122.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **72.9** | 86.3 |  206.2 |
| Throughput median (tok/s) |     **13.7** | 11.6 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.8 |  **79.6** |   84.0 |
| TPOT median (ms)          |         34.9 |  **34.4** |   78.5 |
| E2E median (ms)           |        217.6 | **108.0** |  152.1 |
| Throughput median (tok/s) |          5.2 |  **12.6** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.9 | **37.1** |   51.8 |
| TPOT median (ms)          |         35.0 | **26.9** |  394.3 |
| E2E median (ms)           |         76.9 | **56.1** |  438.3 |
| Throughput median (tok/s) |         19.3 | **23.1** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.4 |  **46.5** |   51.7 |
| TPOT median (ms)          |         19.1 |  **15.4** |   25.3 |
| E2E median (ms)           |        865.6 | **577.9** |  905.9 |
| Throughput median (tok/s) |         41.4 |  **60.2** |   38.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.3 |  **61.9** |   77.9 |
| TPOT median (ms)          |         24.1 |  **23.7** |  112.5 |
| E2E median (ms)           |        279.5 | **187.4** |  367.5 |
| Throughput median (tok/s) |         17.3 |  **23.9** |   13.0 |
| Correctness               |          99% |       99% |    99% |

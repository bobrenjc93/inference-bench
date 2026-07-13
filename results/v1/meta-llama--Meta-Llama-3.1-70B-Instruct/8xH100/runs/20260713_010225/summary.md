# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 12 2026

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
| torchinferno | **42.6s (0.7m)** | `96adc9d` |
| vllm         |    212.7s (3.5m) | `4c81772` |
| sglang       |    156.0s (2.6m) | `80965db` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.7 |  **71.1** |   77.4 |
| TPOT median (ms)          |     **32.2** |      38.6 |   65.6 |
| E2E median (ms)           |        166.3 | **100.6** |  134.6 |
| Throughput median (tok/s) |          7.0 |  **12.7** |   10.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **64.7** |  78.5 |  123.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **84.2** | 100.9 |  206.0 |
| Throughput median (tok/s) |     **11.9** |   9.9 |    4.9 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.0 |  **77.8** |   84.4 |
| TPOT median (ms)          |         34.5 |  **34.1** |   80.3 |
| E2E median (ms)           |        217.9 | **104.4** |  146.7 |
| Throughput median (tok/s) |          5.1 |  **12.6** |    9.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.9 | **37.3** |   51.4 |
| TPOT median (ms)          |         35.1 | **27.3** |  430.8 |
| E2E median (ms)           |         76.1 | **56.0** |  447.6 |
| Throughput median (tok/s) |         19.6 | **22.6** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.3 |  **47.1** |   51.0 |
| TPOT median (ms)          |         19.3 |  **15.6** |   24.6 |
| E2E median (ms)           |        842.7 | **584.7** |  919.0 |
| Throughput median (tok/s) |         40.9 |  **59.9** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.1 |  **62.3** |   77.6 |
| TPOT median (ms)          |         24.2 |  **23.1** |  120.3 |
| E2E median (ms)           |        277.4 | **189.3** |  370.8 |
| Throughput median (tok/s) |         16.9 |  **23.5** |   13.3 |
| Correctness               |          99% |       98% |    99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:42 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `8546437` |
| vllm         |    86.2s (1.4m) | `1cd3e0e` |
| sglang       |     9.0s (0.2m) | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        157.9 |   158.8 | **149.3** |
| TPOT median (ms)          |     **53.0** |    60.6 |      80.2 |
| E2E median (ms)           |    **202.3** |   209.9 |     225.9 |
| Throughput median (tok/s) |          5.8 | **6.8** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        277.6 | **196.8** |  213.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        393.2 | **278.5** |  420.6 |
| Throughput median (tok/s) |          2.5 |   **3.6** |    2.4 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        431.6 |     192.8 | **184.8** |
| TPOT median (ms)          |         71.7 |  **63.8** |     113.8 |
| E2E median (ms)           |        509.0 | **247.8** |     310.5 |
| Throughput median (tok/s) |          2.3 |   **5.4** |       4.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        269.3 | **72.0** |   76.7 |
| TPOT median (ms)          |         52.0 | **35.7** |   89.5 |
| E2E median (ms)           |        314.1 | **98.9** |  177.2 |
| Throughput median (tok/s) |          4.3 | **12.1** |    8.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        418.2 |  **78.9** |   96.1 |
| TPOT median (ms)          |         25.4 |  **18.9** |   26.3 |
| E2E median (ms)           |       1480.2 | **769.2** | 1072.4 |
| Throughput median (tok/s) |         25.5 |  **47.0** |   34.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        310.9 | **139.8** |  144.1 |
| TPOT median (ms)          |         40.4 |  **35.8** |   62.0 |
| E2E median (ms)           |        579.7 | **320.8** |  441.3 |
| Throughput median (tok/s) |          8.1 |  **15.0** |   11.0 |
| Correctness               |          98% |       99% |    99% |

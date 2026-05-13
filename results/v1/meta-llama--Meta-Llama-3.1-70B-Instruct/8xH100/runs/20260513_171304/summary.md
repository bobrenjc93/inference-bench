# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:08 AM PT, May 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     171.6s (2.9m) | `8684859` |
| vllm         |   1105.0s (18.4m) | `e35c0d4` |
| sglang       | **158.4s (2.6m)** | `ff70aea` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        323.5 |     155.6 | **139.1** |
| TPOT median (ms)          |        269.8 |  **49.3** |      74.4 |
| E2E median (ms)           |        563.4 | **205.9** |     206.2 |
| Throughput median (tok/s) |          2.7 |   **7.0** |       6.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        458.0 | **199.9** |  212.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        524.4 | **223.8** |  351.9 |
| Throughput median (tok/s) |          1.9 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        890.6 |     170.3 | **154.8** |
| TPOT median (ms)          |        211.9 |  **70.2** |     105.7 |
| E2E median (ms)           |       1067.3 | **235.7** |     252.0 |
| Throughput median (tok/s) |          1.2 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        459.5 | **57.8** |   73.8 |
| TPOT median (ms)          |        249.1 | **26.9** |   50.7 |
| E2E median (ms)           |        678.0 | **77.6** |  130.1 |
| Throughput median (tok/s) |          2.2 | **15.5** |   10.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      73.6 | **69.6** |
| TPOT median (ms)          |            - |  **14.9** |     22.0 |
| E2E median (ms)           |            - | **608.0** |    830.5 |
| Throughput median (tok/s) |            - |  **59.0** |     42.6 |
| Correctness               |            - |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        532.9 |     131.4 | **129.9** |
| TPOT median (ms)          |        182.7 |  **32.3** |      50.6 |
| E2E median (ms)           |        708.3 | **270.2** |     354.1 |
| Throughput median (tok/s) |          2.0 |  **18.4** |      13.4 |
| Correctness               |          98% |       99% |       98% |

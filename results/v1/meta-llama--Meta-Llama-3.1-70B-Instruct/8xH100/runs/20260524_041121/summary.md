# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          1/4 |   **2/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     351.2s (5.9m) | `9f91b40` |
| vllm         |   1309.6s (21.8m) | `33d7cbe` |
| sglang       | **195.7s (3.3m)** | `d6d9f12` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        270.4 |     158.5 | **141.2** |
| TPOT median (ms)          |        155.3 |  **54.4** |      77.7 |
| E2E median (ms)           |        366.4 | **210.9** |     213.4 |
| Throughput median (tok/s) |          4.0 |   **7.1** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |    **186.0** |     205.2 |  194.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        315.4 | **233.0** |  326.2 |
| Throughput median (tok/s) |          3.2 |   **4.3** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        649.7 |     173.5 | **154.0** |
| TPOT median (ms)          |         99.9 |  **63.4** |     105.3 |
| E2E median (ms)           |        746.8 | **228.1** |     256.7 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        312.0 | **57.6** |   73.7 |
| TPOT median (ms)          |        133.6 | **27.0** |   65.9 |
| E2E median (ms)           |        411.7 | **77.9** |  144.9 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.6 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        797.0 |  **66.5** |   67.5 |
| TPOT median (ms)          |         15.9 |  **15.0** |   22.6 |
| E2E median (ms)           |       1442.8 | **605.5** |  830.6 |
| Throughput median (tok/s) |         25.0 |  **59.5** |   41.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        443.0 |     132.3 | **126.2** |
| TPOT median (ms)          |         80.9 |  **32.0** |      54.3 |
| E2E median (ms)           |        656.6 | **271.1** |     354.4 |
| Throughput median (tok/s) |          7.4 |  **18.6** |      13.0 |
| Correctness               |          98% |       98% |       99% |

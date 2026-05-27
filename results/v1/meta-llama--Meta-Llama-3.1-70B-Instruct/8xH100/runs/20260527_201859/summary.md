# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:07 PM PT, May 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     368.1s (6.1m) | `21f4719` |
| vllm         |   1394.2s (23.2m) | `206b72c` |
| sglang       | **194.8s (3.2m)** | `14f81a6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        254.7 |     162.5 | **146.8** |
| TPOT median (ms)          |         61.1 |  **59.5** |      74.9 |
| E2E median (ms)           |        317.7 | **214.0** |     216.6 |
| Throughput median (tok/s) |          4.2 |   **6.7** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        282.2 |     205.5 | **202.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        323.0 | **228.8** |     342.3 |
| Throughput median (tok/s) |          3.1 |   **4.4** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.6 |     173.4 | **162.9** |
| TPOT median (ms)          |     **56.7** |      61.1 |     100.6 |
| E2E median (ms)           |        795.6 | **228.7** |     265.6 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        163.5 | **60.3** |   78.9 |
| TPOT median (ms)          |         29.6 | **27.4** |   62.8 |
| E2E median (ms)           |        189.9 | **80.8** |  144.6 |
| Throughput median (tok/s) |          6.5 | **15.1** |    9.4 |
| Correctness               |          96% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        648.2 |  **70.1** |   77.7 |
| TPOT median (ms)          |     **14.8** |      15.1 |   23.8 |
| E2E median (ms)           |       1205.1 | **612.7** |  902.3 |
| Throughput median (tok/s) |         27.1 |  **58.9** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        416.4 |     134.4 | **133.7** |
| TPOT median (ms)          |     **32.5** |      32.6 |      52.4 |
| E2E median (ms)           |        566.3 | **273.0** |     374.3 |
| Throughput median (tok/s) |          8.5 |  **18.2** |      12.4 |
| Correctness               |          98% |       98% |       99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:06 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     333.4s (5.6m) | `07a120b` |
| vllm         |    958.1s (16.0m) | `630492d` |
| sglang       | **156.4s (2.6m)** | `0f3932c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        388.3 |    157.4 | **139.9** |
| TPOT median (ms)          |        452.3 | **56.2** |      74.6 |
| E2E median (ms)           |        845.9 |    213.4 | **207.7** |
| Throughput median (tok/s) |          1.6 |  **7.1** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        655.2 | **194.6** |  212.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        817.9 | **222.2** |  356.6 |
| Throughput median (tok/s) |          1.2 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        710.9 |     170.9 | **155.5** |
| TPOT median (ms)          |        563.6 |  **61.2** |      95.3 |
| E2E median (ms)           |       1296.8 | **223.9** |     249.8 |
| Throughput median (tok/s) |          1.1 |   **6.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        424.7 | **58.1** |   75.8 |
| TPOT median (ms)          |        354.3 | **27.5** |   55.0 |
| E2E median (ms)           |        783.3 | **79.1** |  138.4 |
| Throughput median (tok/s) |          1.8 | **15.4** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        580.9 |      70.5 | **68.7** |
| TPOT median (ms)          |         33.7 |  **15.0** |     21.9 |
| E2E median (ms)           |       1905.5 | **612.9** |    830.6 |
| Throughput median (tok/s) |         20.2 |  **58.9** |     43.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        552.0 | **130.3** |  130.4 |
| TPOT median (ms)          |        280.8 |  **32.0** |   49.4 |
| E2E median (ms)           |       1129.9 | **270.3** |  356.6 |
| Throughput median (tok/s) |          5.2 |  **18.4** |   13.4 |
| Correctness               |          98% |       99% |    99% |

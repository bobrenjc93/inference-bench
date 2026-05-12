# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:06 AM PT, May 12 2026

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
| torchinferno |     270.4s (4.5m) | `bc43c69` |
| vllm         |    968.4s (16.1m) | `6427603` |
| sglang       | **156.7s (2.6m)** | `6be1a45` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        506.3 |    166.5 | **134.3** |
| TPOT median (ms)          |        460.6 | **61.0** |      77.5 |
| E2E median (ms)           |        833.7 |    223.8 | **204.1** |
| Throughput median (tok/s) |          1.7 |  **6.7** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        339.0 | **198.0** |  212.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        384.2 | **218.6** |  354.3 |
| Throughput median (tok/s) |          2.6 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        601.6 |     159.2 | **154.5** |
| TPOT median (ms)          |        199.6 |  **49.4** |      95.7 |
| E2E median (ms)           |        773.0 | **201.9** |     255.4 |
| Throughput median (tok/s) |          1.7 |   **6.8** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        400.4 | **58.5** |   77.9 |
| TPOT median (ms)          |        464.1 | **27.2** |   56.2 |
| E2E median (ms)           |        782.9 | **79.6** |  155.6 |
| Throughput median (tok/s) |          1.9 | **15.5** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        546.2 |      68.5 | **66.4** |
| TPOT median (ms)          |         30.8 |  **15.0** |     22.0 |
| E2E median (ms)           |       1813.9 | **607.5** |    837.6 |
| Throughput median (tok/s) |         21.7 |  **58.8** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        478.7 |     130.1 | **129.2** |
| TPOT median (ms)          |        231.0 |  **30.5** |      50.3 |
| E2E median (ms)           |        917.5 | **266.3** |     361.4 |
| Throughput median (tok/s) |          5.9 |  **18.5** |      13.2 |
| Correctness               |          99% |       98% |       98% |

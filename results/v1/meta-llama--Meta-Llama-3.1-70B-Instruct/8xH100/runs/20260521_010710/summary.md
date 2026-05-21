# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 PM PT, May 20 2026

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
| torchinferno |     340.6s (5.7m) | `9f91b40` |
| vllm         |   1182.4s (19.7m) | `bde560e` |
| sglang       | **191.8s (3.2m)** | `f9f82d2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        295.5 |    162.2 | **144.0** |
| TPOT median (ms)          |        152.8 | **58.3** |      71.5 |
| E2E median (ms)           |        403.6 |    223.6 | **211.4** |
| Throughput median (tok/s) |          3.5 |  **6.7** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.9 | **187.6** |  198.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        309.8 | **207.4** |  337.0 |
| Throughput median (tok/s) |          3.2 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        680.6 |     166.8 | **161.9** |
| TPOT median (ms)          |         95.8 |  **63.4** |      98.8 |
| E2E median (ms)           |        799.0 | **215.7** |     256.2 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        364.0 | **58.1** |   76.3 |
| TPOT median (ms)          |        131.3 | **26.7** |   65.7 |
| E2E median (ms)           |        473.9 | **78.8** |  155.7 |
| Throughput median (tok/s) |          2.9 | **15.6** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        838.7 |      73.6 | **67.2** |
| TPOT median (ms)          |         15.8 |  **15.0** |     22.0 |
| E2E median (ms)           |       1413.3 | **616.0** |    833.6 |
| Throughput median (tok/s) |         24.2 |  **58.7** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        490.7 |     129.7 | **129.5** |
| TPOT median (ms)          |         79.1 |  **32.7** |      51.6 |
| E2E median (ms)           |        679.9 | **268.3** |     358.8 |
| Throughput median (tok/s) |          7.1 |  **18.4** |      13.2 |
| Correctness               |          98% |       99% |       99% |

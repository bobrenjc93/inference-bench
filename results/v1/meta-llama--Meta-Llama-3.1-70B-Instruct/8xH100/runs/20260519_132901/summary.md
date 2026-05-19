# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:02 AM PT, May 19 2026

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
| torchinferno |     365.2s (6.1m) | `9f91b40` |
| vllm         |   2313.6s (38.6m) | `a78b842` |
| sglang       | **172.5s (2.9m)** | `de3fc46` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        258.1 |    160.5 | **136.0** |
| TPOT median (ms)          |        152.4 | **61.7** |      74.7 |
| E2E median (ms)           |        359.3 |    218.5 | **204.8** |
| Throughput median (tok/s) |          4.1 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        233.3 | **186.2** |  206.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        303.1 | **209.1** |  339.3 |
| Throughput median (tok/s) |          3.3 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        557.4 |     176.8 | **159.2** |
| TPOT median (ms)          |        148.1 |  **65.8** |      91.3 |
| E2E median (ms)           |        652.4 | **239.5** |     256.3 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        306.3 | **57.5** |   79.5 |
| TPOT median (ms)          |        130.7 | **26.6** |   63.5 |
| E2E median (ms)           |        406.4 | **78.0** |  156.6 |
| Throughput median (tok/s) |          3.6 | **15.9** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        702.2 |      72.3 | **64.4** |
| TPOT median (ms)          |         15.6 |  **14.9** |     22.3 |
| E2E median (ms)           |       1301.7 | **613.8** |    826.4 |
| Throughput median (tok/s) |         26.7 |  **58.4** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        411.5 |     130.7 | **129.0** |
| TPOT median (ms)          |         89.4 |  **33.8** |      50.4 |
| E2E median (ms)           |        604.6 | **271.8** |     356.7 |
| Throughput median (tok/s) |          8.0 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:10 AM PT, May 18 2026

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
| torchinferno |     315.0s (5.2m) | `c837893` |
| vllm         |   1130.2s (18.8m) | `1ac10f1` |
| sglang       | **169.9s (2.8m)** | `0ab427d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        285.3 |    159.0 | **137.7** |
| TPOT median (ms)          |        154.6 | **56.3** |      77.0 |
| E2E median (ms)           |        376.2 |    212.7 | **207.8** |
| Throughput median (tok/s) |          4.0 |  **6.9** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.1 | **196.9** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        294.4 | **218.8** |  342.3 |
| Throughput median (tok/s) |          3.4 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        511.8 |     172.8 | **157.5** |
| TPOT median (ms)          |        108.5 |  **60.1** |      99.0 |
| E2E median (ms)           |        603.8 | **223.1** |     258.8 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        368.1 | **58.0** |   76.4 |
| TPOT median (ms)          |        132.5 | **27.0** |   67.5 |
| E2E median (ms)           |        467.0 | **78.4** |  153.5 |
| Throughput median (tok/s) |          3.0 | **15.4** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        694.8 |      69.7 | **67.7** |
| TPOT median (ms)          |         15.3 |  **15.0** |     22.4 |
| E2E median (ms)           |       1386.5 | **609.5** |    841.8 |
| Throughput median (tok/s) |         27.7 |  **58.7** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        426.8 |     131.3 | **129.1** |
| TPOT median (ms)          |         82.2 |  **31.7** |      53.2 |
| E2E median (ms)           |        625.6 | **268.5** |     360.8 |
| Throughput median (tok/s) |          8.0 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       99% |

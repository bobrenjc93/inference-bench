# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, Jun 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     399.8s (6.7m) | `a80b89c` |
| vllm         |   1323.9s (22.1m) | `ba94a3b` |
| sglang       | **186.5s (3.1m)** | `fca4ef9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        351.1 |    165.7 | **147.5** |
| TPOT median (ms)          |         86.1 | **57.1** |      77.0 |
| E2E median (ms)           |        419.3 |    223.1 | **221.0** |
| Throughput median (tok/s) |          3.0 |  **6.9** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        394.4 | **194.6** |  210.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        550.2 | **261.5** |  350.3 |
| Throughput median (tok/s) |          1.8 |   **3.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        787.0 |     180.8 | **164.7** |
| TPOT median (ms)          |     **65.1** |      66.3 |      98.0 |
| E2E median (ms)           |        843.7 | **244.1** |     259.7 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        473.1 | **63.7** |   79.0 |
| TPOT median (ms)          |         60.8 | **28.5** |   49.3 |
| E2E median (ms)           |        536.3 | **85.9** |  143.1 |
| Throughput median (tok/s) |          2.5 | **13.9** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        497.3 |  **70.0** |   81.3 |
| TPOT median (ms)          |         22.2 |  **15.0** |   22.8 |
| E2E median (ms)           |       1261.3 | **602.9** |  871.0 |
| Throughput median (tok/s) |         27.0 |  **58.8** |   40.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        500.6 | **134.9** |  136.6 |
| TPOT median (ms)          |         46.8 |  **33.4** |   49.4 |
| E2E median (ms)           |        722.2 | **283.5** |  369.0 |
| Throughput median (tok/s) |          7.2 |  **17.9** |   12.7 |
| Correctness               |          98% |       98% |    99% |

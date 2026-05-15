# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:07 PM PT, May 15 2026

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
| torchinferno |     388.9s (6.5m) | `cbfd345` |
| vllm         |   1112.1s (18.5m) | `1ccdf87` |
| sglang       | **167.6s (2.8m)** | `3c2956d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        283.7 |    163.6 | **136.9** |
| TPOT median (ms)          |        149.1 | **55.5** |      75.7 |
| E2E median (ms)           |        368.6 |    213.0 | **206.7** |
| Throughput median (tok/s) |          4.0 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.5 | **171.1** |  202.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        331.0 | **192.5** |  346.3 |
| Throughput median (tok/s) |          3.0 |   **5.2** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        554.0 |     169.8 | **164.1** |
| TPOT median (ms)          |        186.0 |  **57.2** |      98.3 |
| E2E median (ms)           |        701.4 | **222.8** |     260.1 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        387.6 | **57.5** |   73.9 |
| TPOT median (ms)          |        127.7 | **26.4** |   61.6 |
| E2E median (ms)           |        482.3 | **77.6** |  148.0 |
| Throughput median (tok/s) |          2.9 | **16.0** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        846.0 |      72.5 | **66.1** |
| TPOT median (ms)          |         16.8 |  **15.0** |     22.3 |
| E2E median (ms)           |       1514.5 | **628.2** |    839.6 |
| Throughput median (tok/s) |         20.6 |  **58.5** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        452.9 | **126.9** |  128.7 |
| TPOT median (ms)          |         95.9 |  **30.8** |   51.6 |
| E2E median (ms)           |        679.5 | **266.8** |  360.2 |
| Throughput median (tok/s) |          6.5 |  **18.6** |   13.2 |
| Correctness               |          98% |       99% |    99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:09 AM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     351.9s (5.9m) | `c837893` |
| vllm         |   1111.0s (18.5m) | `965d076` |
| sglang       | **167.5s (2.8m)** | `abe2ec2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        297.5 |    163.0 | **137.9** |
| TPOT median (ms)          |        156.1 | **57.2** |      79.4 |
| E2E median (ms)           |        407.4 |    219.2 | **210.0** |
| Throughput median (tok/s) |          3.6 |  **6.7** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        304.1 |     223.8 | **201.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        333.8 | **307.3** |     346.4 |
| Throughput median (tok/s) |          3.0 |   **3.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        553.4 |     179.2 | **162.9** |
| TPOT median (ms)          |        128.6 |  **66.3** |     103.8 |
| E2E median (ms)           |        639.6 | **236.0** |     261.8 |
| Throughput median (tok/s) |          2.1 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.9 | **58.5** |   77.9 |
| TPOT median (ms)          |        134.4 | **26.9** |   61.3 |
| E2E median (ms)           |        429.2 | **79.0** |  154.8 |
| Throughput median (tok/s) |          3.3 | **15.4** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        765.4 |      72.0 | **70.1** |
| TPOT median (ms)          |         17.0 |  **15.0** |     22.7 |
| E2E median (ms)           |       1453.9 | **621.7** |    849.2 |
| Throughput median (tok/s) |         21.7 |  **58.1** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        449.1 |     139.3 | **130.0** |
| TPOT median (ms)          |         87.2 |  **33.1** |      53.4 |
| E2E median (ms)           |        652.8 | **292.6** |     364.4 |
| Throughput median (tok/s) |          6.7 |  **17.9** |      12.9 |
| Correctness               |          98% |       98% |       99% |

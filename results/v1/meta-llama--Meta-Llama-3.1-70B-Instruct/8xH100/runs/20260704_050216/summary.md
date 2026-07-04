# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         6/20 | **11/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **46.3s (0.8m)** | `390fed4` |
| vllm         |    271.7s (4.5m) | `f329ce4` |
| sglang       |    171.1s (2.9m) | `ad744c6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        163.3 | **141.3** |  147.5 |
| TPOT median (ms)          |     **47.0** |      50.0 |   74.8 |
| E2E median (ms)           |        212.1 | **192.2** |  220.5 |
| Throughput median (tok/s) |          5.8 |   **7.4** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **166.6** | 194.9 |  215.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **178.7** | 218.7 |  369.6 |
| Throughput median (tok/s) |      **5.6** |   4.6 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        363.7 |     178.1 | **172.2** |
| TPOT median (ms)          |     **63.2** |      66.8 |     107.2 |
| E2E median (ms)           |        419.6 | **240.5** |     282.5 |
| Throughput median (tok/s) |          3.3 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        136.4 | **63.4** |   73.5 |
| TPOT median (ms)          |     **28.0** |     31.1 |   59.5 |
| E2E median (ms)           |        156.3 | **86.0** |  135.3 |
| Throughput median (tok/s) |          8.1 | **14.1** |   10.3 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        221.6 |      84.4 | **74.6** |
| TPOT median (ms)          |         20.9 |  **15.0** |     21.8 |
| E2E median (ms)           |        954.2 | **632.0** |    845.2 |
| Throughput median (tok/s) |         37.6 |  **57.3** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        210.3 | **132.4** |  136.7 |
| TPOT median (ms)          |     **31.8** |      32.6 |   52.6 |
| E2E median (ms)           |        384.2 | **273.9** |  370.6 |
| Throughput median (tok/s) |         12.1 |  **17.9** |   13.1 |
| Correctness               |          99% |       99% |    98% |

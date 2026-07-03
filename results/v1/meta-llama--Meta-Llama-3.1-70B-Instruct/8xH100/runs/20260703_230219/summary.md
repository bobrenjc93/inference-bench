# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **36.7s (0.6m)** | `390fed4` |
| vllm         |    257.0s (4.3m) | `d6d39c1` |
| sglang       |    151.9s (2.5m) | `6ce02b9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        160.2 |     155.3 | **138.9** |
| TPOT median (ms)          |     **46.4** |      49.0 |      77.1 |
| E2E median (ms)           |        208.7 | **198.3** |     214.1 |
| Throughput median (tok/s) |          5.8 |   **7.1** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        205.9 | **159.1** |  214.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        305.1 | **268.4** |  370.5 |
| Throughput median (tok/s) |          3.3 |   **3.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        340.0 |     198.3 | **172.4** |
| TPOT median (ms)          |         58.6 |  **38.2** |     101.4 |
| E2E median (ms)           |        393.3 | **233.8** |     272.0 |
| Throughput median (tok/s) |          3.4 |   **5.8** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        129.2 | **64.2** |   71.4 |
| TPOT median (ms)          |         37.4 | **30.2** |   68.1 |
| E2E median (ms)           |        156.2 | **87.7** |  143.3 |
| Throughput median (tok/s) |          8.4 | **13.7** |   10.0 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        252.8 |      73.4 | **68.4** |
| TPOT median (ms)          |         20.6 |  **15.2** |     22.6 |
| E2E median (ms)           |        935.9 | **634.9** |    834.6 |
| Throughput median (tok/s) |         37.1 |  **57.7** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        217.6 | **130.1** |  133.2 |
| TPOT median (ms)          |         32.6 |  **26.5** |   53.8 |
| E2E median (ms)           |        399.9 | **284.6** |  366.9 |
| Throughput median (tok/s) |         11.6 |  **17.6** |   12.9 |
| Correctness               |          98% |       98% |    98% |

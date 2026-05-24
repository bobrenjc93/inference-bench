# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     399.2s (6.7m) | `9f91b40` |
| vllm         |   1261.2s (21.0m) | `357fddf` |
| sglang       | **183.3s (3.1m)** | `0b65588` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        269.6 |     156.7 | **141.6** |
| TPOT median (ms)          |        153.1 |  **52.3** |      75.0 |
| E2E median (ms)           |        367.8 | **204.5** |     212.7 |
| Throughput median (tok/s) |          4.0 |   **7.1** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        249.1 |     209.6 | **200.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        295.1 | **234.0** |     333.8 |
| Throughput median (tok/s) |          3.4 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        645.7 |     165.3 | **160.7** |
| TPOT median (ms)          |        114.8 |  **57.8** |     102.7 |
| E2E median (ms)           |        736.8 | **211.3** |     262.6 |
| Throughput median (tok/s) |          1.8 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.7 | **57.7** |   79.4 |
| TPOT median (ms)          |        133.5 | **26.7** |   66.7 |
| E2E median (ms)           |        484.5 | **78.6** |  164.9 |
| Throughput median (tok/s) |          2.7 | **15.5** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        826.8 |      67.1 | **64.2** |
| TPOT median (ms)          |         15.4 |  **15.0** |     22.2 |
| E2E median (ms)           |       1514.4 | **609.5** |    826.7 |
| Throughput median (tok/s) |         23.4 |  **59.3** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        473.8 |     131.3 | **129.3** |
| TPOT median (ms)          |         83.3 |  **30.4** |      53.3 |
| E2E median (ms)           |        679.7 | **267.6** |     360.1 |
| Throughput median (tok/s) |          7.0 |  **18.5** |      13.0 |
| Correctness               |          98% |       99% |       98% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:10 PM PT, May 22 2026

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
| torchinferno |     356.7s (5.9m) | `9f91b40` |
| vllm         |   1278.5s (21.3m) | `6d30655` |
| sglang       | **191.5s (3.2m)** | `c112f76` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        298.3 |     155.7 | **149.9** |
| TPOT median (ms)          |        147.2 |  **58.5** |      75.2 |
| E2E median (ms)           |        403.1 | **208.1** |     221.7 |
| Throughput median (tok/s) |          3.8 |   **6.9** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        292.4 |     205.4 | **200.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        316.9 | **226.7** |     338.0 |
| Throughput median (tok/s) |          3.2 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        700.7 |     173.9 | **160.9** |
| TPOT median (ms)          |        118.8 |  **53.4** |     101.5 |
| E2E median (ms)           |        819.4 | **222.9** |     256.0 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        422.7 | **56.9** |   77.9 |
| TPOT median (ms)          |        128.7 | **26.8** |   61.0 |
| E2E median (ms)           |        524.7 | **77.0** |  153.6 |
| Throughput median (tok/s) |          2.5 | **15.8** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        857.2 |      74.6 | **66.3** |
| TPOT median (ms)          |         17.3 |  **14.9** |     22.3 |
| E2E median (ms)           |       1508.0 | **626.5** |    845.3 |
| Throughput median (tok/s) |         21.1 |  **57.4** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        514.2 |     133.3 | **131.1** |
| TPOT median (ms)          |         82.4 |  **30.7** |      52.0 |
| E2E median (ms)           |        714.4 | **272.2** |     362.9 |
| Throughput median (tok/s) |          6.4 |  **18.2** |      13.0 |
| Correctness               |          98% |       99% |       99% |

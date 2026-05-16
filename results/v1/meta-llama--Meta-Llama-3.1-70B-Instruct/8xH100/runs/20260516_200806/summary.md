# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     378.0s (6.3m) | `db749af` |
| vllm         |   1168.5s (19.5m) | `787bc0d` |
| sglang       | **167.8s (2.8m)** | `57eb5bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        283.6 |     161.4 | **142.2** |
| TPOT median (ms)          |        147.3 |  **55.3** |      74.5 |
| E2E median (ms)           |        365.9 | **211.6** |     213.0 |
| Throughput median (tok/s) |          4.0 |   **6.6** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        232.6 | **196.0** |  211.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        329.2 | **221.1** |  344.7 |
| Throughput median (tok/s) |          3.0 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        524.6 |     167.1 | **156.3** |
| TPOT median (ms)          |        123.8 |  **60.7** |      97.0 |
| E2E median (ms)           |        621.5 | **223.3** |     256.7 |
| Throughput median (tok/s) |          2.2 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        332.8 | **58.4** |   76.7 |
| TPOT median (ms)          |        130.9 | **27.0** |   52.3 |
| E2E median (ms)           |        431.0 | **78.9** |  147.7 |
| Throughput median (tok/s) |          3.2 | **15.5** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        782.1 |      68.6 | **66.3** |
| TPOT median (ms)          |         16.5 |  **15.1** |     22.0 |
| E2E median (ms)           |       1427.6 | **613.7** |    819.4 |
| Throughput median (tok/s) |         21.5 |  **58.4** |     42.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        431.1 | **130.3** |  130.6 |
| TPOT median (ms)          |         83.7 |  **31.6** |   49.2 |
| E2E median (ms)           |        635.0 | **269.7** |  356.3 |
| Throughput median (tok/s) |          6.8 |  **18.3** |   13.2 |
| Correctness               |          98% |       99% |    99% |

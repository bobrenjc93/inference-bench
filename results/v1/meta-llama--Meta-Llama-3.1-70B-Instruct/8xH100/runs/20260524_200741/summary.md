# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, May 24 2026

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
| torchinferno |     254.2s (4.2m) | `9f91b40` |
| vllm         |   1269.6s (21.2m) | `d0a100c` |
| sglang       | **189.6s (3.2m)** | `44922de` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.5 |     162.8 | **147.6** |
| TPOT median (ms)          |        155.7 |  **58.4** |      75.5 |
| E2E median (ms)           |        385.1 | **213.4** |     217.0 |
| Throughput median (tok/s) |          4.0 |   **6.8** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        266.7 | **191.8** |  202.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        333.8 | **212.5** |  341.3 |
| Throughput median (tok/s) |          3.0 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        655.6 |     171.9 | **155.8** |
| TPOT median (ms)          |        198.9 |  **63.0** |     104.3 |
| E2E median (ms)           |        762.8 | **218.2** |     261.6 |
| Throughput median (tok/s) |          1.7 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        407.7 | **58.6** |   76.4 |
| TPOT median (ms)          |        135.2 | **27.6** |   64.2 |
| E2E median (ms)           |        508.9 | **79.6** |  160.5 |
| Throughput median (tok/s) |          2.6 | **15.5** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        919.8 |      69.5 | **68.8** |
| TPOT median (ms)          |         17.7 |  **15.0** |     22.2 |
| E2E median (ms)           |       1582.1 | **606.6** |    846.5 |
| Throughput median (tok/s) |         21.0 |  **59.4** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        507.1 |     130.9 | **130.3** |
| TPOT median (ms)          |        101.5 |  **32.8** |      53.2 |
| E2E median (ms)           |        714.5 | **266.1** |     365.4 |
| Throughput median (tok/s) |          6.4 |  **18.5** |      13.0 |
| Correctness               |          99% |       99% |       99% |

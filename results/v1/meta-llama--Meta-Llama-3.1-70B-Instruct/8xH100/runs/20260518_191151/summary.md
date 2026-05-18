# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:09 AM PT, May 18 2026

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
| torchinferno |     319.8s (5.3m) | `c837893` |
| vllm         |   1143.8s (19.1m) | `ce88f01` |
| sglang       | **165.4s (2.8m)** | `1f185c6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        282.5 |     144.2 | **139.2** |
| TPOT median (ms)          |        153.8 |  **52.4** |      75.2 |
| E2E median (ms)           |        372.9 | **191.9** |     207.7 |
| Throughput median (tok/s) |          4.0 |   **7.5** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.2 | **195.2** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        294.0 | **217.2** |  340.7 |
| Throughput median (tok/s) |          3.4 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        544.3 |     173.8 | **153.1** |
| TPOT median (ms)          |        110.7 |  **63.2** |      99.2 |
| E2E median (ms)           |        644.8 | **228.8** |     252.9 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        341.5 | **58.3** |   71.6 |
| TPOT median (ms)          |        129.9 | **26.9** |   62.5 |
| E2E median (ms)           |        439.6 | **79.3** |  143.5 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        703.0 |      75.1 | **66.9** |
| TPOT median (ms)          |         15.4 |  **15.0** |     22.1 |
| E2E median (ms)           |       1211.3 | **632.1** |    821.8 |
| Throughput median (tok/s) |         29.8 |  **58.0** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        427.9 |     129.3 | **127.4** |
| TPOT median (ms)          |         82.0 |  **31.5** |      51.8 |
| E2E median (ms)           |        592.5 | **269.8** |     353.3 |
| Throughput median (tok/s) |          8.4 |  **18.4** |      13.3 |
| Correctness               |          99% |       98% |       99% |

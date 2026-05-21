# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:43 AM PT, May 21 2026

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
| torchinferno |     346.0s (5.8m) | `9f91b40` |
| vllm         |   1182.5s (19.7m) | `1c78f76` |
| sglang       | **187.6s (3.1m)** | `b765fae` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        276.2 |     151.8 | **134.3** |
| TPOT median (ms)          |        153.6 |  **53.9** |      76.2 |
| E2E median (ms)           |        365.2 | **199.6** |     204.9 |
| Throughput median (tok/s) |          4.0 |   **7.5** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        234.6 | **188.4** |  189.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        311.7 | **211.0** |  337.2 |
| Throughput median (tok/s) |          3.2 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        785.1 |     178.1 | **162.4** |
| TPOT median (ms)          |        169.7 |  **57.0** |     101.2 |
| E2E median (ms)           |        866.4 | **229.4** |     256.0 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        349.0 | **58.6** |   72.0 |
| TPOT median (ms)          |        130.1 | **26.8** |   67.5 |
| E2E median (ms)           |        447.1 | **78.5** |  158.9 |
| Throughput median (tok/s) |          2.9 | **15.5** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        755.2 |      68.7 | **65.8** |
| TPOT median (ms)          |         15.4 |  **15.0** |     23.0 |
| E2E median (ms)           |       1427.9 | **603.3** |    864.3 |
| Throughput median (tok/s) |         25.0 |  **59.1** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        480.0 |     129.1 | **124.7** |
| TPOT median (ms)          |         93.8 |  **30.5** |      53.6 |
| E2E median (ms)           |        683.6 | **264.4** |     364.2 |
| Throughput median (tok/s) |          7.3 |  **18.6** |      12.9 |
| Correctness               |          99% |       99% |       98% |

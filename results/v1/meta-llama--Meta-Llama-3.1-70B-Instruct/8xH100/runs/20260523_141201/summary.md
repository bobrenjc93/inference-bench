# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, May 23 2026

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
| torchinferno |     381.7s (6.4m) | `9f91b40` |
| vllm         |   1286.9s (21.4m) | `3f3e862` |
| sglang       | **223.0s (3.7m)** | `a5a64a3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        321.6 |     156.8 | **142.7** |
| TPOT median (ms)          |        149.0 |  **56.2** |      73.1 |
| E2E median (ms)           |        444.9 | **210.9** |     213.1 |
| Throughput median (tok/s) |          3.0 |   **7.2** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        263.9 | **194.4** |  198.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.4 | **235.5** |  337.1 |
| Throughput median (tok/s) |          3.1 |   **4.2** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        892.0 |     171.0 | **161.8** |
| TPOT median (ms)          |        134.8 |  **60.3** |     108.2 |
| E2E median (ms)           |        992.8 | **223.0** |     258.5 |
| Throughput median (tok/s) |          1.3 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        354.1 | **57.0** |   74.3 |
| TPOT median (ms)          |        130.3 | **27.2** |   63.8 |
| E2E median (ms)           |        455.6 | **77.9** |  150.8 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.5 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        963.7 |      67.8 | **65.2** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.4 |
| E2E median (ms)           |       1636.1 | **599.0** |    840.0 |
| Throughput median (tok/s) |         19.6 |  **59.4** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        559.0 |     129.4 | **128.4** |
| TPOT median (ms)          |         86.0 |  **31.7** |      53.5 |
| E2E median (ms)           |        769.7 | **269.3** |     359.9 |
| Throughput median (tok/s) |          6.0 |  **18.6** |      13.0 |
| Correctness               |          99% |       98% |       99% |

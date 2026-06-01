# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     249.4s (4.2m) | `83e85dd` |
| vllm         |   1210.6s (20.2m) | `8b8546d` |
| sglang       | **178.5s (3.0m)** | `373cadc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        247.0 |     158.2 | **148.9** |
| TPOT median (ms)          |     **50.0** |      55.4 |      74.8 |
| E2E median (ms)           |        294.1 | **209.2** |     216.9 |
| Throughput median (tok/s) |          3.9 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        560.6 | **189.2** |  203.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        653.2 | **210.4** |  330.1 |
| Throughput median (tok/s) |          1.5 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        876.3 |     170.3 | **160.0** |
| TPOT median (ms)          |         99.3 |  **67.0** |      98.9 |
| E2E median (ms)           |        954.8 | **219.0** |     258.8 |
| Throughput median (tok/s) |          1.3 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        468.0 | **58.6** |   78.8 |
| TPOT median (ms)          |         28.8 | **28.2** |   49.6 |
| E2E median (ms)           |        513.5 | **79.9** |  139.8 |
| Throughput median (tok/s) |          2.6 | **15.4** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        958.3 |  **67.2** |   74.0 |
| TPOT median (ms)          |         35.5 |  **15.0** |   23.9 |
| E2E median (ms)           |       2473.0 | **601.4** |  879.4 |
| Throughput median (tok/s) |         12.7 |  **59.6** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        622.1 | **128.7** |  133.0 |
| TPOT median (ms)          |         42.7 |  **33.1** |   49.4 |
| E2E median (ms)           |        977.7 | **264.0** |  365.0 |
| Throughput median (tok/s) |          4.4 |  **18.6** |   12.6 |
| Correctness               |          99% |       99% |    99% |

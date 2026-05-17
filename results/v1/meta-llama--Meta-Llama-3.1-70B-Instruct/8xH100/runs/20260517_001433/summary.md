# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     354.9s (5.9m) | `db749af` |
| vllm         |   1069.7s (17.8m) | `0867497` |
| sglang       | **162.8s (2.7m)** | `0c017db` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.9 |    165.9 | **136.9** |
| TPOT median (ms)          |        148.4 | **57.0** |      71.0 |
| E2E median (ms)           |        374.6 |    221.5 | **206.0** |
| Throughput median (tok/s) |          3.8 |  **6.8** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.6 | **188.5** |  201.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        321.9 | **210.1** |  335.3 |
| Throughput median (tok/s) |          3.1 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        599.3 |     177.2 | **154.6** |
| TPOT median (ms)          |        115.3 |  **53.5** |     101.9 |
| E2E median (ms)           |        688.9 | **223.0** |     248.5 |
| Throughput median (tok/s) |          1.9 |   **6.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        358.5 | **57.6** |   74.3 |
| TPOT median (ms)          |        130.3 | **26.7** |   60.3 |
| E2E median (ms)           |        458.5 | **77.8** |  147.8 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      69.7 | **68.0** |
| TPOT median (ms)          |            - |  **15.0** |     22.5 |
| E2E median (ms)           |            - | **608.1** |    828.7 |
| Throughput median (tok/s) |            - |  **58.8** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        385.3 |     131.8 | **127.1** |
| TPOT median (ms)          |         98.5 |  **30.4** |      51.1 |
| E2E median (ms)           |        461.0 | **268.1** |     353.3 |
| Throughput median (tok/s) |          3.0 |  **18.4** |      13.2 |
| Correctness               |          98% |       99% |       99% |

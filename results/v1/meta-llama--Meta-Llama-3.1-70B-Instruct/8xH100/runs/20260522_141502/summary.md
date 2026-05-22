# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, May 22 2026

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
| torchinferno |     400.3s (6.7m) | `9f91b40` |
| vllm         |   1268.7s (21.1m) | `79ff0ff` |
| sglang       | **196.5s (3.3m)** | `f5ed268` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        290.0 |    167.3 | **137.2** |
| TPOT median (ms)          |        152.0 | **58.9** |      72.8 |
| E2E median (ms)           |        389.4 |    223.9 | **204.6** |
| Throughput median (tok/s) |          3.8 |  **6.4** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        302.6 | **184.9** |  197.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        323.1 | **210.2** |  334.5 |
| Throughput median (tok/s) |          3.1 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        671.3 |     165.2 | **158.5** |
| TPOT median (ms)          |        113.6 |  **57.0** |     103.1 |
| E2E median (ms)           |        779.9 | **217.7** |     254.8 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        372.8 | **57.3** |   73.0 |
| TPOT median (ms)          |        129.5 | **26.6** |   62.9 |
| E2E median (ms)           |        474.6 | **78.1** |  149.2 |
| Throughput median (tok/s) |          2.9 | **16.1** |    9.7 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.3 | **63.6** |
| TPOT median (ms)          |            - |  **15.0** |     22.6 |
| E2E median (ms)           |            - | **622.4** |    828.1 |
| Throughput median (tok/s) |            - |  **59.0** |     42.0 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        409.2 |     129.0 | **125.9** |
| TPOT median (ms)          |         98.7 |  **31.5** |      52.3 |
| E2E median (ms)           |        491.7 | **270.4** |     354.2 |
| Throughput median (tok/s) |          2.9 |  **18.5** |      13.2 |
| Correctness               |          98% |       98% |       99% |

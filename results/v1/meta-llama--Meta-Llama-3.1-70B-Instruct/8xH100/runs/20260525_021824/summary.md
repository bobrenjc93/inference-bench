# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:04 PM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     373.8s (6.2m) | `9f91b40` |
| vllm         |   1331.6s (22.2m) | `b06813e` |
| sglang       | **210.7s (3.5m)** | `850887d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        284.3 |    162.1 | **146.2** |
| TPOT median (ms)          |        152.4 | **55.4** |      72.3 |
| E2E median (ms)           |        381.7 |    218.3 | **213.8** |
| Throughput median (tok/s) |          4.0 |  **6.6** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        260.2 | **194.7** |  201.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        307.3 | **228.2** |  339.1 |
| Throughput median (tok/s) |          3.3 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        779.9 |     175.3 | **160.2** |
| TPOT median (ms)          |        187.4 |  **45.9** |     102.2 |
| E2E median (ms)           |        899.0 | **222.3** |     254.3 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        315.2 | **58.6** |   74.6 |
| TPOT median (ms)          |        130.4 | **26.8** |   46.7 |
| E2E median (ms)           |        418.7 | **79.1** |  127.1 |
| Throughput median (tok/s) |          3.5 | **15.7** |   10.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **67.6** |   70.0 |
| TPOT median (ms)          |            - |  **15.0** |   22.0 |
| E2E median (ms)           |            - | **606.7** |  816.6 |
| Throughput median (tok/s) |            - |  **58.8** |   42.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        409.9 |     131.6 | **130.6** |
| TPOT median (ms)          |        117.6 |  **28.6** |      48.6 |
| E2E median (ms)           |        501.7 | **270.9** |     350.2 |
| Throughput median (tok/s) |          3.1 |  **18.3** |      13.4 |
| Correctness               |          98% |       99% |       98% |

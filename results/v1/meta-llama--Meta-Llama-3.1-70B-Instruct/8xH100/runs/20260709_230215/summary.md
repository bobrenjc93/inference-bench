# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.3s (0.7m)** | `75387c9` |
| vllm         |    199.9s (3.3m) | `f1a5add` |
| sglang       |    243.6s (4.1m) | `77b7698` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        171.9 | **124.2** |  139.4 |
| TPOT median (ms)          |         43.7 |  **39.0** |   78.0 |
| E2E median (ms)           |        209.0 | **159.9** |  215.9 |
| Throughput median (tok/s) |          6.1 |   **9.2** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **149.2** |  224.9 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **173.8** |  386.9 |
| Throughput median (tok/s) |            - |   **5.8** |    2.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **151.4** |  167.4 |
| TPOT median (ms)          |            - |  **47.5** |  110.7 |
| E2E median (ms)           |            - | **197.7** |  283.9 |
| Throughput median (tok/s) |            - |   **7.1** |    4.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **33.8** |   48.2 |
| TPOT median (ms)          |            - | **22.3** |  351.9 |
| E2E median (ms)           |            - | **50.5** |  417.2 |
| Throughput median (tok/s) |            - | **25.2** |    3.6 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.9 | **71.1** |
| TPOT median (ms)          |            - |  **14.8** |     22.5 |
| E2E median (ms)           |            - | **595.8** |    883.4 |
| Throughput median (tok/s) |            - |  **58.7** |     41.3 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        171.9 | **107.3** |  130.2 |
| TPOT median (ms)          |         43.7 |  **24.7** |  112.6 |
| E2E median (ms)           |    **209.0** |     235.5 |  437.5 |
| Throughput median (tok/s) |          6.1 |  **21.2** |   11.5 |
| Correctness               |          98% |       99% |    99% |

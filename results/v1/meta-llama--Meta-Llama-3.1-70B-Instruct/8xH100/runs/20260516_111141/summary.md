# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:08 AM PT, May 16 2026

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
| torchinferno |     304.2s (5.1m) | `db749af` |
| vllm         |   1066.9s (17.8m) | `4db300e` |
| sglang       | **170.9s (2.8m)** | `90d3d42` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        284.4 |    161.3 | **140.8** |
| TPOT median (ms)          |        148.1 | **55.4** |      74.9 |
| E2E median (ms)           |        374.2 |    217.3 | **208.0** |
| Throughput median (tok/s) |          3.9 |  **6.6** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.9 | **192.7** |  204.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        311.6 | **226.4** |  345.9 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        508.4 |     168.7 | **157.1** |
| TPOT median (ms)          |        103.9 |  **60.7** |      97.4 |
| E2E median (ms)           |        607.2 | **219.6** |     255.0 |
| Throughput median (tok/s) |          2.2 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        319.2 | **57.7** |   75.8 |
| TPOT median (ms)          |        130.5 | **26.9** |   51.9 |
| E2E median (ms)           |        417.1 | **77.7** |  140.0 |
| Throughput median (tok/s) |          3.4 | **15.9** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **67.7** |   72.2 |
| TPOT median (ms)          |            - |  **14.9** |   22.3 |
| E2E median (ms)           |            - | **602.9** |  829.5 |
| Throughput median (tok/s) |            - |  **59.5** |   42.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        326.7 | **129.6** |  130.1 |
| TPOT median (ms)          |         95.6 |  **31.6** |   49.3 |
| E2E median (ms)           |        427.5 | **268.8** |  355.7 |
| Throughput median (tok/s) |          3.2 |  **18.5** |   13.2 |
| Correctness               |          98% |       99% |    99% |

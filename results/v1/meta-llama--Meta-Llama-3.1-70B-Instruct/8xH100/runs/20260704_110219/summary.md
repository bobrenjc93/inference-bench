# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **12/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.0s (0.7m)** | `390fed4` |
| vllm         |    281.8s (4.7m) | `1a308c4` |
| sglang       |    157.6s (2.6m) | `e552f6e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        157.5 |     150.2 | **140.0** |
| TPOT median (ms)          |     **46.2** |      50.3 |      75.7 |
| E2E median (ms)           |        205.9 | **192.9** |     217.3 |
| Throughput median (tok/s) |          5.8 |   **7.3** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **157.3** | 215.8 |  217.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **168.9** | 244.2 |  369.3 |
| Throughput median (tok/s) |      **5.9** |   4.1 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        310.8 |     182.7 | **162.9** |
| TPOT median (ms)          |         58.9 |  **43.1** |     103.5 |
| E2E median (ms)           |        366.4 | **225.4** |     266.8 |
| Throughput median (tok/s) |          4.1 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        135.0 | **64.2** |   72.5 |
| TPOT median (ms)          |         41.6 | **30.2** |   59.1 |
| E2E median (ms)           |        160.9 | **87.7** |  136.5 |
| Throughput median (tok/s) |          8.2 | **13.9** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        257.5 |      93.5 | **71.8** |
| TPOT median (ms)          |         19.8 |  **15.1** |     22.4 |
| E2E median (ms)           |        981.7 | **693.3** |    852.0 |
| Throughput median (tok/s) |         36.8 |  **55.2** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        203.6 |     141.3 | **132.9** |
| TPOT median (ms)          |         33.3 |  **27.7** |      52.2 |
| E2E median (ms)           |        376.8 | **288.7** |     368.4 |
| Throughput median (tok/s) |         12.2 |  **17.3** |      12.9 |
| Correctness               |          99% |       99% |       99% |

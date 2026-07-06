# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, Jul 5 2026

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
| torchinferno | **39.2s (0.7m)** | `46164b4` |
| vllm         |    361.1s (6.0m) | `95a248f` |
| sglang       |    213.0s (3.5m) | `8673e85` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        154.1 | **126.0** |  132.3 |
| TPOT median (ms)          |         45.7 |  **45.0** |   82.2 |
| E2E median (ms)           |        196.1 | **167.0** |  209.6 |
| Throughput median (tok/s) |          6.0 |   **8.2** |    5.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        160.2 | **124.1** |  208.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        167.8 | **149.7** |  351.0 |
| Throughput median (tok/s) |          6.0 |   **6.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        317.7 | **147.0** |  160.2 |
| TPOT median (ms)          |         61.3 |  **50.0** |  105.2 |
| E2E median (ms)           |        376.9 | **188.8** |  268.9 |
| Throughput median (tok/s) |          4.0 |   **7.3** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         79.4 | **32.4** |   47.3 |
| TPOT median (ms)          |         64.1 | **21.7** |  318.4 |
| E2E median (ms)           |        114.6 | **48.0** |  359.6 |
| Throughput median (tok/s) |         12.3 | **25.8** |    4.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        262.5 |      75.7 | **64.8** |
| TPOT median (ms)          |         19.6 |  **14.8** |     22.7 |
| E2E median (ms)           |        934.2 | **643.0** |    921.8 |
| Throughput median (tok/s) |         37.0 |  **59.4** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.8 | **101.0** |  122.7 |
| TPOT median (ms)          |         38.1 |  **26.3** |  105.7 |
| E2E median (ms)           |        357.9 | **239.3** |  422.2 |
| Throughput median (tok/s) |         13.1 |  **21.5** |   11.8 |
| Correctness               |          98% |       98% |    99% |

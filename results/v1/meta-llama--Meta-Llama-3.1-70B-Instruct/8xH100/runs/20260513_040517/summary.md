# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:06 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     301.3s (5.0m) | `9d5290c` |
| vllm         |    982.5s (16.4m) | `dcacdf9` |
| sglang       | **159.1s (2.7m)** | `4e35c30` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        380.2 |    170.0 | **136.9** |
| TPOT median (ms)          |        479.1 | **59.0** |      72.0 |
| E2E median (ms)           |        804.6 |    229.7 | **205.2** |
| Throughput median (tok/s) |          1.7 |  **6.3** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        729.2 | **198.5** |      - |
| TPOT median (ms)          |          0.0 |       0.0 |      - |
| E2E median (ms)           |        760.4 | **220.8** |      - |
| Throughput median (tok/s) |          1.3 |   **4.5** |      - |
| Correctness               |         100% |      100% |      - |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        650.7 | **166.3** |      - |
| TPOT median (ms)          |        195.9 |  **51.6** |      - |
| E2E median (ms)           |        836.4 | **212.9** |      - |
| Throughput median (tok/s) |          1.5 |   **6.4** |      - |
| Correctness               |          98% |       98% |      - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        397.1 | **57.3** |      - |
| TPOT median (ms)          |        455.0 | **26.9** |      - |
| E2E median (ms)           |        802.8 | **77.8** |      - |
| Throughput median (tok/s) |          1.7 | **15.7** |      - |
| Correctness               |          96% |      97% |      - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        606.5 |  **68.7** |      - |
| TPOT median (ms)          |         30.7 |  **15.0** |      - |
| E2E median (ms)           |       1978.7 | **610.3** |      - |
| Throughput median (tok/s) |         18.4 |  **58.7** |      - |
| Correctness               |         100% |      100% |      - |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        552.7 | **132.2** |     136.9 |
| TPOT median (ms)          |        232.1 |  **30.5** |      72.0 |
| E2E median (ms)           |       1036.6 |     270.3 | **205.2** |
| Throughput median (tok/s) |          4.9 |  **18.3** |       5.9 |
| Correctness               |          98% |       99% |       98% |

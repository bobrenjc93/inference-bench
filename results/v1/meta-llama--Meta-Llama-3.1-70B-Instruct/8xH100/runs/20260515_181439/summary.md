# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:09 AM PT, May 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **2/4** |    1/4 |
| **Total**        |         1/20 | **14/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     384.5s (6.4m) | `df63258` |
| vllm         |   1173.9s (19.6m) | `6147c70` |
| sglang       | **174.1s (2.9m)** | `4df42da` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        286.9 |    158.6 | **136.7** |
| TPOT median (ms)          |        149.9 | **54.5** |      75.4 |
| E2E median (ms)           |        375.4 |    209.2 | **207.3** |
| Throughput median (tok/s) |          3.8 |  **6.9** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        262.8 | **200.1** |  210.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        291.8 | **255.9** |  352.4 |
| Throughput median (tok/s) |          3.4 |   **3.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        534.4 |     174.1 | **160.4** |
| TPOT median (ms)          |        135.7 |  **62.8** |     102.7 |
| E2E median (ms)           |        631.7 | **225.4** |     258.0 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        347.5 | **57.6** |   74.2 |
| TPOT median (ms)          |        132.9 | **27.0** |   68.6 |
| E2E median (ms)           |        458.7 | **77.9** |  161.1 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        573.1 |      65.5 | **65.2** |
| TPOT median (ms)          |     **14.9** |      15.0 |     22.1 |
| E2E median (ms)           |       1195.1 | **606.2** |    815.3 |
| Throughput median (tok/s) |         27.3 |  **59.9** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        400.9 |     131.2 | **129.3** |
| TPOT median (ms)          |         86.7 |  **31.9** |      53.7 |
| E2E median (ms)           |        590.5 | **274.9** |     358.8 |
| Throughput median (tok/s) |          7.9 |  **18.5** |      13.2 |
| Correctness               |          98% |       99% |       99% |

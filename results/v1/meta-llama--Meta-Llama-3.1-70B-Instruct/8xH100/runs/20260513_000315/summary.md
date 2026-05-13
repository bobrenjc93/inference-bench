# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:07 PM PT, May 12 2026

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
| torchinferno |     339.0s (5.6m) | `9d5290c` |
| vllm         |    962.3s (16.0m) | `3d635c5` |
| sglang       | **167.3s (2.8m)** | `4fb40bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        394.7 |    162.2 | **139.6** |
| TPOT median (ms)          |        487.0 | **57.4** |      76.4 |
| E2E median (ms)           |        825.6 |    217.9 | **210.3** |
| Throughput median (tok/s) |          1.7 |  **6.5** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        723.6 | **184.7** |  200.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        754.8 | **207.0** |  333.1 |
| Throughput median (tok/s) |          1.3 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        618.6 |     171.9 | **158.5** |
| TPOT median (ms)          |        213.9 |  **58.8** |      93.5 |
| E2E median (ms)           |        815.9 | **225.6** |     255.9 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        528.9 | **58.0** |   75.7 |
| TPOT median (ms)          |        465.2 | **26.6** |   61.8 |
| E2E median (ms)           |        908.5 | **78.6** |  152.9 |
| Throughput median (tok/s) |          1.7 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        617.4 |      69.9 | **66.6** |
| TPOT median (ms)          |         31.8 |  **15.0** |     22.3 |
| E2E median (ms)           |       2013.7 | **608.6** |    821.4 |
| Throughput median (tok/s) |         18.3 |  **58.5** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        576.7 |     129.4 | **128.2** |
| TPOT median (ms)          |        239.6 |  **31.6** |      50.8 |
| E2E median (ms)           |       1063.7 | **267.5** |     354.7 |
| Throughput median (tok/s) |          4.9 |  **18.3** |      13.1 |
| Correctness               |          98% |       99% |       98% |

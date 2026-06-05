# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **15/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     307.6s (5.1m) | `d62260f` |
| vllm         |   1349.3s (22.5m) | `4200f62` |
| sglang       | **193.0s (3.2m)** | `c9f582a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        296.7 |   172.8 | **141.5** |
| TPOT median (ms)          |     **49.2** |    58.7 |      71.3 |
| E2E median (ms)           |        340.8 |   226.6 | **206.7** |
| Throughput median (tok/s) |          4.0 | **6.6** |       5.9 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        255.4 | **179.4** |  205.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        358.4 | **203.1** |  337.1 |
| Throughput median (tok/s) |          2.8 |   **4.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        741.4 |     179.8 | **165.7** |
| TPOT median (ms)          |         62.8 |  **54.0** |     109.1 |
| E2E median (ms)           |        801.8 | **229.0** |     272.3 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        338.5 | **61.4** |   86.1 |
| TPOT median (ms)          |         32.6 | **28.7** |   47.8 |
| E2E median (ms)           |        367.9 | **82.8** |  152.4 |
| Throughput median (tok/s) |          3.6 | **14.3** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        515.3 |  **70.4** |   79.0 |
| TPOT median (ms)          |         31.6 |  **14.8** |   23.2 |
| E2E median (ms)           |       1564.0 | **618.1** |  866.2 |
| Throughput median (tok/s) |         21.2 |  **59.7** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        429.5 | **132.8** |  135.5 |
| TPOT median (ms)          |         35.2 |  **31.2** |   50.3 |
| E2E median (ms)           |        686.6 | **271.9** |  366.9 |
| Throughput median (tok/s) |          6.7 |  **18.3** |   12.7 |
| Correctness               |          99% |       99% |    99% |

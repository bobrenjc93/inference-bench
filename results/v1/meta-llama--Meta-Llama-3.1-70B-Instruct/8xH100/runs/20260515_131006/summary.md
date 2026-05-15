# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:08 AM PT, May 15 2026

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
| torchinferno |     344.8s (5.7m) | `d648af4` |
| vllm         |   1114.9s (18.6m) | `95cfe10` |
| sglang       | **172.7s (2.9m)** | `3f7e538` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        307.7 |    164.7 | **141.7** |
| TPOT median (ms)          |        159.9 | **62.9** |      75.0 |
| E2E median (ms)           |        398.4 |    225.8 | **211.1** |
| Throughput median (tok/s) |          3.7 |  **6.5** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.3 | **198.1** |  207.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        351.9 | **219.9** |  351.3 |
| Throughput median (tok/s) |          2.8 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        578.4 |     171.3 | **162.3** |
| TPOT median (ms)          |        137.1 |  **49.9** |      99.4 |
| E2E median (ms)           |        721.0 | **219.7** |     267.3 |
| Throughput median (tok/s) |          1.8 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        325.5 | **57.6** |   73.1 |
| TPOT median (ms)          |        133.6 | **26.8** |   61.2 |
| E2E median (ms)           |        418.3 | **77.7** |  151.3 |
| Throughput median (tok/s) |          3.9 | **15.8** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        520.1 |      68.4 | **67.4** |
| TPOT median (ms)          |         15.5 |  **15.0** |     22.5 |
| E2E median (ms)           |       1191.2 | **609.9** |    840.3 |
| Throughput median (tok/s) |         27.6 |  **59.3** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        405.6 |     132.0 | **130.5** |
| TPOT median (ms)          |         89.2 |  **30.9** |      51.6 |
| E2E median (ms)           |        616.2 | **270.6** |     364.3 |
| Throughput median (tok/s) |          8.0 |  **18.5** |      13.0 |
| Correctness               |          99% |       98% |       99% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 4 2026

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
| torchinferno |     468.8s (7.8m) | `a9e2f5a` |
| vllm         |   1375.6s (22.9m) | `9354fb1` |
| sglang       | **210.3s (3.5m)** | `1332540` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        286.0 |   161.7 | **139.7** |
| TPOT median (ms)          |     **50.3** |    63.6 |      77.6 |
| E2E median (ms)           |        335.0 |   221.9 | **210.8** |
| Throughput median (tok/s) |          3.7 | **6.7** |       5.7 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.4 | **195.3** |  211.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        370.7 | **215.9** |  350.9 |
| Throughput median (tok/s) |          2.7 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        824.1 |     179.3 | **161.8** |
| TPOT median (ms)          |        127.7 |  **68.6** |     107.1 |
| E2E median (ms)           |        942.4 | **234.5** |     264.6 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        345.2 | **61.0** |   79.1 |
| TPOT median (ms)          |         31.8 | **27.7** |   52.1 |
| E2E median (ms)           |        387.4 | **83.4** |  148.0 |
| Throughput median (tok/s) |          3.9 | **14.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        473.9 |  **69.7** |   75.3 |
| TPOT median (ms)          |         28.4 |  **14.9** |   23.4 |
| E2E median (ms)           |       1496.1 | **598.7** |  888.0 |
| Throughput median (tok/s) |         24.2 |  **59.3** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        439.7 | **133.4** |  133.4 |
| TPOT median (ms)          |         47.7 |  **34.9** |   52.0 |
| E2E median (ms)           |        706.3 | **270.9** |  372.5 |
| Throughput median (tok/s) |          7.2 |  **18.2** |   12.6 |
| Correctness               |          98% |       98% |    99% |

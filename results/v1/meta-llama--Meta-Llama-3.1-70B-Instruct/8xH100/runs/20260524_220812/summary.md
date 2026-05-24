# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     351.2s (5.9m) | `9f91b40` |
| vllm         |   1235.5s (20.6m) | `d0a100c` |
| sglang       | **200.1s (3.3m)** | `93fa577` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        286.4 |     153.1 | **140.8** |
| TPOT median (ms)          |        152.9 |  **50.1** |      76.4 |
| E2E median (ms)           |        379.0 | **201.0** |     212.9 |
| Throughput median (tok/s) |          4.0 |   **7.2** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        280.0 | **191.8** |  203.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        316.1 | **213.5** |  336.4 |
| Throughput median (tok/s) |          3.2 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        675.8 |     176.9 | **152.1** |
| TPOT median (ms)          |        186.7 |  **62.1** |     106.3 |
| E2E median (ms)           |        776.4 | **234.2** |     250.2 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        360.9 | **58.5** |   80.0 |
| TPOT median (ms)          |        131.8 | **26.4** |   54.9 |
| E2E median (ms)           |        461.0 | **79.3** |  150.7 |
| Throughput median (tok/s) |          3.1 | **15.7** |    9.4 |
| Correctness               |          97% |      98% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        758.6 |      79.0 | **68.1** |
| TPOT median (ms)          |         15.7 |  **15.1** |     22.1 |
| E2E median (ms)           |       1360.8 | **628.9** |    800.0 |
| Throughput median (tok/s) |         26.2 |  **58.0** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        472.4 |     131.9 | **128.8** |
| TPOT median (ms)          |         97.4 |  **30.7** |      51.9 |
| E2E median (ms)           |        658.7 | **271.4** |     350.0 |
| Throughput median (tok/s) |          7.6 |  **18.3** |      13.2 |
| Correctness               |          98% |       99% |       99% |

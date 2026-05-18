# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:09 AM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     346.8s (5.8m) | `c837893` |
| vllm         |   1080.2s (18.0m) | `2e40faf` |
| sglang       | **166.5s (2.8m)** | `f04c522` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        274.5 |    163.8 | **137.3** |
| TPOT median (ms)          |        151.0 | **63.9** |      72.0 |
| E2E median (ms)           |        368.9 |    223.3 | **202.4** |
| Throughput median (tok/s) |          4.1 |  **6.6** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        273.8 |     195.1 | **192.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        300.4 | **256.7** |     328.3 |
| Throughput median (tok/s) |          3.3 |   **3.9** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        522.8 |     168.8 | **156.7** |
| TPOT median (ms)          |        134.2 |  **60.8** |      99.1 |
| E2E median (ms)           |        626.2 | **219.9** |     253.6 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.9 | **58.2** |   75.2 |
| TPOT median (ms)          |        132.1 | **27.0** |   67.4 |
| E2E median (ms)           |        435.9 | **78.6** |  151.3 |
| Throughput median (tok/s) |          3.1 | **15.8** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        695.9 |      66.6 | **64.2** |
| TPOT median (ms)          |         15.6 |  **15.1** |     22.4 |
| E2E median (ms)           |       1302.4 | **622.7** |    836.9 |
| Throughput median (tok/s) |         28.2 |  **58.7** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        421.0 |     130.5 | **125.2** |
| TPOT median (ms)          |         86.6 |  **33.4** |      52.2 |
| E2E median (ms)           |        606.8 | **280.2** |     354.5 |
| Throughput median (tok/s) |          8.2 |  **18.2** |      13.2 |
| Correctness               |          99% |       99% |       99% |

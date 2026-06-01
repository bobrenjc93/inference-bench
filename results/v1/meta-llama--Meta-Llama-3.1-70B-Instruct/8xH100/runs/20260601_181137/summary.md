# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, Jun 1 2026

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
| torchinferno |     324.1s (5.4m) | `1fd9573` |
| vllm         |   1333.8s (22.2m) | `0357335` |
| sglang       | **243.6s (4.1m)** | `f6a5a1b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        204.6 |   160.7 | **147.0** |
| TPOT median (ms)          |     **42.8** |    57.2 |      75.9 |
| E2E median (ms)           |        242.9 |   218.6 | **214.2** |
| Throughput median (tok/s) |          5.4 | **6.7** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        355.5 | **184.6** |  196.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        447.1 | **203.8** |  326.7 |
| Throughput median (tok/s) |          2.2 |   **4.9** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        655.4 |     164.2 | **159.5** |
| TPOT median (ms)          |         73.7 |  **60.3** |     105.0 |
| E2E median (ms)           |        759.6 | **221.1** |     256.7 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        401.2 | **57.3** |   80.2 |
| TPOT median (ms)          |         29.9 | **28.0** |   41.6 |
| E2E median (ms)           |        434.2 | **78.1** |  130.4 |
| Throughput median (tok/s) |          2.8 | **15.9** |   10.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2863.1 |  **64.1** |   74.3 |
| TPOT median (ms)          |         93.6 |  **14.9** |   23.4 |
| E2E median (ms)           |       5601.0 | **597.6** |  867.8 |
| Throughput median (tok/s) |          5.5 |  **59.9** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        896.0 | **126.2** |  131.4 |
| TPOT median (ms)          |         48.0 |  **32.1** |   49.2 |
| E2E median (ms)           |       1497.0 | **263.9** |  359.2 |
| Throughput median (tok/s) |          3.5 |  **18.7** |   12.8 |
| Correctness               |          98% |       99% |    99% |

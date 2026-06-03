# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |   **2/4** |     1/4 |
| self_consistency |          0/4 |       0/4 | **3/4** |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **13/20** |    5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     402.1s (6.7m) | `8ac98e9` |
| vllm         |   1433.0s (23.9m) | `969aec4` |
| sglang       | **256.9s (4.3m)** | `13852d3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.1 |     159.9 | **145.4** |
| TPOT median (ms)          |     **51.2** |      61.9 |      73.2 |
| E2E median (ms)           |        332.3 | **212.6** |     213.4 |
| Throughput median (tok/s) |          3.5 |   **7.1** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        226.3 | 323.9 | **199.4** |
| TPOT median (ms)          |          0.0 |   0.0 |       0.0 |
| E2E median (ms)           |        352.2 | 354.6 | **333.6** |
| Throughput median (tok/s) |          2.8 |   2.8 |   **3.0** |
| Correctness               |         100% |  100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        944.0 |     178.5 | **165.7** |
| TPOT median (ms)          |        170.4 |  **64.6** |     101.7 |
| E2E median (ms)           |       1069.6 | **231.1** |     274.1 |
| Throughput median (tok/s) |          1.2 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        362.1 | **60.5** |   80.8 |
| TPOT median (ms)          |         30.7 | **28.1** |   61.6 |
| E2E median (ms)           |        401.6 | **81.7** |  147.9 |
| Throughput median (tok/s) |          3.6 | **15.1** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        416.2 |  **71.5** |   78.5 |
| TPOT median (ms)          |         36.2 |  **14.8** |   23.0 |
| E2E median (ms)           |       1628.7 | **614.2** |  872.7 |
| Throughput median (tok/s) |         21.1 |  **59.7** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        447.3 |     158.9 | **133.9** |
| TPOT median (ms)          |         57.7 |  **33.9** |      51.9 |
| E2E median (ms)           |        756.9 | **298.9** |     368.3 |
| Throughput median (tok/s) |          6.4 |  **18.1** |      12.6 |
| Correctness               |          99% |       98% |       99% |

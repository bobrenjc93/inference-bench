# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 PM PT, May 23 2026

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
| torchinferno |     294.2s (4.9m) | `9f91b40` |
| vllm         |   1294.3s (21.6m) | `33d7cbe` |
| sglang       | **197.4s (3.3m)** | `af8f669` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        265.3 |    159.5 | **140.7** |
| TPOT median (ms)          |        152.7 | **56.0** |      77.0 |
| E2E median (ms)           |        368.1 |    214.8 | **214.8** |
| Throughput median (tok/s) |          4.1 |  **6.6** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.6 | **187.6** |  211.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        301.7 | **207.4** |  354.7 |
| Throughput median (tok/s) |          3.3 |   **4.8** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        799.2 |     171.5 | **154.1** |
| TPOT median (ms)          |        108.9 |  **61.3** |      98.9 |
| E2E median (ms)           |        882.3 | **222.6** |     256.2 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        332.5 | **57.4** |   77.0 |
| TPOT median (ms)          |        131.7 | **26.6** |   62.5 |
| E2E median (ms)           |        435.4 | **77.5** |  150.5 |
| Throughput median (tok/s) |          3.1 | **15.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        867.8 |      79.9 | **69.2** |
| TPOT median (ms)          |         16.5 |  **15.0** |     21.7 |
| E2E median (ms)           |       1469.8 | **626.1** |    811.8 |
| Throughput median (tok/s) |         23.3 |  **57.9** |     43.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        508.9 |     131.2 | **130.4** |
| TPOT median (ms)          |         82.0 |  **31.8** |      52.0 |
| E2E median (ms)           |        691.5 | **269.7** |     357.6 |
| Throughput median (tok/s) |          7.1 |  **18.3** |      13.2 |
| Correctness               |          98% |       98% |       99% |

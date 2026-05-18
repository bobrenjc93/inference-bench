# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:10 PM PT, May 17 2026

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
| torchinferno |     365.8s (6.1m) | `3f0f3bc` |
| vllm         |   1085.2s (18.1m) | `966903e` |
| sglang       | **165.7s (2.8m)** | `b380316` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        261.5 |     158.6 | **138.1** |
| TPOT median (ms)          |        155.9 |  **53.3** |      75.9 |
| E2E median (ms)           |        367.7 | **200.2** |     207.6 |
| Throughput median (tok/s) |          4.1 |   **7.2** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        223.3 | **194.1** |  197.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        307.4 | **251.6** |  334.7 |
| Throughput median (tok/s) |          3.3 |   **4.0** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        528.8 |     177.6 | **158.1** |
| TPOT median (ms)          |        122.9 |  **65.8** |     108.1 |
| E2E median (ms)           |        624.1 | **234.0** |     265.0 |
| Throughput median (tok/s) |          2.1 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.8 | **58.4** |   73.6 |
| TPOT median (ms)          |        133.2 | **26.2** |   67.6 |
| E2E median (ms)           |        446.0 | **78.5** |  154.1 |
| Throughput median (tok/s) |          3.3 | **15.7** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        659.8 |      68.4 | **67.1** |
| TPOT median (ms)          |         15.2 |  **15.1** |     21.9 |
| E2E median (ms)           |       1196.8 | **606.4** |    814.0 |
| Throughput median (tok/s) |         27.8 |  **58.8** |     43.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        405.1 |     131.4 | **126.9** |
| TPOT median (ms)          |         85.4 |  **32.1** |      54.7 |
| E2E median (ms)           |        588.4 | **274.1** |     355.1 |
| Throughput median (tok/s) |          8.1 |  **18.3** |      13.2 |
| Correctness               |          98% |       99% |       99% |

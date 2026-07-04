# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **2/4** |       1/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **12/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.5s (0.8m)** | `390fed4` |
| vllm         |    188.4s (3.1m) | `67ff0ae` |
| sglang       |    182.0s (3.0m) | `5af1f94` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        177.2 |     148.1 | **143.4** |
| TPOT median (ms)          |     **48.3** |      52.0 |      73.1 |
| E2E median (ms)           |        235.0 | **194.2** |     218.0 |
| Throughput median (tok/s) |          5.7 |   **7.2** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.4 | **151.0** |  215.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |    **162.6** |     258.7 |  381.1 |
| Throughput median (tok/s) |      **6.1** |       3.9 |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        344.2 |     181.5 | **169.1** |
| TPOT median (ms)          |     **59.5** |      61.6 |     106.3 |
| E2E median (ms)           |        400.4 | **231.4** |     270.9 |
| Throughput median (tok/s) |          3.4 |   **5.8** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        129.0 | **64.1** |   74.2 |
| TPOT median (ms)          |         36.3 | **30.6** |   69.3 |
| E2E median (ms)           |        154.0 | **87.9** |  152.5 |
| Throughput median (tok/s) |          8.6 | **13.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        237.7 |      83.6 | **74.5** |
| TPOT median (ms)          |         20.7 |  **15.1** |     22.5 |
| E2E median (ms)           |        963.5 | **650.2** |    855.3 |
| Throughput median (tok/s) |         37.4 |  **57.1** |     40.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        208.1 | **125.7** |  135.4 |
| TPOT median (ms)          |         32.9 |  **31.8** |   54.2 |
| E2E median (ms)           |        383.1 | **284.5** |  375.6 |
| Throughput median (tok/s) |         12.3 |  **17.5** |   12.7 |
| Correctness               |          99% |       99% |    99% |

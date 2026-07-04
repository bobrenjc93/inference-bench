# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **47.9s (0.8m)** | `390fed4` |
| vllm         |    485.7s (8.1m) | `4a6bf3c` |
| sglang       |    345.1s (5.8m) | `754524d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        157.6 |     148.8 | **139.2** |
| TPOT median (ms)          |     **45.9** |      53.9 |      78.1 |
| E2E median (ms)           |        210.3 | **190.8** |     217.2 |
| Throughput median (tok/s) |          5.8 |   **7.3** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        258.1 | **194.3** |  221.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        302.8 | **212.1** |  380.3 |
| Throughput median (tok/s) |          3.3 |   **4.7** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        360.2 |     174.1 | **169.6** |
| TPOT median (ms)          |         62.8 |  **57.6** |     111.6 |
| E2E median (ms)           |        413.2 | **230.3** |     283.1 |
| Throughput median (tok/s) |          3.6 |   **6.2** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        125.0 | **63.6** |   77.6 |
| TPOT median (ms)          |         47.2 | **31.1** |   54.5 |
| E2E median (ms)           |        150.5 | **87.3** |  138.2 |
| Throughput median (tok/s) |          8.6 | **13.7** |   10.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        258.1 |      81.5 | **75.9** |
| TPOT median (ms)          |         20.8 |  **15.0** |     22.4 |
| E2E median (ms)           |        970.1 | **615.0** |    826.4 |
| Throughput median (tok/s) |         36.3 |  **57.8** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        231.8 | **132.5** |  136.8 |
| TPOT median (ms)          |         35.3 |  **31.5** |   53.3 |
| E2E median (ms)           |        409.4 | **267.1** |  369.0 |
| Throughput median (tok/s) |         11.5 |  **17.9** |   12.9 |
| Correctness               |          98% |       99% |    99% |

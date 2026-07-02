# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:52 AM PT, Jul 2 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **2/4** |    1/4 |          1/4 |
| self_consistency |   **2/4** |    1/4 |          0/4 |
| multi_turn       |   **3/4** |    1/4 |          0/4 |
| tree_of_thought  |   **3/4** |    1/4 |          0/4 |
| long_output      |   **3/4** |    1/4 |          0/4 |
| **Total**        | **13/20** |   5/20 |         1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `08a8a4a` |
| sglang       |     0.0s (0.0m) | `b276a9a` |
| torchinferno |     0.0s (0.0m) | `46007b2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     142.8 | **115.7** |        173.0 |
| TPOT median (ms)          |      56.0 |      87.0 |     **51.2** |
| E2E median (ms)           | **194.0** |     203.3 |        214.5 |
| Throughput median (tok/s) |   **7.5** |       5.9 |          5.4 |
| Correctness               |       98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     215.0 | **193.5** |        196.7 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **244.1** |     382.0 |        277.7 |
| Throughput median (tok/s) |   **4.1** |       2.6 |          3.6 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     160.6 | **148.3** |        306.4 |
| TPOT median (ms)          |  **52.8** |     126.1 |         65.7 |
| E2E median (ms)           | **207.1** |     280.2 |        365.3 |
| Throughput median (tok/s) |   **6.6** |       4.7 |          3.3 |
| Correctness               |       98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     64.0 | **58.1** |        158.2 |
| TPOT median (ms)          | **31.5** |     74.2 |         35.0 |
| E2E median (ms)           | **87.3** |    147.6 |        186.8 |
| Throughput median (tok/s) | **14.1** |      9.1 |          6.5 |
| Correctness               |      97% |      97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      63.3 | **60.7** |        271.3 |
| TPOT median (ms)          |  **17.0** |     24.5 |         24.8 |
| E2E median (ms)           | **661.4** |    874.7 |       1192.7 |
| Throughput median (tok/s) |  **53.7** |     38.7 |         31.5 |
| Correctness               |      100% |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     129.1 | **115.3** |        221.1 |
| TPOT median (ms)          |  **31.4** |      62.4 |         35.3 |
| E2E median (ms)           | **278.8** |     377.6 |        447.4 |
| Throughput median (tok/s) |  **17.2** |      12.2 |         10.1 |
| Correctness               |       99% |       99% |          99% |

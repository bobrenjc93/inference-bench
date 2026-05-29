# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, May 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          1/4 |   **3/4** |     0/4 |
| **Total**        |         2/20 | **14/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     388.1s (6.5m) | `6ead340` |
| vllm         |   1292.1s (21.5m) | `0b56815` |
| sglang       | **224.8s (3.7m)** | `ec075d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        242.4 |   166.9 | **142.0** |
| TPOT median (ms)          |     **56.7** |    58.8 |      77.7 |
| E2E median (ms)           |        302.1 |   217.7 | **215.4** |
| Throughput median (tok/s) |          4.6 | **6.7** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.4 | **196.4** |  204.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        343.3 | **220.2** |  336.0 |
| Throughput median (tok/s) |          2.9 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        693.2 |     166.3 | **163.6** |
| TPOT median (ms)          |         60.2 |  **59.6** |      97.7 |
| E2E median (ms)           |        744.9 | **220.0** |     255.3 |
| Throughput median (tok/s) |          1.9 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        184.4 | **57.5** |   77.5 |
| TPOT median (ms)          |         29.8 | **28.1** |   57.3 |
| E2E median (ms)           |        214.2 | **77.7** |  144.9 |
| Throughput median (tok/s) |          6.3 | **15.6** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        529.0 |  **74.4** |   77.9 |
| TPOT median (ms)          |     **14.3** |      14.9 |   23.0 |
| E2E median (ms)           |       1084.7 | **620.1** |  859.8 |
| Throughput median (tok/s) |         30.0 |  **59.2** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        388.7 | **132.3** |  133.0 |
| TPOT median (ms)          |     **32.2** |      32.3 |   51.1 |
| E2E median (ms)           |        537.8 | **271.1** |  362.3 |
| Throughput median (tok/s) |          9.2 |  **18.5** |   12.8 |
| Correctness               |          98% |       98% |    99% |

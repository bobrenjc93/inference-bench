# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     354.1s (5.9m) | `96c9b54` |
| vllm         |     434.7s (7.2m) | `745bba5` |
| sglang       | **239.3s (4.0m)** | `5351800` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        234.8 | **136.2** |  146.4 |
| TPOT median (ms)          |     **44.0** |      47.4 |   76.4 |
| E2E median (ms)           |        274.6 | **172.6** |  218.1 |
| Throughput median (tok/s) |          5.3 |   **8.0** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.1 | **187.5** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        376.3 | **215.3** |  366.4 |
| Throughput median (tok/s) |          2.7 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        503.4 |     161.0 | **159.6** |
| TPOT median (ms)          |     **37.8** |      58.7 |     104.6 |
| E2E median (ms)           |        542.5 | **215.0** |     252.4 |
| Throughput median (tok/s) |          2.3 |   **6.5** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        216.2 | **59.1** |   86.5 |
| TPOT median (ms)          |         31.2 | **29.1** |   46.5 |
| E2E median (ms)           |        248.8 | **80.9** |  150.5 |
| Throughput median (tok/s) |          5.6 | **14.9** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        361.4 |      71.9 | **69.0** |
| TPOT median (ms)          |         21.1 |  **14.9** |     22.2 |
| E2E median (ms)           |       1181.0 | **603.1** |    839.1 |
| Throughput median (tok/s) |         32.0 |  **59.3** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.8 | **123.1** |  135.1 |
| TPOT median (ms)          |     **26.8** |      30.0 |   50.0 |
| E2E median (ms)           |        524.7 | **257.4** |  365.3 |
| Throughput median (tok/s) |          9.6 |  **18.7** |   13.0 |
| Correctness               |          99% |       99% |    98% |

# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          2/4 |       2/4 |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     403.4s (6.7m) | `5680b84` |
| vllm         |     515.7s (8.6m) | `11a1230` |
| sglang       | **275.2s (4.6m)** | `4a76699` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |    **139.1** |    142.0 |  149.9 |
| TPOT median (ms)          |         45.9 | **45.2** |   77.4 |
| E2E median (ms)           |    **177.3** |    177.6 |  223.3 |
| Throughput median (tok/s) |          6.3 |  **8.1** |    5.5 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.8 | **199.0** |  206.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        265.5 | **223.8** |  344.6 |
| Throughput median (tok/s) |          3.8 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        411.7 |     161.7 | **159.0** |
| TPOT median (ms)          |         57.6 |  **49.4** |     107.3 |
| E2E median (ms)           |        466.0 | **200.6** |     263.9 |
| Throughput median (tok/s) |          2.8 |   **6.7** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        295.2 | **60.6** |   78.9 |
| TPOT median (ms)          |         42.4 | **31.7** |   55.2 |
| E2E median (ms)           |        360.6 | **84.4** |  140.7 |
| Throughput median (tok/s) |          3.5 | **14.6** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        310.2 |      72.3 | **68.7** |
| TPOT median (ms)          |         22.3 |  **15.0** |     22.7 |
| E2E median (ms)           |       1190.1 | **600.2** |    848.4 |
| Throughput median (tok/s) |         32.4 |  **59.4** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.0 | **127.1** |  132.7 |
| TPOT median (ms)          |         33.6 |  **28.3** |   52.5 |
| E2E median (ms)           |        491.9 | **257.3** |  364.2 |
| Throughput median (tok/s) |          9.8 |  **18.6** |   13.0 |
| Correctness               |          99% |       99% |    98% |

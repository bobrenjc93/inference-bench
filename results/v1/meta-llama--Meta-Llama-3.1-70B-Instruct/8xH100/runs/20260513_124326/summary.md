# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:01 AM PT, May 13 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.3s (1.5m)** | `acf8b4e` |
| vllm         |  1208.4s (20.1m) | `3b1ef03` |
| sglang       |    174.4s (2.9m) | `4984552` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        429.4 |    174.1 | **142.0** |
| TPOT median (ms)          |        320.2 | **60.7** |      79.1 |
| E2E median (ms)           |        686.1 |    229.3 | **217.0** |
| Throughput median (tok/s) |          2.2 |  **6.5** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        295.5 | **180.3** |  215.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        440.8 | **206.3** |  365.1 |
| Throughput median (tok/s) |          2.3 |   **4.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1401.4 |     191.1 | **168.1** |
| TPOT median (ms)          |        256.3 |  **70.7** |     110.4 |
| E2E median (ms)           |       1614.2 | **253.8** |     276.1 |
| Throughput median (tok/s) |          0.8 |   **5.5** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        474.8 | **60.8** |   81.3 |
| TPOT median (ms)          |        241.6 | **28.4** |   74.5 |
| E2E median (ms)           |        671.5 | **82.6** |  160.3 |
| Throughput median (tok/s) |          2.2 | **15.0** |    8.9 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1019.7 |      77.5 | **73.0** |
| TPOT median (ms)          |         32.3 |  **15.0** |     21.9 |
| E2E median (ms)           |       2426.2 | **647.7** |    845.3 |
| Throughput median (tok/s) |         15.7 |  **57.1** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        724.2 |     136.8 | **135.9** |
| TPOT median (ms)          |        170.1 |  **34.9** |      57.2 |
| E2E median (ms)           |       1167.8 | **283.9** |     372.8 |
| Throughput median (tok/s) |          4.6 |  **17.8** |      12.8 |
| Correctness               |          98% |       99% |       98% |

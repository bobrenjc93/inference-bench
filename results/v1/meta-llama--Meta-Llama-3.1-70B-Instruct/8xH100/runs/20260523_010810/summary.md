# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 PM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     333.3s (5.6m) | `9f91b40` |
| vllm         |   1288.8s (21.5m) | `552bbe6` |
| sglang       | **213.7s (3.6m)** | `c112f76` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        295.1 |    159.2 | **142.6** |
| TPOT median (ms)          |        151.2 | **60.9** |      75.7 |
| E2E median (ms)           |        396.6 |    215.6 | **214.5** |
| Throughput median (tok/s) |          3.9 |  **6.9** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.3 |     207.3 | **200.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        311.7 | **225.9** |     335.9 |
| Throughput median (tok/s) |          3.2 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        706.2 |     172.7 | **153.5** |
| TPOT median (ms)          |        134.8 |  **54.9** |     105.7 |
| E2E median (ms)           |        821.9 | **216.1** |     257.7 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        352.0 | **61.4** |   75.9 |
| TPOT median (ms)          |        132.3 | **28.0** |   58.1 |
| E2E median (ms)           |        458.6 | **84.2** |  148.7 |
| Throughput median (tok/s) |          3.1 | **14.5** |    9.6 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        949.6 |      68.1 | **66.1** |
| TPOT median (ms)          |         19.3 |  **15.0** |     22.3 |
| E2E median (ms)           |       1538.6 | **603.2** |    831.0 |
| Throughput median (tok/s) |         20.2 |  **59.4** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        517.6 |     133.8 | **127.7** |
| TPOT median (ms)          |         87.5 |  **31.8** |      52.4 |
| E2E median (ms)           |        705.5 | **269.0** |     357.6 |
| Throughput median (tok/s) |          6.4 |  **18.3** |      13.2 |
| Correctness               |          99% |       98% |       99% |

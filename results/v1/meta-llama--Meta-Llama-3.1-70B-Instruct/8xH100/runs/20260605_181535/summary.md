# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     435.4s (7.3m) | `89edcfc` |
| vllm         |   1365.0s (22.7m) | `b593396` |
| sglang       | **206.5s (3.4m)** | `57909f7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        356.7 |     163.3 | **155.4** |
| TPOT median (ms)          |     **56.0** |      58.3 |      71.5 |
| E2E median (ms)           |        409.9 | **213.3** |     225.3 |
| Throughput median (tok/s) |          3.2 |   **6.7** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        286.7 |     213.8 | **206.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        392.5 | **305.2** |     339.9 |
| Throughput median (tok/s) |          2.5 |   **3.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        727.8 |     173.2 | **161.2** |
| TPOT median (ms)          |         66.8 |  **51.8** |     104.3 |
| E2E median (ms)           |        793.2 | **224.9** |     262.6 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        437.0 | **62.6** |   79.9 |
| TPOT median (ms)          |         33.6 | **28.6** |   44.2 |
| E2E median (ms)           |        468.7 | **84.4** |  132.8 |
| Throughput median (tok/s) |          2.8 | **14.5** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        553.5 |  **71.0** |   74.9 |
| TPOT median (ms)          |         29.2 |  **14.7** |   23.6 |
| E2E median (ms)           |       1634.7 | **613.5** |  873.9 |
| Throughput median (tok/s) |         23.3 |  **59.3** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        472.4 |     136.8 | **135.6** |
| TPOT median (ms)          |         37.1 |  **30.7** |      48.7 |
| E2E median (ms)           |        739.8 | **288.3** |     366.9 |
| Throughput median (tok/s) |          6.7 |  **18.0** |      12.7 |
| Correctness               |          98% |       99% |       98% |

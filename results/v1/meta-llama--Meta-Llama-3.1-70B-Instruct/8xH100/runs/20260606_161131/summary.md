# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 AM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     344.0s (5.7m) | `75bbe35` |
| vllm         |   1266.5s (21.1m) | `fa27d4e` |
| sglang       | **200.0s (3.3m)** | `bd7fea0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        402.0 | **149.0** |  165.4 |
| TPOT median (ms)          |     **51.0** |      53.0 |   70.7 |
| E2E median (ms)           |        448.3 | **200.2** |  231.0 |
| Throughput median (tok/s) |          3.3 |   **7.3** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.9 | **195.1** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        383.2 | **242.9** |  334.5 |
| Throughput median (tok/s) |          2.6 |   **4.1** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        735.7 |     173.8 | **168.8** |
| TPOT median (ms)          |         64.4 |  **61.7** |     100.3 |
| E2E median (ms)           |        787.3 | **223.1** |     269.5 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        360.6 | **59.4** |   84.0 |
| TPOT median (ms)          |         31.0 | **28.8** |   49.9 |
| E2E median (ms)           |        390.3 | **80.2** |  146.5 |
| Throughput median (tok/s) |          3.5 | **15.0** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        516.5 |  **67.4** |   79.9 |
| TPOT median (ms)          |         30.3 |  **15.1** |   22.9 |
| E2E median (ms)           |       1579.6 | **603.1** |  866.0 |
| Throughput median (tok/s) |         22.8 |  **59.2** |   40.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        459.3 | **128.9** |  140.9 |
| TPOT median (ms)          |         35.3 |  **31.7** |   48.7 |
| E2E median (ms)           |        717.7 | **269.9** |  369.5 |
| Throughput median (tok/s) |          6.8 |  **18.3** |   12.6 |
| Correctness               |          99% |       98% |    99% |

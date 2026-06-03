# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, Jun 2 2026

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
| torchinferno |     344.3s (5.7m) | `650fe5f` |
| vllm         |   1339.1s (22.3m) | `f020435` |
| sglang       | **213.9s (3.6m)** | `ab7c4ab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        355.2 |     160.5 | **140.9** |
| TPOT median (ms)          |     **52.4** |      60.7 |      76.2 |
| E2E median (ms)           |        406.3 | **209.7** |     210.9 |
| Throughput median (tok/s) |          3.3 |   **7.0** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        280.5 |     255.9 | **211.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        392.1 | **291.3** |     346.5 |
| Throughput median (tok/s) |          2.6 |   **3.4** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        774.4 |     171.1 | **157.5** |
| TPOT median (ms)          |        108.6 |  **58.4** |      98.1 |
| E2E median (ms)           |        882.4 | **218.1** |     254.4 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        364.8 | **60.1** |   77.0 |
| TPOT median (ms)          |         30.9 | **27.8** |   56.4 |
| E2E median (ms)           |        388.4 | **81.5** |  146.4 |
| Throughput median (tok/s) |          3.3 | **15.0** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        408.5 |  **72.4** |   75.3 |
| TPOT median (ms)          |         36.3 |  **14.7** |   23.2 |
| E2E median (ms)           |       1671.3 | **605.8** |  892.4 |
| Throughput median (tok/s) |         21.5 |  **59.5** |   40.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        436.7 |     144.0 | **132.4** |
| TPOT median (ms)          |         45.6 |  **32.3** |      50.8 |
| E2E median (ms)           |        748.1 | **281.3** |     370.1 |
| Throughput median (tok/s) |          6.4 |  **18.2** |      12.8 |
| Correctness               |          98% |       98% |       99% |

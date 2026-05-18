# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:10 AM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     306.4s (5.1m) | `c837893` |
| vllm         |   1096.3s (18.3m) | `e414e1f` |
| sglang       | **168.2s (2.8m)** | `f04c522` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        253.7 |    163.4 | **139.7** |
| TPOT median (ms)          |        151.2 | **59.3** |      74.7 |
| E2E median (ms)           |        356.4 |    219.3 | **206.3** |
| Throughput median (tok/s) |          4.2 |  **6.7** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        280.7 | **192.1** |  200.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        317.3 | **215.4** |  335.1 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        528.1 |     171.6 | **155.2** |
| TPOT median (ms)          |        119.6 |  **60.9** |     101.4 |
| E2E median (ms)           |        619.3 | **222.9** |     255.2 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        345.9 | **58.6** |   75.2 |
| TPOT median (ms)          |        131.2 | **26.8** |   69.1 |
| E2E median (ms)           |        442.1 | **78.8** |  151.0 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        683.1 |  **67.4** |   68.1 |
| TPOT median (ms)          |     **15.0** |      15.1 |   22.1 |
| E2E median (ms)           |       1196.5 | **615.6** |  808.9 |
| Throughput median (tok/s) |         30.3 |  **58.5** |   42.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        418.3 |     130.6 | **127.8** |
| TPOT median (ms)          |         83.4 |  **32.4** |      53.5 |
| E2E median (ms)           |        586.3 | **270.4** |     351.3 |
| Throughput median (tok/s) |          8.5 |  **18.3** |      13.2 |
| Correctness               |          98% |       98% |       99% |

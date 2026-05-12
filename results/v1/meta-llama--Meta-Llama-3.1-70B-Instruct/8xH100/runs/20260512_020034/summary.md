# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:05 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          0/4 |   **2/4** | **2/4** |
| self_consistency |          1/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         1/20 | **15/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     250.1s (4.2m) | `4af2371` |
| vllm         |    946.2s (15.8m) | `39dff5f` |
| sglang       | **161.7s (2.7m)** | `5495026` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        501.4 |    160.4 | **134.9** |
| TPOT median (ms)          |        435.1 | **54.7** |      77.1 |
| E2E median (ms)           |        805.1 |    210.7 | **207.4** |
| Throughput median (tok/s) |          1.7 |  **7.1** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        331.0 | **182.4** |  211.7 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        495.9 | **204.8** |  355.4 |
| Throughput median (tok/s) |          2.0 |   **4.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        676.1 |     171.0 | **158.2** |
| TPOT median (ms)          |        506.9 |  **57.0** |     105.8 |
| E2E median (ms)           |       1101.7 | **226.0** |     257.8 |
| Throughput median (tok/s) |          1.1 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        369.1 | **59.1** |   78.0 |
| TPOT median (ms)          |        378.5 | **26.5** |   65.4 |
| E2E median (ms)           |        701.8 | **79.1** |  157.6 |
| Throughput median (tok/s) |          2.0 | **15.7** |    9.1 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        579.1 |      68.5 | **66.1** |
| TPOT median (ms)          |         32.4 |  **15.0** |     22.4 |
| E2E median (ms)           |       2082.5 | **603.3** |    847.9 |
| Throughput median (tok/s) |         20.5 |  **59.7** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        491.4 | **128.3** |  129.8 |
| TPOT median (ms)          |        270.6 |  **30.6** |   54.2 |
| E2E median (ms)           |       1037.4 | **264.8** |  365.2 |
| Throughput median (tok/s) |          5.5 |  **18.7** |   13.0 |
| Correctness               |          98% |       98% |    99% |

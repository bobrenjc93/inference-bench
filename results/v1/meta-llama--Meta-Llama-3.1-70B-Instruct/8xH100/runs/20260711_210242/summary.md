# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **12/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.9s (0.6m)** | `a8874cd` |
| vllm         |    252.7s (4.2m) | `1ef1c7e` |
| sglang       |    155.0s (2.6m) | `d8ef766` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        139.6 |      86.3 | **76.8** |
| TPOT median (ms)          |     **32.1** |      41.6 |     65.1 |
| E2E median (ms)           |        165.1 | **118.0** |    131.3 |
| Throughput median (tok/s) |          7.0 |  **11.0** |     10.4 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **66.0** | 74.8 |  122.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **82.0** | 93.6 |  207.4 |
| Throughput median (tok/s) |     **12.2** | 10.7 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        190.4 |      84.4 | **84.1** |
| TPOT median (ms)          |     **35.4** |      36.2 |     66.7 |
| E2E median (ms)           |        219.6 | **115.4** |    141.0 |
| Throughput median (tok/s) |          5.1 |  **11.5** |      9.7 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.3 | **36.9** |   52.6 |
| TPOT median (ms)          |         34.7 | **24.5** |  417.4 |
| E2E median (ms)           |         72.5 | **55.1** |  441.6 |
| Throughput median (tok/s) |         19.8 | **23.5** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.9 |  **48.5** |   52.4 |
| TPOT median (ms)          |         19.5 |  **15.3** |   24.8 |
| E2E median (ms)           |        855.4 | **578.5** |  941.2 |
| Throughput median (tok/s) |         40.9 |  **60.8** |   38.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.3 |  **66.2** |   77.7 |
| TPOT median (ms)          |         24.3 |  **23.5** |  114.8 |
| E2E median (ms)           |        278.9 | **192.1** |  372.5 |
| Throughput median (tok/s) |         17.0 |  **23.5** |   13.4 |
| Correctness               |          99% |       99% |    99% |

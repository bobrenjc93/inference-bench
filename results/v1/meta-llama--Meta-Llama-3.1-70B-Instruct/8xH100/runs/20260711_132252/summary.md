# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:22 AM PT, Jul 11 2026

## Integrity Warnings

- **torchinferno:** TorchInferno queue profile reports generated-prefix logits reuse (generated-prefix reuse requests=997, reuse tokens=55832, generated-prefix route count=997). Treat TorchInferno score-facing metrics in this run as not comparable; normal KV prefix reuse is still allowed.

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.7s (0.7m)** | `9af4c72` |
| vllm         |    303.6s (5.1m) | `19069bc` |
| sglang       |    209.9s (3.5m) | `32cb89d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        139.6 | **71.1** |   79.8 |
| TPOT median (ms)          |     **33.1** |     34.6 |   64.4 |
| E2E median (ms)           |        165.3 | **95.3** |  135.6 |
| Throughput median (tok/s) |          7.2 | **14.1** |   10.1 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **25.7** | 66.0 |  122.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **26.4** | 81.6 |  208.5 |
| Throughput median (tok/s) |     **37.8** | 12.2 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        189.6 |      90.6 | **84.4** |
| TPOT median (ms)          |     **35.4** |      54.9 |     67.4 |
| E2E median (ms)           |        218.2 | **126.4** |    141.3 |
| Throughput median (tok/s) |          5.2 |  **11.0** |      9.1 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.9 | **32.4** |   52.8 |
| TPOT median (ms)          |         35.1 | **21.6** |  397.8 |
| E2E median (ms)           |         75.1 | **48.0** |  464.9 |
| Throughput median (tok/s) |         19.3 | **26.3** |    3.1 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.7 |  **43.9** |   51.7 |
| TPOT median (ms)          |         19.0 |  **14.7** |   25.1 |
| E2E median (ms)           |        873.4 | **556.5** |  994.8 |
| Throughput median (tok/s) |         41.0 |  **63.4** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        119.3 |  **60.8** |   78.2 |
| TPOT median (ms)          |     **24.5** |      25.2 |  110.9 |
| E2E median (ms)           |        271.7 | **181.6** |  389.0 |
| Throughput median (tok/s) |         22.1 |  **25.4** |   13.1 |
| Correctness               |          99% |       98% |    98% |

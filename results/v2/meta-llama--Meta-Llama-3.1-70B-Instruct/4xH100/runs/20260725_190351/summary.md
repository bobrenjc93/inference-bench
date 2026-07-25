# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `e7c2e308f4dea8d484a14ae43fccd3cd5eaa1d2c`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`12e0c166d9eeb083a004217ea15e60b556bd7f1e`; vllm=`70009fb9344d2a7ba642e68369e0a64a6252e8bc` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`659d349b61724f8eb368df2b96c8adce0f6396c6` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 PM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          2/4 |       2/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         7/20 | **11/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     447.1s (7.5m) | `12e0c16` |
| vllm         |     230.0s (3.8m) | `70009fb` |
| sglang       | **195.3s (3.3m)** | `659d349` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.0** |    109.2 |   80.3 |
| TPOT median (ms)          |         72.4 | **51.0** |   83.8 |
| E2E median (ms)           |    **125.6** |    155.4 |  140.8 |
| Throughput median (tok/s) |          9.5 |  **9.9** |    9.4 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.6** | 113.8 |  135.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **90.8** | 134.0 |  215.0 |
| Throughput median (tok/s) |     **11.0** |   7.5 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.3** |    104.2 |   86.4 |
| TPOT median (ms)          |         74.7 | **61.3** |   83.2 |
| E2E median (ms)           |    **126.6** |    147.1 |  154.0 |
| Throughput median (tok/s) |          9.2 |  **9.7** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.1 | **50.0** |   57.6 |
| TPOT median (ms)          |         41.2 | **34.5** |  125.6 |
| E2E median (ms)           |        101.6 | **75.4** |  204.8 |
| Throughput median (tok/s) |         12.8 | **16.3** |    6.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.6 |      62.9 | **56.5** |
| TPOT median (ms)          |         26.0 |  **21.3** |     31.2 |
| E2E median (ms)           |       1002.9 | **814.4** |   1110.7 |
| Throughput median (tok/s) |         36.1 |  **43.6** |     31.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.5** |      88.0 |   83.2 |
| TPOT median (ms)          |         42.9 |  **33.6** |   64.8 |
| E2E median (ms)           |        289.5 | **265.2** |  365.1 |
| Throughput median (tok/s) |         15.7 |  **17.4** |   12.2 |
| Correctness               |          99% |       98% |    99% |

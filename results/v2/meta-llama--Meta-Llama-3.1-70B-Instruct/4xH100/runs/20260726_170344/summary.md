# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `b8a25a039a7b6b1f89eaab67cddf946ca72693ee`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`b68d7ef2622d2d22e964dd842381021865e942b8` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`e14068d161a7de7b70bf309716e1df86830e208e` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:03 AM PT, Jul 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         7/20 | **10/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     351.0s (5.9m) | `b2bb774` |
| vllm         |     217.3s (3.6m) | `b68d7ef` |
| sglang       | **196.1s (3.3m)** | `e14068d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |  sglang |
| :------------------------ | -----------: | -------: | ------: |
| TTFT median (ms)          |     **76.2** |     97.6 |    79.1 |
| TPOT median (ms)          |         72.9 | **59.3** |    73.4 |
| E2E median (ms)           |    **122.1** |    145.4 |   138.5 |
| Throughput median (tok/s) |          9.6 |      9.3 | **9.6** |
| Correctness               |          98% |      98% |     98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **79.4** | 108.4 |  133.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **106.6** | 128.0 |  209.6 |
| Throughput median (tok/s) |      **9.4** |   7.8 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **79.1** |    100.3 |   83.6 |
| TPOT median (ms)          |         76.7 | **62.5** |   79.0 |
| E2E median (ms)           |    **126.1** |    141.7 |  149.8 |
| Throughput median (tok/s) |          9.1 |  **9.7** |    9.1 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.4 | **50.1** |   54.4 |
| TPOT median (ms)          |         41.7 | **34.8** |  129.7 |
| E2E median (ms)           |        102.0 | **75.3** |  206.5 |
| Throughput median (tok/s) |         12.6 | **16.3** |    6.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         78.3 |      62.4 | **54.9** |
| TPOT median (ms)          |         26.1 |  **21.1** |     30.2 |
| E2E median (ms)           |       1031.9 | **812.0** |   1072.4 |
| Throughput median (tok/s) |         36.0 |  **43.9** |     32.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **75.7** |      83.8 |   81.1 |
| TPOT median (ms)          |         43.5 |  **35.5** |   62.4 |
| E2E median (ms)           |        297.7 | **260.5** |  355.4 |
| Throughput median (tok/s) |         15.3 |  **17.4** |   12.5 |
| Correctness               |          99% |       99% |    98% |

# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `8ca1ecd8ae62633e5e532e8454ce337c916a16c9`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b885a36f7b919ae06b73e2ec582df8363b990f8f`; vllm=`9321aff536c1a73f0a7fefc68aef1f2630a904cc` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`9791fc70903b1144687571d7ac748fdf025ae1ec` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:03 AM PT, Jul 25 2026

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
| torchinferno |     391.4s (6.5m) | `b885a36` |
| vllm         |     240.8s (4.0m) | `9321aff` |
| sglang       | **202.6s (3.4m)** | `9791fc7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |  sglang |
| :------------------------ | -----------: | -------: | ------: |
| TTFT median (ms)          |     **76.2** |     96.1 |    80.5 |
| TPOT median (ms)          |         72.6 | **58.5** |    73.1 |
| E2E median (ms)           |    **123.1** |    144.4 |   141.0 |
| Throughput median (tok/s) |          9.4 |      9.5 | **9.6** |
| Correctness               |          98% |      98% |     98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.7** | 115.7 |  137.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **93.1** | 136.3 |  214.1 |
| Throughput median (tok/s) |     **10.7** |   7.3 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.2** |    100.4 |   86.3 |
| TPOT median (ms)          |         74.7 | **58.0** |   88.1 |
| E2E median (ms)           |    **127.2** |    141.6 |  154.3 |
| Throughput median (tok/s) |          9.2 |  **9.5** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         67.1 | **49.5** |   56.3 |
| TPOT median (ms)          |         41.8 | **34.5** |  128.9 |
| E2E median (ms)           |        108.0 | **73.6** |  211.0 |
| Throughput median (tok/s) |         12.3 | **16.5** |    6.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         78.8 |      62.9 | **55.5** |
| TPOT median (ms)          |         26.0 |  **21.2** |     31.9 |
| E2E median (ms)           |       1007.2 | **810.8** |   1118.9 |
| Throughput median (tok/s) |         36.2 |  **43.7** |     30.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.8** |      84.9 |   83.3 |
| TPOT median (ms)          |         43.0 |  **34.4** |   64.4 |
| E2E median (ms)           |        291.7 | **261.3** |  367.9 |
| Throughput median (tok/s) |         15.6 |  **17.3** |   12.1 |
| Correctness               |          99% |       98% |    98% |

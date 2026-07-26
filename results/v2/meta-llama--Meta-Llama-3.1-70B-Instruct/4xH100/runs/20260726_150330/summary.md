# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `8aeb3068f266e150969a10b2589c034d59cfe611`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`7154856f3dcb1d3fdd5a136f7d2c5987f22244f5` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`e14068d161a7de7b70bf309716e1df86830e208e` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 AM PT, Jul 26 2026

## Scorecard

| Benchmark        | torchinferno |    vllm | sglang |
| :--------------- | -----------: | ------: | -----: |
| few_shot         |      **3/4** |     1/4 |    0/4 |
| self_consistency |      **3/4** |     0/4 |    0/4 |
| multi_turn       |      **3/4** |     1/4 |    0/4 |
| tree_of_thought  |          0/4 | **4/4** |    0/4 |
| long_output      |          0/4 | **3/4** |    1/4 |
| **Total**        |         9/20 |    9/20 |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     410.1s (6.8m) | `b2bb774` |
| vllm         |     200.6s (3.3m) | `7154856` |
| sglang       | **195.8s (3.3m)** | `e14068d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.4** |    101.0 |   83.7 |
| TPOT median (ms)          |         72.8 | **59.2** |   74.4 |
| E2E median (ms)           |    **122.7** |    148.0 |  143.5 |
| Throughput median (tok/s) |      **9.7** |      9.2 |    9.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **60.5** | 106.1 |  140.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **88.4** | 125.8 |  214.4 |
| Throughput median (tok/s) |     **11.3** |   8.0 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.1** |    102.6 |   87.8 |
| TPOT median (ms)          |         74.9 | **58.4** |   85.1 |
| E2E median (ms)           |    **123.9** |    148.2 |  155.2 |
| Throughput median (tok/s) |     **10.0** |      9.8 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.1 | **49.7** |   59.5 |
| TPOT median (ms)          |         41.2 | **34.7** |  116.9 |
| E2E median (ms)           |        102.0 | **74.4** |  220.6 |
| Throughput median (tok/s) |         13.0 | **16.3** |    6.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         78.2 |      63.2 | **57.7** |
| TPOT median (ms)          |         26.1 |  **21.4** |     30.7 |
| E2E median (ms)           |       1051.1 | **821.1** |   1097.7 |
| Throughput median (tok/s) |         36.0 |  **43.4** |     31.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **71.5** |      84.5 |   85.8 |
| TPOT median (ms)          |         43.0 |  **34.7** |   61.4 |
| E2E median (ms)           |        297.6 | **263.5** |  366.3 |
| Throughput median (tok/s) |         16.0 |  **17.3** |   12.1 |
| Correctness               |          98% |       98% |    99% |

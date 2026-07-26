# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `16012f87ee09b350792010dd1bba13510d2c139d`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`3f1d40960fb79e6f1314755abf2d43d142e33363` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`e14068d161a7de7b70bf309716e1df86830e208e` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 AM PT, Jul 26 2026

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
| torchinferno |     371.0s (6.2m) | `b2bb774` |
| vllm         |     198.1s (3.3m) | `3f1d409` |
| sglang       | **197.4s (3.3m)** | `e14068d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.6** |    104.3 |   82.0 |
| TPOT median (ms)          |         73.3 | **55.2** |   74.2 |
| E2E median (ms)           |    **122.7** |    153.2 |  141.9 |
| Throughput median (tok/s) |      **9.6** |      9.4 |    9.1 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **81.4** | 106.1 |  138.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **109.8** | 124.6 |  208.0 |
| Throughput median (tok/s) |      **9.1** |   8.0 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.2** |    103.6 |   87.5 |
| TPOT median (ms)          |         76.0 | **65.1** |   80.3 |
| E2E median (ms)           |    **124.2** |    146.5 |  154.0 |
| Throughput median (tok/s) |      **9.3** |      9.1 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         64.7 | **49.7** |   56.4 |
| TPOT median (ms)          |         41.5 | **34.7** |  109.8 |
| E2E median (ms)           |        101.1 | **74.3** |  207.9 |
| Throughput median (tok/s) |         12.7 | **16.5** |    6.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.1 |      63.2 | **55.2** |
| TPOT median (ms)          |         26.1 |  **21.3** |     30.7 |
| E2E median (ms)           |       1031.4 | **815.1** |   1083.9 |
| Throughput median (tok/s) |         36.0 |  **43.6** |     31.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **76.0** |      85.4 |   83.8 |
| TPOT median (ms)          |         43.3 |  **35.2** |   59.0 |
| E2E median (ms)           |        297.8 | **262.7** |  359.1 |
| Throughput median (tok/s) |         15.3 |  **17.3** |   12.2 |
| Correctness               |          99% |       98% |    99% |

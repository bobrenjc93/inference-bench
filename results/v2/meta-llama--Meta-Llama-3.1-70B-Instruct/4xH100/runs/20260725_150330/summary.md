# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `2a2ef31b9cf87c4358f180a203253bdfe8e3ab9e`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`db30bee1ce57016983d4526883e75e516639768a`; vllm=`0b0bd2b5f6a7f15ef59621efe6e535b54c6348f9` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`69a3c54c7023d1cdcc15e16131a3d6ef128f430d` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 AM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |    vllm | sglang |
| :--------------- | -----------: | ------: | -----: |
| few_shot         |      **3/4** |     1/4 |    0/4 |
| self_consistency |      **3/4** |     0/4 |    0/4 |
| multi_turn       |      **4/4** |     0/4 |    0/4 |
| tree_of_thought  |          0/4 | **4/4** |    0/4 |
| long_output      |          0/4 | **3/4** |    1/4 |
| **Total**        |    **10/20** |    8/20 |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     403.3s (6.7m) | `db30bee` |
| vllm         |     200.9s (3.3m) | `0b0bd2b` |
| sglang       | **197.7s (3.3m)** | `69a3c54` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **74.9** |    100.0 |   85.2 |
| TPOT median (ms)          |         71.0 | **56.1** |   75.0 |
| E2E median (ms)           |    **129.0** |    147.8 |  146.1 |
| Throughput median (tok/s) |      **9.7** |      9.5 |    9.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **62.8** | 113.9 |  134.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **91.1** | 131.9 |  207.7 |
| Throughput median (tok/s) |     **11.0** |   7.6 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.6** | 102.5 |   86.2 |
| TPOT median (ms)          |     **63.0** |  64.5 |   82.3 |
| E2E median (ms)           |    **127.9** | 145.5 |  151.8 |
| Throughput median (tok/s) |     **10.4** |   9.3 |    8.9 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         63.7 | **49.5** |   57.2 |
| TPOT median (ms)          |         41.1 | **34.4** |  142.3 |
| E2E median (ms)           |         99.9 | **74.1** |  227.0 |
| Throughput median (tok/s) |         12.9 | **16.4** |    6.1 |
| Correctness               |          98% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.0 |      63.0 | **57.2** |
| TPOT median (ms)          |         25.1 |  **21.4** |     30.7 |
| E2E median (ms)           |        985.9 | **813.7** |   1093.7 |
| Throughput median (tok/s) |         37.0 |  **43.5** |     31.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **69.8** |      85.8 |   84.1 |
| TPOT median (ms)          |         40.0 |  **35.3** |   66.1 |
| E2E median (ms)           |        286.8 | **262.6** |  365.2 |
| Throughput median (tok/s) |         16.2 |  **17.2** |   12.1 |
| Correctness               |          99% |       98% |    98% |

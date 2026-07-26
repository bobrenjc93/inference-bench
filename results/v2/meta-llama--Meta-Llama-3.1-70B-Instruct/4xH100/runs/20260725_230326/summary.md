# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `66064b9de4ca6e9066b774eeee8595127e845ea2`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`d30b1ecd1bdf7c3d92f3b444c4538efd8fbb40ac` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`2c63a2f12b0114bf1e8454721e7db8112c28ed9f` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 PM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         8/20 | **10/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     257.9s (4.3m) | `b2bb774` |
| vllm         | **195.8s (3.3m)** | `d30b1ec` |
| sglang       |     196.9s (3.3m) | `2c63a2f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **75.8** |    102.0 |   84.3 |
| TPOT median (ms)          |         71.4 | **55.4** |   72.7 |
| E2E median (ms)           |    **122.4** |    149.9 |  148.1 |
| Throughput median (tok/s) |      **9.8** |      9.5 |    8.9 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **77.2** | 118.0 |  138.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **105.6** | 138.7 |  209.9 |
| Throughput median (tok/s) |      **9.5** |   7.2 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.5** |    100.3 |   85.1 |
| TPOT median (ms)          |         75.9 | **62.9** |   80.3 |
| E2E median (ms)           |    **125.0** |    143.2 |  152.9 |
| Throughput median (tok/s) |          9.2 |  **9.4** |    8.9 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         66.6 | **50.0** |   57.4 |
| TPOT median (ms)          |         41.5 | **34.9** |  126.5 |
| E2E median (ms)           |        104.8 | **74.4** |  215.2 |
| Throughput median (tok/s) |         12.4 | **16.4** |    6.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         80.8 |      63.0 | **56.7** |
| TPOT median (ms)          |         26.0 |  **21.4** |     31.1 |
| E2E median (ms)           |       1035.2 | **820.1** |   1112.9 |
| Throughput median (tok/s) |         36.1 |  **43.5** |     31.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **75.8** |      86.7 |   84.5 |
| TPOT median (ms)          |         43.0 |  **34.9** |   62.1 |
| E2E median (ms)           |        298.6 | **265.3** |  367.8 |
| Throughput median (tok/s) |         15.4 |  **17.2** |   12.1 |
| Correctness               |          99% |       98% |    98% |

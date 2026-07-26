# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `8d18869c9b595c6ec340912057839be87c14957f`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`30b0714031ae24f77832099cf120576dae28b17c` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`2cbddb842d67b7d16f04c5a7856a0ff9bddc7767` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:03 PM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          2/4 |       2/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |      **3/4** |       1/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         8/20 | **10/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     345.6s (5.8m) | `b2bb774` |
| vllm         | **196.7s (3.3m)** | `30b0714` |
| sglang       |     198.6s (3.3m) | `2cbddb8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.9** |    107.3 |   84.4 |
| TPOT median (ms)          |         74.0 | **55.9** |   83.9 |
| E2E median (ms)           |    **124.5** |    157.4 |  147.3 |
| Throughput median (tok/s) |          9.5 |  **9.6** |    9.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **62.6** | 117.2 |  136.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **89.8** | 136.7 |  213.7 |
| Throughput median (tok/s) |     **11.1** |   7.3 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.0** |    101.5 |   86.4 |
| TPOT median (ms)          |         74.0 | **64.5** |   83.4 |
| E2E median (ms)           |    **122.4** |    144.1 |  155.4 |
| Throughput median (tok/s) |     **10.0** |      9.2 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.2 | **50.2** |   55.2 |
| TPOT median (ms)          |         41.5 | **34.7** |  123.3 |
| E2E median (ms)           |        101.9 | **74.9** |  221.5 |
| Throughput median (tok/s) |         12.8 | **16.3** |    6.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.2 |      63.4 | **56.7** |
| TPOT median (ms)          |         26.1 |  **21.4** |     30.7 |
| E2E median (ms)           |       1048.2 | **820.2** |   1120.9 |
| Throughput median (tok/s) |         36.0 |  **43.3** |     31.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.2** |      87.9 |   83.8 |
| TPOT median (ms)          |         43.1 |  **35.3** |   64.2 |
| E2E median (ms)           |        297.4 | **266.7** |  371.7 |
| Throughput median (tok/s) |         15.9 |  **17.2** |   12.1 |
| Correctness               |          99% |       98% |    99% |

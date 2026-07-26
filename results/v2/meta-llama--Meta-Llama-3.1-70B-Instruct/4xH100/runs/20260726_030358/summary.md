# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `0564e3632c59eac6f23eda64cfef7379b123bfe4`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`1240c74c0a47473449cf0c3a9c2d87a1e159f73b` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`2cbddb842d67b7d16f04c5a7856a0ff9bddc7767` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:03 PM PT, Jul 25 2026

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
| torchinferno |     525.6s (8.8m) | `b2bb774` |
| vllm         |     217.4s (3.6m) | `1240c74` |
| sglang       | **196.8s (3.3m)** | `2cbddb8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.0** |    101.1 |   82.3 |
| TPOT median (ms)          |         73.2 | **56.3** |   70.0 |
| E2E median (ms)           |    **122.1** |    151.5 |  142.5 |
| Throughput median (tok/s) |      **9.7** |      9.6 |    9.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.8** | 111.3 |  133.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **90.9** | 130.1 |  213.1 |
| Throughput median (tok/s) |     **11.0** |   7.7 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.7** |     98.9 |   84.5 |
| TPOT median (ms)          |         75.3 | **62.4** |   82.7 |
| E2E median (ms)           |    **122.6** |    142.7 |  153.1 |
| Throughput median (tok/s) |      **9.9** |      9.6 |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.1 | **49.9** |   57.4 |
| TPOT median (ms)          |         41.8 | **34.5** |  131.9 |
| E2E median (ms)           |        103.5 | **74.8** |  208.0 |
| Throughput median (tok/s) |         12.8 | **16.3** |    6.6 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         80.0 |      63.0 | **56.5** |
| TPOT median (ms)          |         25.9 |  **21.3** |     31.0 |
| E2E median (ms)           |       1051.0 | **812.9** |   1113.2 |
| Throughput median (tok/s) |         36.3 |  **43.6** |     31.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.5** |      84.8 |   82.9 |
| TPOT median (ms)          |         43.2 |  **34.9** |   63.1 |
| E2E median (ms)           |        298.0 | **262.4** |  366.0 |
| Throughput median (tok/s) |         15.9 |  **17.4** |   12.2 |
| Correctness               |          98% |       98% |    98% |

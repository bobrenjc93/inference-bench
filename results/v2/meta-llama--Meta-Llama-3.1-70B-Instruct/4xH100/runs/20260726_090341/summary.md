# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `823c4738d34dbd8ace8c920709bd0bbe861f1e6a`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`da3a252fd13f51c22657bfc8650936f2fbb5b6f3` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`61057bda6c4b8cda1117d74f100d0735645c0cfb` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:03 AM PT, Jul 26 2026

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
| torchinferno |     404.1s (6.7m) | `b2bb774` |
| vllm         |     205.7s (3.4m) | `da3a252` |
| sglang       | **195.0s (3.3m)** | `61057bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.1** |    101.4 |   80.6 |
| TPOT median (ms)          |         73.7 | **58.6** |   71.3 |
| E2E median (ms)           |    **123.7** |    150.7 |  142.3 |
| Throughput median (tok/s) |      **9.6** |      9.1 |    9.4 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **60.7** | 108.1 |  132.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **87.1** | 128.5 |  209.4 |
| Throughput median (tok/s) |     **11.5** |   7.8 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.8** |    100.5 |   84.8 |
| TPOT median (ms)          |         74.7 | **64.8** |   87.0 |
| E2E median (ms)           |    **124.5** |    142.7 |  152.7 |
| Throughput median (tok/s) |      **9.8** |      9.4 |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.6 | **50.2** |   57.2 |
| TPOT median (ms)          |         41.7 | **34.8** |  130.3 |
| E2E median (ms)           |        104.8 | **74.9** |  215.7 |
| Throughput median (tok/s) |         13.0 | **16.2** |    6.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         80.6 |      63.3 | **56.2** |
| TPOT median (ms)          |         25.9 |  **21.5** |     31.5 |
| E2E median (ms)           |       1054.2 | **822.4** |   1135.1 |
| Throughput median (tok/s) |         36.0 |  **43.5** |     30.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.4** |      84.7 |   82.3 |
| TPOT median (ms)          |         43.2 |  **35.9** |   64.0 |
| E2E median (ms)           |        298.9 | **263.8** |  371.1 |
| Throughput median (tok/s) |         16.0 |  **17.2** |   12.1 |
| Correctness               |          99% |       98% |    98% |

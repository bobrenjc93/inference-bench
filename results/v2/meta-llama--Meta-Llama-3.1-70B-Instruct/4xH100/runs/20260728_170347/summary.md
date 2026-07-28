# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `fca7d65540170dc920443ed914e852d39a7d1b77`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`6c7e679f048dc6123caecc3985150766e455ff22` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`4e5a05148a2b3cc55eadbf48ff39c99a94546a35` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:03 AM PT, Jul 28 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **4/4** |  0/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **19/20** | 0/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     472.8s (7.9m) | `ed3588b` |
| vllm         | **201.6s (3.4m)** | `6c7e679` |
| sglang       |     225.1s (3.8m) | `4e5a051` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.7** | 100.9 |   83.6 |
| TPOT median (ms)          |     **51.9** |  57.1 |   75.4 |
| E2E median (ms)           |    **110.1** | 151.4 |  144.6 |
| Throughput median (tok/s) |     **12.6** |   9.5 |    9.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **54.4** | 128.3 |  141.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **78.5** | 147.6 |  216.4 |
| Throughput median (tok/s) |     **12.7** |   6.8 |    4.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.8** |  99.6 |   86.1 |
| TPOT median (ms)          |     **51.9** |  61.9 |   80.0 |
| E2E median (ms)           |    **108.5** | 139.1 |  153.7 |
| Throughput median (tok/s) |     **12.5** |   9.8 |    9.0 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.5** | 49.3 |   60.9 |
| TPOT median (ms)          |     **26.7** | 34.3 |  126.8 |
| E2E median (ms)           |     **69.0** | 74.0 |  225.0 |
| Throughput median (tok/s) |     **18.8** | 16.5 |    6.3 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **48.9** |  62.7 |   58.2 |
| TPOT median (ms)          |     **18.6** |  21.3 |   31.3 |
| E2E median (ms)           |    **705.4** | 813.0 | 1136.4 |
| Throughput median (tok/s) |     **50.6** |  43.6 |   31.2 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **57.3** |  88.2 |   86.0 |
| TPOT median (ms)          |     **29.8** |  34.9 |   62.7 |
| E2E median (ms)           |    **214.3** | 265.0 |  375.2 |
| Throughput median (tok/s) |     **21.4** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    98% |

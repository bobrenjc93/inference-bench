# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `a984bcbe1a65095312367753092f0cf51eaa8576`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`d2bfc6fe20343c638840c8867c29f7365fe23378` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`32c30c0f96fff5ce18aeb8d7e80aa7d1b0d9a49c` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 AM PT, Jul 28 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **4/4** |  0/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **18/20** | 1/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     362.0s (6.0m) | `ed3588b` |
| vllm         |     215.8s (3.6m) | `d2bfc6f` |
| sglang       | **177.9s (3.0m)** | `32c30c0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **68.4** |    107.2 |   80.0 |
| TPOT median (ms)          |         52.5 | **50.0** |   77.0 |
| E2E median (ms)           |    **110.5** |    154.7 |  141.2 |
| Throughput median (tok/s) |     **12.5** |      9.3 |    9.4 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **61.5** | 119.6 |  140.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **84.8** | 139.3 |  217.0 |
| Throughput median (tok/s) |     **11.8** |   7.2 |    4.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.9** | 112.7 |   87.3 |
| TPOT median (ms)          |     **51.5** |  62.7 |   87.1 |
| E2E median (ms)           |    **109.4** | 148.1 |  155.0 |
| Throughput median (tok/s) |     **12.6** |   9.3 |    8.5 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.5** | 50.4 |   56.9 |
| TPOT median (ms)          |     **26.7** | 34.8 |  125.6 |
| E2E median (ms)           |     **69.6** | 74.7 |  207.3 |
| Throughput median (tok/s) |     **19.5** | 16.2 |    6.7 |
| Correctness               |          96% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.3** |  62.3 |   56.4 |
| TPOT median (ms)          |     **18.3** |  21.1 |   31.5 |
| E2E median (ms)           |    **710.3** | 808.2 | 1122.1 |
| Throughput median (tok/s) |     **51.0** |  44.0 |   31.0 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **58.5** |  90.4 |   84.2 |
| TPOT median (ms)          |     **29.8** |  33.7 |   64.2 |
| E2E median (ms)           |    **216.9** | 265.0 |  368.5 |
| Throughput median (tok/s) |     **21.5** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    99% |

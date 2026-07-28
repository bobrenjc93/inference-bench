# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `f4cd290bb72d276949c8b62b3b92da379a446c30`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`90245f4190a35593a625e4bc349485c39c774d39` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`fc8b328f5cb526fd1fa2c26cb3dafe3761af8d5d` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:05 PM PT, Jul 27 2026

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
| torchinferno |     347.8s (5.8m) | `ed3588b` |
| vllm         |     211.9s (3.5m) | `90245f4` |
| sglang       | **197.8s (3.3m)** | `fc8b328` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.0** | 105.8 |   80.8 |
| TPOT median (ms)          |     **52.5** |  54.5 |   75.4 |
| E2E median (ms)           |    **110.3** | 150.0 |  141.1 |
| Throughput median (tok/s) |     **13.0** |   9.7 |    9.3 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.1** | 118.2 |  137.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **73.8** | 138.5 |  214.1 |
| Throughput median (tok/s) |     **13.6** |   7.2 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.3** |  99.9 |   85.9 |
| TPOT median (ms)          |     **49.8** |  61.8 |   84.7 |
| E2E median (ms)           |     **99.5** | 140.6 |  154.7 |
| Throughput median (tok/s) |     **14.2** |   9.2 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.3** | 49.9 |   58.4 |
| TPOT median (ms)          |     **26.8** | 34.5 |  105.9 |
| E2E median (ms)           |     **69.6** | 74.5 |  210.6 |
| Throughput median (tok/s) |     **18.6** | 16.3 |    6.7 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.6** |  63.1 |   56.8 |
| TPOT median (ms)          |     **18.6** |  21.4 |   31.2 |
| E2E median (ms)           |    **717.1** | 813.2 | 1106.0 |
| Throughput median (tok/s) |     **50.1** |  43.5 |   31.3 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **55.7** |  87.4 |   83.8 |
| TPOT median (ms)          |     **29.6** |  34.4 |   59.4 |
| E2E median (ms)           |    **214.0** | 263.4 |  365.3 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    98% |

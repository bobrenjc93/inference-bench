# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `f7088f965a22c688f239eae113729b0c50c22cef`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`c314af1abfddff7b6cce9af578be72c496c6a5e4` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`4ea17169b0d06efb98932b5bbd453ec44b40b6a4` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:03 PM PT, Jul 26 2026

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
| torchinferno |     355.2s (5.9m) | `ed3588b` |
| vllm         | **198.5s (3.3m)** | `c314af1` |
| sglang       |     199.2s (3.3m) | `4ea1716` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.0** |  98.7 |   79.4 |
| TPOT median (ms)          |     **53.9** |  58.5 |   69.8 |
| E2E median (ms)           |    **113.5** | 142.7 |  138.5 |
| Throughput median (tok/s) |     **12.2** |   9.6 |    9.6 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **57.4** | 103.8 |  138.4 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **81.5** | 123.0 |  212.5 |
| Throughput median (tok/s) |     **12.3** |   8.1 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.2** | 100.1 |   85.3 |
| TPOT median (ms)          |     **52.0** |  61.0 |   76.8 |
| E2E median (ms)           |    **109.5** | 139.5 |  152.9 |
| Throughput median (tok/s) |     **12.3** |  10.1 |    8.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.6** | 49.5 |   56.1 |
| TPOT median (ms)          |     **26.8** | 34.6 |  135.5 |
| E2E median (ms)           |     **66.9** | 74.6 |  212.8 |
| Throughput median (tok/s) |     **18.9** | 16.6 |    6.8 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.6** |  62.4 |   55.7 |
| TPOT median (ms)          |     **18.6** |  21.2 |   29.8 |
| E2E median (ms)           |    **714.7** | 810.4 | 1060.5 |
| Throughput median (tok/s) |     **50.5** |  43.9 |   32.7 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **57.8** |  82.9 |   83.0 |
| TPOT median (ms)          |     **30.3** |  35.1 |   62.4 |
| E2E median (ms)           |    **217.2** | 258.0 |  355.5 |
| Throughput median (tok/s) |     **21.2** |  17.7 |   12.5 |
| Correctness               |          98% |   98% |    98% |

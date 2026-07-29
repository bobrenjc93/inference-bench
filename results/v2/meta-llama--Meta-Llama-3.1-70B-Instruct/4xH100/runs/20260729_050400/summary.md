# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `18e25bfd8dd9ea1295aa9228c81a30a30d254ad6`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`7de49bab7e91a2a77e98a31fae4b1c615b34dce8` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`7c248dde7fe1f3b5100966f8143f97a9932c22a4` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 10:04 PM PT, Jul 28 2026

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
| torchinferno |     536.2s (8.9m) | `ed3588b` |
| vllm         |     217.7s (3.6m) | `7de49ba` |
| sglang       | **203.9s (3.4m)** | `7c248dd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.3** |  99.7 |   81.6 |
| TPOT median (ms)          |     **51.2** |  56.8 |   80.4 |
| E2E median (ms)           |    **109.5** | 144.7 |  142.1 |
| Throughput median (tok/s) |     **12.8** |   9.4 |    9.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.4** | 120.9 |  137.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **72.7** | 140.7 |  211.4 |
| Throughput median (tok/s) |     **13.7** |   7.1 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **66.6** | 100.2 |   86.7 |
| TPOT median (ms)          |     **50.2** |  63.0 |   89.2 |
| E2E median (ms)           |    **102.2** | 142.7 |  157.1 |
| Throughput median (tok/s) |     **13.4** |   9.5 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.9** | 49.8 |   57.4 |
| TPOT median (ms)          |     **26.8** | 34.5 |  124.4 |
| E2E median (ms)           |     **69.8** | 74.0 |  203.1 |
| Throughput median (tok/s) |     **18.9** | 16.5 |    6.8 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.0** |  62.9 |   56.8 |
| TPOT median (ms)          |     **18.4** |  21.3 |   31.6 |
| E2E median (ms)           |    **699.5** | 814.2 | 1127.9 |
| Throughput median (tok/s) |     **51.0** |  43.6 |   30.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.0** |  86.7 |   83.9 |
| TPOT median (ms)          |     **29.3** |  35.1 |   65.1 |
| E2E median (ms)           |    **210.7** | 263.3 |  368.3 |
| Throughput median (tok/s) |     **21.9** |  17.2 |   12.1 |
| Correctness               |          98% |   98% |    98% |

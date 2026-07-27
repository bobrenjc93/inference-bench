# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `82132004b7d0d277e2a64c25e71ad051097bda18`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`30fbd055379ce4c5f26fcece6cfc90c5d8596f59` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`1d350aaad3511920616a5cd16fbe413166b34a88` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:04 AM PT, Jul 27 2026

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
| torchinferno |     372.0s (6.2m) | `ed3588b` |
| vllm         | **198.9s (3.3m)** | `30fbd05` |
| sglang       |     210.8s (3.5m) | `1d350aa` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.6** | 102.2 |   83.4 |
| TPOT median (ms)          |     **51.5** |  58.6 |   82.3 |
| E2E median (ms)           |    **110.5** | 148.4 |  145.0 |
| Throughput median (tok/s) |     **12.8** |   9.5 |    9.1 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.7** | 107.0 |  134.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **74.6** | 126.5 |  211.1 |
| Throughput median (tok/s) |     **13.4** |   7.9 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **68.9** | 109.4 |   87.3 |
| TPOT median (ms)          |     **49.9** |  62.4 |   90.9 |
| E2E median (ms)           |    **105.2** | 147.8 |  156.9 |
| Throughput median (tok/s) |     **12.8** |   9.5 |    8.4 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **41.1** | 50.2 |   60.2 |
| TPOT median (ms)          |     **26.4** | 34.7 |  112.0 |
| E2E median (ms)           |     **65.6** | 75.1 |  227.4 |
| Throughput median (tok/s) |     **19.9** | 16.3 |    6.1 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **50.1** |  63.3 |   57.6 |
| TPOT median (ms)          |     **18.4** |  21.4 |   30.7 |
| E2E median (ms)           |    **710.6** | 815.4 | 1096.0 |
| Throughput median (tok/s) |     **50.9** |  43.5 |   31.8 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.5** |  86.4 |   84.6 |
| TPOT median (ms)          |     **29.2** |  35.4 |   63.2 |
| E2E median (ms)           |    **213.3** | 262.6 |  367.3 |
| Throughput median (tok/s) |     **22.0** |  17.3 |   12.0 |
| Correctness               |          98% |   98% |    99% |

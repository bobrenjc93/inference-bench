# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `f4184415c3b965e066c757397914af24c949b188`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; vllm=`25ace8fe5df07fc13f4aef5a89db391f326e60ee` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`9cffc2ba526dbc59bb2e8378ad7dcee7cd38a24e` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 2:04 AM PT, Jul 28 2026

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
| torchinferno |     447.8s (7.5m) | `ed3588b` |
| vllm         |     328.6s (5.5m) | `25ace8f` |
| sglang       | **198.0s (3.3m)** | `9cffc2b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **70.1** | 102.9 |   83.3 |
| TPOT median (ms)          |     **52.2** |  54.6 |   83.5 |
| E2E median (ms)           |    **110.3** | 148.1 |  143.3 |
| Throughput median (tok/s) |     **12.7** |   9.6 |    9.1 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **51.4** | 133.7 |  140.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **74.3** | 154.1 |  214.4 |
| Throughput median (tok/s) |     **13.5** |   6.5 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **69.6** | 103.4 |   86.8 |
| TPOT median (ms)          |     **49.6** |  60.7 |   83.3 |
| E2E median (ms)           |    **105.3** | 148.2 |  155.5 |
| Throughput median (tok/s) |     **13.0** |   9.2 |    8.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **41.8** | 49.8 |   59.2 |
| TPOT median (ms)          |     **26.6** | 34.7 |   98.3 |
| E2E median (ms)           |     **68.4** | 74.8 |  201.6 |
| Throughput median (tok/s) |     **19.3** | 16.3 |    6.7 |
| Correctness               |          97% |  97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **49.3** |  63.3 |   57.3 |
| TPOT median (ms)          |     **18.5** |  21.4 |   31.0 |
| E2E median (ms)           |    **703.8** | 815.4 | 1117.1 |
| Throughput median (tok/s) |     **50.9** |  43.5 |   31.4 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.4** |  90.6 |   85.3 |
| TPOT median (ms)          |     **29.4** |  34.3 |   59.2 |
| E2E median (ms)           |    **212.4** | 268.1 |  366.4 |
| Throughput median (tok/s) |     **21.9** |  17.0 |   12.1 |
| Correctness               |          99% |   98% |    98% |

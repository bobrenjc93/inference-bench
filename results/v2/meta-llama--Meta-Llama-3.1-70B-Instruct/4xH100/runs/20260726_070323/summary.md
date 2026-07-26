# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `612b354a1627079e3a8aeb3a083e9f61ff960afd`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`8d28b48d01b2ba56e962c7c57b894c6b4fcf8a35` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`61057bda6c4b8cda1117d74f100d0735645c0cfb` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 AM PT, Jul 26 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          2/4 |       2/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         8/20 | **10/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     440.7s (7.3m) | `b2bb774` |
| vllm         |     256.6s (4.3m) | `8d28b48` |
| sglang       | **199.5s (3.3m)** | `61057bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.2** |    100.1 |   80.6 |
| TPOT median (ms)          |         73.1 | **56.4** |   68.9 |
| E2E median (ms)           |    **122.4** |    150.9 |  139.2 |
| Throughput median (tok/s) |      **9.6** |      9.4 |    9.5 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **74.7** | 122.6 |  131.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **102.3** | 140.3 |  206.6 |
| Throughput median (tok/s) |      **9.8** |   7.1 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **78.1** |    100.3 |   84.5 |
| TPOT median (ms)          |         75.7 | **63.6** |   88.4 |
| E2E median (ms)           |    **123.3** |    142.5 |  153.0 |
| Throughput median (tok/s) |          9.4 | **10.0** |    8.7 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         58.5 | **50.1** |   58.8 |
| TPOT median (ms)          |         41.1 | **34.7** |   96.6 |
| E2E median (ms)           |         90.4 | **75.4** |  208.0 |
| Throughput median (tok/s) |         15.5 | **16.4** |    6.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         79.6 |      62.2 | **54.8** |
| TPOT median (ms)          |         26.1 |  **21.2** |     30.6 |
| E2E median (ms)           |       1063.8 | **811.0** |   1091.6 |
| Throughput median (tok/s) |         35.8 |  **43.9** |     31.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **73.4** |      87.1 |   82.1 |
| TPOT median (ms)          |         43.2 |  **35.2** |   56.9 |
| E2E median (ms)           |        300.4 | **264.0** |  359.7 |
| Throughput median (tok/s) |         16.0 |  **17.4** |   12.4 |
| Correctness               |          98% |       98% |    99% |

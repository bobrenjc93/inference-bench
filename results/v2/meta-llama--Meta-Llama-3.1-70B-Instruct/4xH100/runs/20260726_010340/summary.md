# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `c055b3791557ed3f43bbbd67509d79913c26416d`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`b2bb774413f14e277b358573fee112c9d466cb33`; vllm=`b153ae6089e9ec3272c423340d2116da97b904ce` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`2cbddb842d67b7d16f04c5a7856a0ff9bddc7767` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 PM PT, Jul 25 2026

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
| torchinferno |     501.2s (8.4m) | `b2bb774` |
| vllm         |     210.6s (3.5m) | `b153ae6` |
| sglang       | **199.8s (3.3m)** | `2cbddb8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **77.0** |    105.7 |   81.5 |
| TPOT median (ms)          |         72.5 | **53.8** |   70.8 |
| E2E median (ms)           |    **125.6** |    156.3 |  142.2 |
| Throughput median (tok/s) |      **9.6** |      9.5 |    9.4 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **63.8** | 115.9 |  133.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **90.4** | 135.2 |  211.1 |
| Throughput median (tok/s) |     **11.1** |   7.4 |    4.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **76.7** |    103.3 |   86.7 |
| TPOT median (ms)          |         74.9 | **64.3** |   86.2 |
| E2E median (ms)           |    **122.6** |    144.0 |  154.2 |
| Throughput median (tok/s) |      **9.7** |      9.5 |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.0 | **50.0** |   60.2 |
| TPOT median (ms)          |         41.7 | **34.7** |  129.8 |
| E2E median (ms)           |        100.6 | **75.3** |  206.5 |
| Throughput median (tok/s) |         12.5 | **16.3** |    6.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |         78.4 |      63.3 | **57.4** |
| TPOT median (ms)          |         26.0 |  **21.4** |     30.7 |
| E2E median (ms)           |       1043.4 | **818.7** |   1117.3 |
| Throughput median (tok/s) |         36.1 |  **43.5** |     31.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |     **72.2** |      87.6 |   83.8 |
| TPOT median (ms)          |         43.0 |  **34.9** |   63.5 |
| E2E median (ms)           |        296.5 | **265.9** |  366.3 |
| Throughput median (tok/s) |         15.8 |  **17.2** |   12.3 |
| Correctness               |          99% |       98% |    99% |

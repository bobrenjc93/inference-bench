# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `95f866f38dd2700021683746d97b8b693627aad2`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`97af8eca0494f263ac06d499989585a2b943b109`; vllm=`190be7dad2afa6684902324e0dffa2dc0229a364` + build patch `d7c94bca23b3d5712a6d17fe6928c7c2714d157567b2ac97b5cccb3dfe2c87d7`; sglang=`f5155d960286db25952217f343ee0d3c358f7f77` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 12:03 AM PT, Jul 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |      **4/4** |       0/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **12/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     510.7s (8.5m) | `97af8ec` |
| vllm         |     201.8s (3.4m) | `190be7d` |
| sglang       | **197.8s (3.3m)** | `f5155d9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        234.7 |    110.4 |  **83.4** |
| TPOT median (ms)          |        230.4 | **48.3** |      71.6 |
| E2E median (ms)           |        450.3 |    155.4 | **142.7** |
| Throughput median (tok/s) |          2.9 |  **9.8** |       9.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        369.3 | **106.7** |  136.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        464.2 | **125.8** |  209.6 |
| Throughput median (tok/s) |          2.2 |   **7.9** |    4.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **67.4** | 100.5 |   86.4 |
| TPOT median (ms)          |     **62.3** |  64.3 |   86.2 |
| E2E median (ms)           |    **124.5** | 140.7 |  154.5 |
| Throughput median (tok/s) |     **10.6** |   9.4 |    8.7 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.4 | **49.7** |   59.0 |
| TPOT median (ms)          |         40.4 | **34.3** |  106.1 |
| E2E median (ms)           |        100.0 | **74.6** |  229.6 |
| Throughput median (tok/s) |         12.5 | **16.3** |    6.3 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        254.3 |      63.2 | **57.0** |
| TPOT median (ms)          |         60.7 |  **21.4** |     30.9 |
| E2E median (ms)           |       2434.0 | **814.9** |   1114.5 |
| Throughput median (tok/s) |         14.9 |  **43.4** |     31.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        198.2 |      86.1 | **84.6** |
| TPOT median (ms)          |         78.8 |  **33.7** |     59.0 |
| E2E median (ms)           |        714.6 | **262.3** |    370.2 |
| Throughput median (tok/s) |          8.6 |  **17.4** |     12.2 |
| Correctness               |          98% |       98% |      98% |

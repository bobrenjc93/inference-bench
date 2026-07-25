# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `110fbc896692dd4969e8f22eb252b4fc7a6bbaea`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`97af8eca0494f263ac06d499989585a2b943b109`; vllm=`0ba2aa35a81dcc3246b26291368b53fa2389c7d7` + build patch `d22bf8e0c0e1802dc97fcb8743d32ecc762682c00f595f2b82434af9f0b94ca6`; sglang=`6a046fad09d4ea4b377c5d98149edd1e55d52d5d` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:35 PM PT, Jul 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          0/4 |       1/4 | **3/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |      **4/4** |       0/4 |     0/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         4/20 | **11/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     340.8s (5.7m) | `97af8ec` |
| vllm         | **195.5s (3.3m)** | `0ba2aa3` |
| sglang       |     230.5s (3.8m) | `6a046fa` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        231.9 |    102.3 |  **80.5** |
| TPOT median (ms)          |        228.6 | **56.3** |      71.2 |
| E2E median (ms)           |        446.9 |    149.7 | **140.9** |
| Throughput median (tok/s) |          2.9 |      9.3 |   **9.4** |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        361.5 | **119.5** |  133.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        455.0 | **140.9** |  207.4 |
| Throughput median (tok/s) |          2.2 |   **7.1** |    4.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **67.6** | 100.2 |   85.5 |
| TPOT median (ms)          |     **62.3** |  63.8 |   84.2 |
| E2E median (ms)           |    **124.8** | 140.7 |  155.7 |
| Throughput median (tok/s) |     **10.5** |   9.4 |    8.8 |
| Correctness               |          98% |   98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         63.9 | **49.4** |   56.1 |
| TPOT median (ms)          |         40.9 | **34.3** |  134.5 |
| E2E median (ms)           |        100.3 | **74.2** |  209.8 |
| Throughput median (tok/s) |         13.1 | **16.5** |    6.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        261.6 |      63.2 | **56.0** |
| TPOT median (ms)          |         61.0 |  **21.3** |     30.6 |
| E2E median (ms)           |       2591.0 | **815.9** |   1111.8 |
| Throughput median (tok/s) |         14.8 |  **43.5** |     31.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        197.3 |      86.9 | **82.4** |
| TPOT median (ms)          |         78.6 |  **35.2** |     64.1 |
| E2E median (ms)           |        743.6 | **264.3** |    365.1 |
| Throughput median (tok/s) |          8.7 |  **17.2** |     12.3 |
| Correctness               |          98% |       98% |      99% |

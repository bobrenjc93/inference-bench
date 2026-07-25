# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `bc2ec7444e006a919dc6a1cfd7d1bed3b540704e`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, vllm=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; vllm=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`97af8eca0494f263ac06d499989585a2b943b109`; vllm=`318b527cc2d1f672683407be05ea26a2cf1f3ea6` + build patch `d22bf8e0c0e1802dc97fcb8743d32ecc762682c00f595f2b82434af9f0b94ca6`; sglang=`95865de24f2e6a18e9df1ea0a567933c3bb57379` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:54 PM PT, Jul 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |      **3/4** |       1/4 |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **13/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     342.9s (5.7m) | `97af8ec` |
| vllm         | **201.5s (3.4m)** | `318b527` |
| sglang       |     257.3s (4.3m) | `95865de` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        231.5 |    105.3 |  **82.6** |
| TPOT median (ms)          |        227.5 | **53.0** |      74.0 |
| E2E median (ms)           |        445.2 |    150.7 | **143.1** |
| Throughput median (tok/s) |          3.0 |  **9.4** |       9.2 |
| Correctness               |          97% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        367.8 | **111.2** |  134.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        460.2 | **128.9** |  210.1 |
| Throughput median (tok/s) |          2.2 |   **7.8** |    4.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **68.0** |    108.5 |   85.3 |
| TPOT median (ms)          |         62.9 | **53.0** |   82.0 |
| E2E median (ms)           |    **125.9** |    156.2 |  153.9 |
| Throughput median (tok/s) |     **10.4** |      9.1 |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         63.1 | **49.8** |   56.6 |
| TPOT median (ms)          |         40.9 | **34.3** |  126.5 |
| E2E median (ms)           |        100.2 | **75.1** |  205.9 |
| Throughput median (tok/s) |         12.7 | **16.4** |    6.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        285.5 |      62.3 | **56.5** |
| TPOT median (ms)          |         63.8 |  **21.1** |     30.9 |
| E2E median (ms)           |       2764.0 | **808.0** |   1101.6 |
| Throughput median (tok/s) |         13.9 |  **44.1** |     31.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        203.2 |      87.4 | **83.2** |
| TPOT median (ms)          |         79.0 |  **32.3** |     62.7 |
| E2E median (ms)           |        779.1 | **263.8** |    362.9 |
| Throughput median (tok/s) |          8.4 |  **17.3** |     12.2 |
| Correctness               |          98% |       98% |      99% |

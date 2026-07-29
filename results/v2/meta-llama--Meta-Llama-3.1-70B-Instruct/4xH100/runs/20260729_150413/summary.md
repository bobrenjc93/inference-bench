# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `a9e7a7ac313cc1395e675f2673ab6706fa804c39`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`f69af7b7ad62f055867732196c13f0dd742097d2` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 8:04 AM PT, Jul 29 2026

## Integrity Warnings

- **vllm:** Provider reported benchmark or deployment errors under the result eligibility policy.
- **vllm:** Benchmark 'few_shot' has no completed result.
- **vllm:** Benchmark 'self_consistency' has no completed result.
- **vllm:** Benchmark 'multi_turn' has no completed result.
- **vllm:** Benchmark 'tree_of_thought' has no completed result.
- **vllm:** Benchmark 'long_output' has no completed result.

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **4/4** |  N/C |    0/4 |
| self_consistency |      **3/4** |  N/C |    0/4 |
| multi_turn       |      **4/4** |  N/C |    0/4 |
| tree_of_thought  |      **4/4** |  N/C |    0/4 |
| long_output      |      **4/4** |  N/C |    0/4 |
| **Total**        |    **19/20** |  N/C |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.
N/C = excluded from scoring because integrity validation did not pass.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno |   418.5s (7.0m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   245.8s (4.1m) | `f69af7b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **71.2** |    - |   88.7 |
| TPOT median (ms)          |     **52.9** |    - |   70.6 |
| E2E median (ms)           |    **114.3** |    - |  147.8 |
| Throughput median (tok/s) |     **12.4** |    - |    9.1 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-624b0642/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.9** |    - |  138.9 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **80.2** |    - |  218.3 |
| Throughput median (tok/s) |     **12.5** |    - |    4.6 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-624b0642/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **68.5** |    - |   90.0 |
| TPOT median (ms)          |     **51.7** |    - |   79.3 |
| E2E median (ms)           |    **106.0** |    - |  155.9 |
| Throughput median (tok/s) |     **13.0** |    - |    8.7 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-624b0642/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.1** |    - |   60.2 |
| TPOT median (ms)          |     **26.9** |    - |  108.6 |
| E2E median (ms)           |     **67.9** |    - |  218.2 |
| Throughput median (tok/s) |     **19.7** |    - |    6.6 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-624b0642/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **49.3** |    - |   57.9 |
| TPOT median (ms)          |     **18.7** |    - |   31.3 |
| E2E median (ms)           |    **713.1** |    - | 1109.8 |
| Throughput median (tok/s) |     **50.2** |    - |   31.2 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-624b0642/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.4** |    - |   87.2 |
| TPOT median (ms)          |     **30.0** |    - |   57.9 |
| E2E median (ms)           |    **216.3** |    - |  370.0 |
| Throughput median (tok/s) |     **21.5** |    - |   12.0 |
| Correctness               |          98% |    - |    99% |

# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `091ba22e37e08c8b0b66c3bf915d8840f8b0396b`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`db3da62333c96e48bb1cc96448b78a79bdec4d51` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 4:03 AM PT, Jul 30 2026

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
| torchinferno |   381.2s (6.4m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   202.3s (3.4m) | `db3da62` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **70.7** |    - |   82.7 |
| TPOT median (ms)          |     **53.2** |    - |   77.9 |
| E2E median (ms)           |    **112.8** |    - |  142.8 |
| Throughput median (tok/s) |     **12.5** |    - |    9.3 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-4b45a80b/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.5** |    - |  139.8 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **86.4** |    - |  212.0 |
| Throughput median (tok/s) |     **11.6** |    - |    4.7 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-4b45a80b/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **68.9** |    - |   84.9 |
| TPOT median (ms)          |     **52.4** |    - |   77.7 |
| E2E median (ms)           |    **106.4** |    - |  148.8 |
| Throughput median (tok/s) |     **12.9** |    - |    9.1 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-4b45a80b/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **43.7** |    - |   57.2 |
| TPOT median (ms)          |     **27.3** |    - |  122.5 |
| E2E median (ms)           |     **71.8** |    - |  213.6 |
| Throughput median (tok/s) |     **18.6** |    - |    6.5 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-4b45a80b/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **50.5** |    - |   56.2 |
| TPOT median (ms)          |     **18.5** |    - |   30.2 |
| E2E median (ms)           |    **717.3** |    - | 1073.2 |
| Throughput median (tok/s) |     **50.4** |    - |   32.3 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-4b45a80b/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.3** |    - |   84.2 |
| TPOT median (ms)          |     **30.3** |    - |   61.7 |
| E2E median (ms)           |    **218.9** |    - |  358.1 |
| Throughput median (tok/s) |     **21.2** |    - |   12.4 |
| Correctness               |          99% |    - |    98% |

# Benchmark Summary

- **Evaluation:** v3
- **Finalized:** true
- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **Model revision:** `1605565b47bb9346c5515c34102e054115b4f98b`
- **Harness commit:** `98676e83a23002c3aff2cffd037f9d1875ebfe51`
- **TP:** 4
- **Hardware:** 4xH100
- **Metric schema:** v2
- **Output token count:** client_tokenizer
- **Sampling top-p:** 1
- **Minimum correctness:** 95%
- **Output token tolerance:** +/-10%
- **Observed GPU coverage:** torchinferno=4/4, sglang=4/4
- **Observed GPU products:** torchinferno=NVIDIA H100 80GB HBM3; sglang=NVIDIA H100 80GB HBM3
- **Provider source:** torchinferno=`ed3588baa169bd38262adad54c898246a48a0bc2`; sglang=`c5bd3d7dce7623b8d2ffe3e662d3fd5198e6f4ba` + build patch `972c15935915b45b55a968aff63c9a737a715e7392e660b81fef2e7032ec8ac6`
- **Timestamp:** 6:03 AM PT, Jul 30 2026

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
| torchinferno |   422.3s (7.0m) | `ed3588b` |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |   194.4s (3.2m) | `c5bd3d7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **71.7** |    - |   81.7 |
| TPOT median (ms)          |     **52.8** |    - |   80.1 |
| E2E median (ms)           |    **112.3** |    - |  142.0 |
| Throughput median (tok/s) |     **12.5** |    - |    9.3 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-1c06af19/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **53.9** |    - |  134.3 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |     **76.6** |    - |  209.1 |
| Throughput median (tok/s) |     **13.0** |    - |    4.8 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-1c06af19/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **71.1** |    - |   86.1 |
| TPOT median (ms)          |     **52.3** |    - |   85.8 |
| E2E median (ms)           |    **111.0** |    - |  153.2 |
| Throughput median (tok/s) |     **12.4** |    - |    8.7 |
| Correctness               |          98% |    - |    98% |

> **vllm error:** `Command '['/workspace/submit-1c06af19/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **42.8** |    - |   55.7 |
| TPOT median (ms)          |     **26.7** |    - |  145.9 |
| E2E median (ms)           |     **69.2** |    - |  205.5 |
| Throughput median (tok/s) |     **19.0** |    - |    6.9 |
| Correctness               |          97% |    - |    97% |

> **vllm error:** `Command '['/workspace/submit-1c06af19/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **51.3** |    - |   57.3 |
| TPOT median (ms)          |     **18.7** |    - |   31.2 |
| E2E median (ms)           |    **710.5** |    - | 1113.0 |
| Throughput median (tok/s) |     **50.1** |    - |   31.3 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `Command '['/workspace/submit-1c06af19/builds/v3/vllm/venv/bin/python', '-m', 'pip', 'install', '-e', '.']' returned non-zero exit status 1.`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.2** |    - |   83.0 |
| TPOT median (ms)          |     **30.1** |    - |   68.6 |
| E2E median (ms)           |    **215.9** |    - |  364.6 |
| Throughput median (tok/s) |     **21.4** |    - |   12.2 |
| Correctness               |          98% |    - |    99% |

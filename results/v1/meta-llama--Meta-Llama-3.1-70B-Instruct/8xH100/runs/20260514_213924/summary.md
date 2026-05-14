# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:14 PM PT, May 14 2026

## Scorecard

| Benchmark | torchinferno | vllm | sglang |
| :-------- | -----------: | ---: | -----: |
| **Total** |          0/0 |  0/0 |    0/0 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **89.9s (1.5m)** | `6cf1f72` |
| vllm         |  1036.2s (17.3m) | `f887aa1` |
| sglang       |    182.4s (3.0m) | `88d3ed7` |

## Per-Benchmark Results

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |      - |
| TPOT median (ms)          |            - |    - |      - |
| E2E median (ms)           |            - |    - |      - |
| Throughput median (tok/s) |            - |    - |      - |
| Correctness               |            - |    - |      - |

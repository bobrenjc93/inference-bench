# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:10 PM PT, May 21 2026

## Scorecard

| Benchmark | torchinferno | vllm | sglang |
| :-------- | -----------: | ---: | -----: |
| **Total** |          0/0 |  0/0 |    0/0 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **87.4s (1.5m)** | `9f91b40` |
| vllm         |  1044.2s (17.4m) | `17b6982` |
| sglang       |    177.4s (3.0m) | `1a85586` |

## Per-Benchmark Results

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |      - |
| TPOT median (ms)          |            - |    - |      - |
| E2E median (ms)           |            - |    - |      - |
| Throughput median (tok/s) |            - |    - |      - |
| Correctness               |            - |    - |      - |

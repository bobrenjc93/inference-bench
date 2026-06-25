# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     441.3s (7.4m) | `c7ff2ca` |
| vllm         |     521.4s (8.7m) | `a6f41ab` |
| sglang       | **268.8s (4.5m)** | `e497668` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **139.7** |  140.2 |
| TPOT median (ms)          |            - |  **47.9** |   76.1 |
| E2E median (ms)           |            - | **181.6** |  210.3 |
| Throughput median (tok/s) |            - |   **7.7** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
P2P/IPC
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 21/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NVLS comm 0x55a70789aa60 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NVLS comm 0x55b3e5d59950 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NVLS comm 0x561f75c72380 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NVLS comm 0x563b37a0c980 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NVLS comm 0x558bf0d3d010 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NVLS comm 0x559bf5a401d0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NVLS comm 0x560dc9195c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NVLS comm 0x55f6112cf400 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:2382 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 93
gpu-dev-ee2f3198:1801:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 59
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:2384 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 109
gpu-dev-ee2f3198:1797:2385 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 23
gpu-dev-ee2f3198:1800:2386 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 136
gpu-dev-ee2f3198:1798:2387 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0     gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
         0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channe1   |             1              1              0              0              0              0              0  

ls per peer
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-ee2f3198:1802:2388 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 183
gpu-dev-ee2f3198:1803:2389 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 184
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x55a70789aa60 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x563b37a0c980 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x558bf0d3d010 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x55f6112cf400 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.35 (kernels 0.44, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
1.19, bootstrap 0.12, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.22, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.34 (kernels 0.41, alloc 1.30, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x560dc9195c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x559bf5a401d0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 971.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x561f75c72380 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x55b3e5d59950 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.34 (kernels 0.40, alloc gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.35 (kernels 0.42, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
0.77, bootstrap 0.54, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.29, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.34 (kernels 0.44, alloc gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.35 (kernels 0.41, alloc 1.27, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
1.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.53, rest 0.00)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **189.1** |  205.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **213.3** |  341.0 |
| Throughput median (tok/s) |            - |   **4.7** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
P2P/IPC
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 21/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NVLS comm 0x55a70789aa60 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NVLS comm 0x55b3e5d59950 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NVLS comm 0x561f75c72380 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NVLS comm 0x563b37a0c980 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NVLS comm 0x558bf0d3d010 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NVLS comm 0x559bf5a401d0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NVLS comm 0x560dc9195c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NVLS comm 0x55f6112cf400 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:2382 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 93
gpu-dev-ee2f3198:1801:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 59
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:2384 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 109
gpu-dev-ee2f3198:1797:2385 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 23
gpu-dev-ee2f3198:1800:2386 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 136
gpu-dev-ee2f3198:1798:2387 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0     gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
         0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channe1   |             1              1              0              0              0              0              0  

ls per peer
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-ee2f3198:1802:2388 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 183
gpu-dev-ee2f3198:1803:2389 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 184
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x55a70789aa60 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x563b37a0c980 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x558bf0d3d010 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x55f6112cf400 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.35 (kernels 0.44, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
1.19, bootstrap 0.12, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.22, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.34 (kernels 0.41, alloc 1.30, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x560dc9195c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x559bf5a401d0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 971.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x561f75c72380 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x55b3e5d59950 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.34 (kernels 0.40, alloc gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.35 (kernels 0.42, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
0.77, bootstrap 0.54, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.29, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.34 (kernels 0.44, alloc gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.35 (kernels 0.41, alloc 1.27, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
1.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.53, rest 0.00)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **158.9** |  161.2 |
| TPOT median (ms)          |            - |  **54.5** |  109.8 |
| E2E median (ms)           |            - | **205.7** |  267.9 |
| Throughput median (tok/s) |            - |   **6.6** |    5.0 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
P2P/IPC
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 21/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NVLS comm 0x55a70789aa60 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NVLS comm 0x55b3e5d59950 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NVLS comm 0x561f75c72380 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NVLS comm 0x563b37a0c980 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NVLS comm 0x558bf0d3d010 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NVLS comm 0x559bf5a401d0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NVLS comm 0x560dc9195c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NVLS comm 0x55f6112cf400 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:2382 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 93
gpu-dev-ee2f3198:1801:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 59
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:2384 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 109
gpu-dev-ee2f3198:1797:2385 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 23
gpu-dev-ee2f3198:1800:2386 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 136
gpu-dev-ee2f3198:1798:2387 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0     gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
         0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channe1   |             1              1              0              0              0              0              0  

ls per peer
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-ee2f3198:1802:2388 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 183
gpu-dev-ee2f3198:1803:2389 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 184
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x55a70789aa60 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x563b37a0c980 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x558bf0d3d010 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x55f6112cf400 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.35 (kernels 0.44, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
1.19, bootstrap 0.12, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.22, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.34 (kernels 0.41, alloc 1.30, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x560dc9195c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x559bf5a401d0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 971.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x561f75c72380 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x55b3e5d59950 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.34 (kernels 0.40, alloc gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.35 (kernels 0.42, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
0.77, bootstrap 0.54, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.29, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.34 (kernels 0.44, alloc gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.35 (kernels 0.41, alloc 1.27, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
1.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.53, rest 0.00)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.2** |   79.5 |
| TPOT median (ms)          |            - | **28.8** |   34.1 |
| E2E median (ms)           |            - | **80.1** |  120.9 |
| Throughput median (tok/s) |            - | **15.1** |   10.7 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
P2P/IPC
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 21/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NVLS comm 0x55a70789aa60 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NVLS comm 0x55b3e5d59950 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NVLS comm 0x561f75c72380 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NVLS comm 0x563b37a0c980 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NVLS comm 0x558bf0d3d010 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NVLS comm 0x559bf5a401d0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NVLS comm 0x560dc9195c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NVLS comm 0x55f6112cf400 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:2382 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 93
gpu-dev-ee2f3198:1801:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 59
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:2384 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 109
gpu-dev-ee2f3198:1797:2385 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 23
gpu-dev-ee2f3198:1800:2386 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 136
gpu-dev-ee2f3198:1798:2387 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0     gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
         0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channe1   |             1              1              0              0              0              0              0  

ls per peer
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-ee2f3198:1802:2388 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 183
gpu-dev-ee2f3198:1803:2389 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 184
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x55a70789aa60 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x563b37a0c980 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x558bf0d3d010 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x55f6112cf400 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.35 (kernels 0.44, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
1.19, bootstrap 0.12, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.22, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.34 (kernels 0.41, alloc 1.30, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x560dc9195c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x559bf5a401d0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 971.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x561f75c72380 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x55b3e5d59950 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.34 (kernels 0.40, alloc gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.35 (kernels 0.42, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
0.77, bootstrap 0.54, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.29, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.34 (kernels 0.44, alloc gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.35 (kernels 0.41, alloc 1.27, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
1.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.53, rest 0.00)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.7 | **72.3** |
| TPOT median (ms)          |            - |  **15.1** |     22.2 |
| E2E median (ms)           |            - | **635.5** |    826.5 |
| Throughput median (tok/s) |            - |  **57.4** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
P2P/IPC
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 21/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Connected all trees
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NVLS comm 0x55a70789aa60 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NVLS comm 0x55b3e5d59950 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NVLS comm 0x561f75c72380 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NVLS comm 0x563b37a0c980 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NVLS comm 0x558bf0d3d010 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NVLS comm 0x559bf5a401d0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NVLS comm 0x560dc9195c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NVLS comm 0x55f6112cf400 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-ee2f3198:1804:2382 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 93
gpu-dev-ee2f3198:1801:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 59
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:2384 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 109
gpu-dev-ee2f3198:1797:2385 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 23
gpu-dev-ee2f3198:1800:2386 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 136
gpu-dev-ee2f3198:1798:2387 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
cuMemGdrSupport 1
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0     gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
         0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channe1   |             1              1              0              0              0              0              0  

ls per peer
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-ee2f3198:1802:2388 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 183
gpu-dev-ee2f3198:1803:2389 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 184
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO ncclCommInitRankConfig comm 0x55a70789aa60 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO ncclCommInitRankConfig comm 0x563b37a0c980 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO ncclCommInitRankConfig comm 0x558bf0d3d010 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO ncclCommInitRankConfig comm 0x55f6112cf400 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-ee2f3198:1804:1804 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1800:1800 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.35 (kernels 0.44, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
1.19, bootstrap 0.12, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.22, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1802:1802 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.34 (kernels 0.41, alloc 1.30, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO ncclCommInitRankConfig comm 0x560dc9195c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-ee2f3198:1798:1798 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.34 (kernels 0.41, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO ncclCommInitRankConfig comm 0x559bf5a401d0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 971.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO ncclCommInitRankConfig comm 0x561f75c72380 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO ncclCommInitRankConfig comm 0x55b3e5d59950 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-ee2f3198:1801:1801 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.34 (kernels 0.40, alloc gpu-dev-ee2f3198:1797:1797 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.35 (kernels 0.42, alloc 000 commId 0xd4a8fe0560a5b3d6 - Init COMPLETE
0.77, bootstrap 0.54, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
1.29, bootstrap 0.01, allgathers 0.00, topo 0.08, graphs 0.01, connections 0.52, rest 0.01)
gpu-dev-ee2f3198:1799:1799 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.34 (kernels 0.44, alloc gpu-dev-ee2f3198:1803:1803 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.35 (kernels 0.41, alloc 1.27, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.52, rest 0.01)
1.25, bootstrap 0.06, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.53, rest 0.00)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.7** |  131.7 |
| TPOT median (ms)          |            - |  **29.3** |   48.4 |
| E2E median (ms)           |            - | **263.2** |  353.3 |
| Throughput median (tok/s) |            - |  **18.3** |   13.3 |
| Correctness               |            - |       98% |    99% |

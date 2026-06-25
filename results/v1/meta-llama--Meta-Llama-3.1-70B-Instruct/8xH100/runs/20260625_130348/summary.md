# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, Jun 25 2026

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
| torchinferno |     449.0s (7.5m) | `de2d6f1` |
| vllm         |    640.9s (10.7m) | `9bfd878` |
| sglang       | **261.6s (4.4m)** | `890b38c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **142.2** |  144.9 |
| TPOT median (ms)          |            - |  **50.2** |   76.6 |
| E2E median (ms)           |            - | **191.5** |  216.1 |
| Throughput median (tok/s) |            - |   **7.4** |    5.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NVLS comm 0x55c4d3fd8fd0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NVLS comm 0x5650de21b3f0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NVLS comm 0x5651eda7ebb0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NVLS comm 0x558f40a39580 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NVLS comm 0x55b58dcba440 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NVLS comm 0x55d5bc99d5f0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NVLS comm 0x556fe40be740 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NVLS comm 0x55e3b037add0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1801:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 160
gpu-dev-aa464b9b:1802:2380 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 50
gpu-dev-aa464b9b:1800:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 147
gpu-dev-aa464b9b:1799:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 163
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1796:2384 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 20
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1798:2385 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 24
gpu-dev-aa464b9b:1795:2386 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 131
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1797:2387 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 107
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d5bc99d5f0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b58dcba440 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5651eda7ebb0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55c4d3fd8fd0 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x556fe40be740 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55e3b037add0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558f40a39580 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.45, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x5650de21b3f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.39, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.38, bootstrap 0.08, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.00)
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.34, alloc 1.47, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.55, rest 0.00)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **197.6** |  214.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **219.9** |  353.5 |
| Throughput median (tok/s) |            - |   **4.5** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NVLS comm 0x55c4d3fd8fd0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NVLS comm 0x5650de21b3f0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NVLS comm 0x5651eda7ebb0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NVLS comm 0x558f40a39580 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NVLS comm 0x55b58dcba440 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NVLS comm 0x55d5bc99d5f0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NVLS comm 0x556fe40be740 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NVLS comm 0x55e3b037add0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1801:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 160
gpu-dev-aa464b9b:1802:2380 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 50
gpu-dev-aa464b9b:1800:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 147
gpu-dev-aa464b9b:1799:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 163
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1796:2384 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 20
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1798:2385 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 24
gpu-dev-aa464b9b:1795:2386 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 131
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1797:2387 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 107
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d5bc99d5f0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b58dcba440 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5651eda7ebb0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55c4d3fd8fd0 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x556fe40be740 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55e3b037add0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558f40a39580 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.45, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x5650de21b3f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.39, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.38, bootstrap 0.08, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.00)
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.34, alloc 1.47, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.55, rest 0.00)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **165.5** |  171.6 |
| TPOT median (ms)          |            - |  **55.1** |  115.7 |
| E2E median (ms)           |            - | **213.7** |  280.9 |
| Throughput median (tok/s) |            - |   **6.6** |    4.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NVLS comm 0x55c4d3fd8fd0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NVLS comm 0x5650de21b3f0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NVLS comm 0x5651eda7ebb0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NVLS comm 0x558f40a39580 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NVLS comm 0x55b58dcba440 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NVLS comm 0x55d5bc99d5f0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NVLS comm 0x556fe40be740 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NVLS comm 0x55e3b037add0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1801:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 160
gpu-dev-aa464b9b:1802:2380 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 50
gpu-dev-aa464b9b:1800:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 147
gpu-dev-aa464b9b:1799:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 163
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1796:2384 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 20
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1798:2385 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 24
gpu-dev-aa464b9b:1795:2386 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 131
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1797:2387 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 107
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d5bc99d5f0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b58dcba440 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5651eda7ebb0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55c4d3fd8fd0 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x556fe40be740 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55e3b037add0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558f40a39580 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.45, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x5650de21b3f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.39, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.38, bootstrap 0.08, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.00)
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.34, alloc 1.47, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.55, rest 0.00)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.8** |   80.5 |
| TPOT median (ms)          |            - | **31.4** |   58.4 |
| E2E median (ms)           |            - | **84.6** |  150.0 |
| Throughput median (tok/s) |            - | **14.8** |    9.3 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NVLS comm 0x55c4d3fd8fd0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NVLS comm 0x5650de21b3f0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NVLS comm 0x5651eda7ebb0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NVLS comm 0x558f40a39580 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NVLS comm 0x55b58dcba440 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NVLS comm 0x55d5bc99d5f0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NVLS comm 0x556fe40be740 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NVLS comm 0x55e3b037add0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1801:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 160
gpu-dev-aa464b9b:1802:2380 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 50
gpu-dev-aa464b9b:1800:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 147
gpu-dev-aa464b9b:1799:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 163
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1796:2384 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 20
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1798:2385 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 24
gpu-dev-aa464b9b:1795:2386 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 131
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1797:2387 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 107
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d5bc99d5f0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b58dcba440 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5651eda7ebb0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55c4d3fd8fd0 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x556fe40be740 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55e3b037add0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558f40a39580 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.45, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x5650de21b3f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.39, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.38, bootstrap 0.08, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.00)
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.34, alloc 1.47, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.55, rest 0.00)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      73.9 | **70.5** |
| TPOT median (ms)          |            - |  **14.8** |     22.5 |
| E2E median (ms)           |            - | **608.3** |    838.6 |
| Throughput median (tok/s) |            - |  **59.5** |     41.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Connected all trees
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NVLS comm 0x55c4d3fd8fd0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NVLS comm 0x5650de21b3f0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NVLS comm 0x5651eda7ebb0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NVLS comm 0x558f40a39580 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NVLS comm 0x55b58dcba440 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NVLS comm 0x55d5bc99d5f0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NVLS comm 0x556fe40be740 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NVLS comm 0x55e3b037add0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-aa464b9b:1801:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 160
gpu-dev-aa464b9b:1802:2380 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 50
gpu-dev-aa464b9b:1800:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 147
gpu-dev-aa464b9b:1799:2383 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 163
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1796:2384 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 20
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1798:2385 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 24
gpu-dev-aa464b9b:1795:2386 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 131
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1797:2387 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 107
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x55d5bc99d5f0 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b58dcba440 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x5651eda7ebb0 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x55c4d3fd8fd0 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-aa464b9b:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x556fe40be740 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x55e3b037add0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-aa464b9b:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558f40a39580 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.45, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
gpu-dev-aa464b9b:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.36, alloc gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x5650de21b3f0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-aa464b9b:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.34, alloc gpu-dev-aa464b9b:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.39, bootstrap 0.09, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
1.38, bootstrap 0.08, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
000 commId 0x4dd4bb71647e17d6 - Init COMPLETE
1.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.00)
gpu-dev-aa464b9b:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.34, alloc 1.47, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.55, rest 0.00)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.0** |  136.3 |
| TPOT median (ms)          |            - |  **30.3** |   54.6 |
| E2E median (ms)           |            - | **263.6** |  367.8 |
| Throughput median (tok/s) |            - |  **18.6** |   12.8 |
| Correctness               |            - |       98% |    99% |

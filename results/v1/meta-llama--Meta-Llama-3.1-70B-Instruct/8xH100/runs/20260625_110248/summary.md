# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 25 2026

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
| torchinferno |     439.4s (7.3m) | `c7ff2ca` |
| vllm         |     554.4s (9.2m) | `9222148` |
| sglang       | **263.1s (4.4m)** | `bc15017` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **141.2** |  151.1 |
| TPOT median (ms)          |            - |  **47.4** |   83.1 |
| E2E median (ms)           |            - | **185.6** |  228.6 |
| Throughput median (tok/s) |            - |   **7.6** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 19/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Connected all trees
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Connected all trees
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Connected all trees
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Connected all trees
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Connected all trees
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Connected all trees
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NVLS comm 0x55cdbfbb89a0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NVLS comm 0x56496eab3c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NVLS comm 0x560a66b72870 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NVLS comm 0x55a439e5a710 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NVLS comm 0x558a1e2acd10 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NVLS comm 0x5586728a4850 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NVLS comm 0x55b75dbe2c30 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NVLS comm 0x55e9eb0be730 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 183
gpu-dev-b5985af4:1801:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 57
gpu-dev-b5985af4:1798:2383 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 22
gpu-dev-b5985af4:1796:2384 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
gpu-dev-b5985af4:1803:2385 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 183
gpu-dev-b5985af4:1800:2386 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 57
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-b5985af4:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
ls per peer
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-b5985af4:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-b5985af4:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-b5985af4:1799:2387 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 31
gpu-dev-b5985af4:1797:2388 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 42
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x5586728a4850 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-b5985af4:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x558a1e2acd10 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x55a439e5a710 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560a66b72870 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-b5985af4:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x55e9eb0be730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-b5985af4:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x55b75dbe2c30 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.48 (kernels 0.34, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55cdbfbb89a0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x56496eab3c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.47 (kernels 0.39, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.30, bootstrap 0.19, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.47 (kernels 0.38, alloc gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.48 (kernels 0.33, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.43, bootstrap 0.00, allgathers 0.02, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.48 (kernels 0.33, alloc gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.47 (kernels 0.33, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.47 (kernels 0.36, alloc 1.42, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.25, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.47 (kernels 0.36, alloc 1.26, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.26, bootstrap 0.23, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
1.46, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **195.9** |  234.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **214.3** |  400.7 |
| Throughput median (tok/s) |            - |   **4.7** |    2.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 19/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Connected all trees
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Connected all trees
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Connected all trees
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Connected all trees
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Connected all trees
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Connected all trees
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NVLS comm 0x55cdbfbb89a0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NVLS comm 0x56496eab3c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NVLS comm 0x560a66b72870 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NVLS comm 0x55a439e5a710 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NVLS comm 0x558a1e2acd10 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NVLS comm 0x5586728a4850 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NVLS comm 0x55b75dbe2c30 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NVLS comm 0x55e9eb0be730 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 183
gpu-dev-b5985af4:1801:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 57
gpu-dev-b5985af4:1798:2383 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 22
gpu-dev-b5985af4:1796:2384 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
gpu-dev-b5985af4:1803:2385 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 183
gpu-dev-b5985af4:1800:2386 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 57
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-b5985af4:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
ls per peer
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-b5985af4:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-b5985af4:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-b5985af4:1799:2387 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 31
gpu-dev-b5985af4:1797:2388 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 42
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x5586728a4850 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-b5985af4:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x558a1e2acd10 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x55a439e5a710 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560a66b72870 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-b5985af4:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x55e9eb0be730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-b5985af4:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x55b75dbe2c30 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.48 (kernels 0.34, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55cdbfbb89a0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x56496eab3c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.47 (kernels 0.39, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.30, bootstrap 0.19, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.47 (kernels 0.38, alloc gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.48 (kernels 0.33, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.43, bootstrap 0.00, allgathers 0.02, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.48 (kernels 0.33, alloc gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.47 (kernels 0.33, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.47 (kernels 0.36, alloc 1.42, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.25, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.47 (kernels 0.36, alloc 1.26, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.26, bootstrap 0.23, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
1.46, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **154.3** |  166.3 |
| TPOT median (ms)          |            - |  **44.4** |  106.5 |
| E2E median (ms)           |            - | **197.1** |  264.0 |
| Throughput median (tok/s) |            - |   **6.9** |    5.2 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 19/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Connected all trees
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Connected all trees
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Connected all trees
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Connected all trees
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Connected all trees
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Connected all trees
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NVLS comm 0x55cdbfbb89a0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NVLS comm 0x56496eab3c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NVLS comm 0x560a66b72870 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NVLS comm 0x55a439e5a710 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NVLS comm 0x558a1e2acd10 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NVLS comm 0x5586728a4850 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NVLS comm 0x55b75dbe2c30 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NVLS comm 0x55e9eb0be730 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 183
gpu-dev-b5985af4:1801:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 57
gpu-dev-b5985af4:1798:2383 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 22
gpu-dev-b5985af4:1796:2384 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
gpu-dev-b5985af4:1803:2385 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 183
gpu-dev-b5985af4:1800:2386 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 57
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-b5985af4:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
ls per peer
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-b5985af4:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-b5985af4:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-b5985af4:1799:2387 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 31
gpu-dev-b5985af4:1797:2388 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 42
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x5586728a4850 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-b5985af4:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x558a1e2acd10 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x55a439e5a710 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560a66b72870 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-b5985af4:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x55e9eb0be730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-b5985af4:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x55b75dbe2c30 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.48 (kernels 0.34, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55cdbfbb89a0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x56496eab3c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.47 (kernels 0.39, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.30, bootstrap 0.19, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.47 (kernels 0.38, alloc gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.48 (kernels 0.33, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.43, bootstrap 0.00, allgathers 0.02, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.48 (kernels 0.33, alloc gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.47 (kernels 0.33, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.47 (kernels 0.36, alloc 1.42, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.25, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.47 (kernels 0.36, alloc 1.26, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.26, bootstrap 0.23, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
1.46, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.1** |   80.3 |
| TPOT median (ms)          |            - | **28.7** |   62.6 |
| E2E median (ms)           |            - | **81.1** |  149.7 |
| Throughput median (tok/s) |            - | **14.7** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 19/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Connected all trees
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Connected all trees
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Connected all trees
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Connected all trees
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Connected all trees
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Connected all trees
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NVLS comm 0x55cdbfbb89a0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NVLS comm 0x56496eab3c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NVLS comm 0x560a66b72870 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NVLS comm 0x55a439e5a710 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NVLS comm 0x558a1e2acd10 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NVLS comm 0x5586728a4850 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NVLS comm 0x55b75dbe2c30 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NVLS comm 0x55e9eb0be730 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 183
gpu-dev-b5985af4:1801:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 57
gpu-dev-b5985af4:1798:2383 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 22
gpu-dev-b5985af4:1796:2384 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
gpu-dev-b5985af4:1803:2385 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 183
gpu-dev-b5985af4:1800:2386 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 57
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-b5985af4:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
ls per peer
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-b5985af4:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-b5985af4:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-b5985af4:1799:2387 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 31
gpu-dev-b5985af4:1797:2388 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 42
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x5586728a4850 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-b5985af4:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x558a1e2acd10 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x55a439e5a710 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560a66b72870 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-b5985af4:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x55e9eb0be730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-b5985af4:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x55b75dbe2c30 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.48 (kernels 0.34, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55cdbfbb89a0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x56496eab3c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.47 (kernels 0.39, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.30, bootstrap 0.19, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.47 (kernels 0.38, alloc gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.48 (kernels 0.33, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.43, bootstrap 0.00, allgathers 0.02, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.48 (kernels 0.33, alloc gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.47 (kernels 0.33, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.47 (kernels 0.36, alloc 1.42, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.25, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.47 (kernels 0.36, alloc 1.26, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.26, bootstrap 0.23, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
1.46, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      79.6 | **74.1** |
| TPOT median (ms)          |            - |  **14.8** |     21.7 |
| E2E median (ms)           |            - | **628.9** |    830.5 |
| Throughput median (tok/s) |            - |  **58.7** |     42.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 19/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 18/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 20/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 19/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 21/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 22/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 20/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Channel 23/0 : 1[1] -> 0[0] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 21/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 22/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Channel 23/0 : 2[2] -> 1[1] via P2P/IPC
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Connected all trees
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Connected all trees
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Connected all trees
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Connected all trees
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Connected all trees
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Connected all trees
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Connected all trees
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NVLS comm 0x55cdbfbb89a0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NVLS comm 0x56496eab3c90 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NVLS comm 0x560a66b72870 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NVLS comm 0x55a439e5a710 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NVLS comm 0x558a1e2acd10 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NVLS comm 0x5586728a4850 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NVLS comm 0x55b75dbe2c30 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NVLS comm 0x55e9eb0be730 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-b5985af4:1802:2381 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 183
gpu-dev-b5985af4:1801:2382 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 57
gpu-dev-b5985af4:1798:2383 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 22
gpu-dev-b5985af4:1796:2384 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
gpu-dev-b5985af4:1803:2385 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 183
gpu-dev-b5985af4:1800:2386 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 57
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-b5985af4:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
ls per peer
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-b5985af4:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-b5985af4:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-b5985af4:1799:2387 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 31
gpu-dev-b5985af4:1797:2388 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 42
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x5586728a4850 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-b5985af4:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x558a1e2acd10 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x55a439e5a710 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560a66b72870 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-b5985af4:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x55e9eb0be730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-b5985af4:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x55b75dbe2c30 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.48 (kernels 0.34, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55cdbfbb89a0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x56496eab3c90 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-b5985af4:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.47 (kernels 0.39, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.30, bootstrap 0.19, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.54, rest 0.01)
000 commId 0x5ce9425bd0a52729 - Init COMPLETE
gpu-dev-b5985af4:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.47 (kernels 0.38, alloc gpu-dev-b5985af4:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.48 (kernels 0.33, alloc 000 commId 0x5ce9425bd0a52729 - Init COMPLETE
1.43, bootstrap 0.00, allgathers 0.02, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
gpu-dev-b5985af4:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.48 (kernels 0.33, alloc gpu-dev-b5985af4:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.47 (kernels 0.33, alloc gpu-dev-b5985af4:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.47 (kernels 0.36, alloc 1.42, bootstrap 0.02, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.25, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
gpu-dev-b5985af4:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.47 (kernels 0.36, alloc 1.26, bootstrap 0.24, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.26, bootstrap 0.23, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
1.45, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.55, rest 0.00)
1.46, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.54, rest 0.01)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **126.0** |  141.3 |
| TPOT median (ms)          |            - |  **27.0** |   54.8 |
| E2E median (ms)           |            - | **261.4** |  374.7 |
| Throughput median (tok/s) |            - |  **18.5** |   13.1 |
| Correctness               |            - |       99% |    99% |

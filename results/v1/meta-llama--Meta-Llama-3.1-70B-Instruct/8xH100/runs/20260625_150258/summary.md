# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jun 25 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     411.4s (6.9m) | `754cc36` |
| vllm         |     560.0s (9.3m) | `d490b98` |
| sglang       | **276.5s (4.6m)** | `4d06d4c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **136.3** |  149.0 |
| TPOT median (ms)          |            - |  **46.7** |   81.3 |
| E2E median (ms)           |            - | **181.2** |  226.3 |
| Throughput median (tok/s) |            - |   **7.6** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 18/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 19/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 20/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 21/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Connected all trees
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Connected all trees
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Connected all trees
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Connected all trees
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Connected all trees
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Connected all trees
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NVLS comm 0x55b0e50b0050 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NVLS comm 0x56346dcce900 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NVLS comm 0x560919a30bf0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NVLS comm 0x55b2dbc76da0 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NVLS comm 0x561cdce64170 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NVLS comm 0x55ebd6d6b020 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSigpu-dev-0342cf21:1136:1136 [4] NCCL INFO NVLS comm 0x5564355a2910 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
ze 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NVLS comm 0x55e049498d70 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1717 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 17
gpu-dev-0342cf21:1132:1718 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 35
gpu-dev-0342cf21:1133:1719 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 45
gpu-dev-0342cf21:1135:1720 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 17
gpu-dev-0342cf21:1136:1721 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 185
gpu-dev-0342cf21:1138:1723 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 70
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1722 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 185
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1724 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 65
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-0342cf21:1132:1132 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO ncclCommInitRankConfig comm 0x56346dcce900 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-0342cf21:1136:1136 [4] NCCL INFO ncclCommInitRankConfig comm 0x5564355a2910 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-0342cf21:1132:1132 [0] NCCL INFO ncclCommInitRankConfig comm 0x55b0e50b0050 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-0342cf21:1134:1134 [2] NCCL INFO ncclCommInitRankConfig comm 0x561cdce64170 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.32, alloc gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.33, alloc 1.43, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO ncclCommInitRankConfig comm 0x55e049498d70 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a81.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.43, bootstrap 0.04, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b2dbc76da0 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-0342cf21:1139:1139 [7] NCCL INFO ncclCommInitRankConfig comm 0x55ebd6d6b020 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO ncclCommInitRankConfig comm 0x560919a30bf0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.33, alloc 000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
1.42, bootstrap 0.06, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.33, alloc 1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.56, rest 0.00)
1.47, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.55, rest 0.01)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **175.6** |  211.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **199.3** |  344.8 |
| Throughput median (tok/s) |            - |   **5.0** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 18/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 19/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 20/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 21/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Connected all trees
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Connected all trees
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Connected all trees
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Connected all trees
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Connected all trees
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Connected all trees
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NVLS comm 0x55b0e50b0050 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NVLS comm 0x56346dcce900 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NVLS comm 0x560919a30bf0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NVLS comm 0x55b2dbc76da0 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NVLS comm 0x561cdce64170 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NVLS comm 0x55ebd6d6b020 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSigpu-dev-0342cf21:1136:1136 [4] NCCL INFO NVLS comm 0x5564355a2910 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
ze 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NVLS comm 0x55e049498d70 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1717 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 17
gpu-dev-0342cf21:1132:1718 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 35
gpu-dev-0342cf21:1133:1719 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 45
gpu-dev-0342cf21:1135:1720 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 17
gpu-dev-0342cf21:1136:1721 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 185
gpu-dev-0342cf21:1138:1723 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 70
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1722 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 185
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1724 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 65
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-0342cf21:1132:1132 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO ncclCommInitRankConfig comm 0x56346dcce900 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-0342cf21:1136:1136 [4] NCCL INFO ncclCommInitRankConfig comm 0x5564355a2910 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-0342cf21:1132:1132 [0] NCCL INFO ncclCommInitRankConfig comm 0x55b0e50b0050 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-0342cf21:1134:1134 [2] NCCL INFO ncclCommInitRankConfig comm 0x561cdce64170 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.32, alloc gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.33, alloc 1.43, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO ncclCommInitRankConfig comm 0x55e049498d70 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a81.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.43, bootstrap 0.04, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b2dbc76da0 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-0342cf21:1139:1139 [7] NCCL INFO ncclCommInitRankConfig comm 0x55ebd6d6b020 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO ncclCommInitRankConfig comm 0x560919a30bf0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.33, alloc 000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
1.42, bootstrap 0.06, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.33, alloc 1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.56, rest 0.00)
1.47, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.55, rest 0.01)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **165.1** |  171.4 |
| TPOT median (ms)          |            - |  **59.6** |  100.4 |
| E2E median (ms)           |            - | **214.0** |  268.2 |
| Throughput median (tok/s) |            - |   **6.3** |    4.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 18/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 19/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 20/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 21/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Connected all trees
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Connected all trees
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Connected all trees
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Connected all trees
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Connected all trees
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Connected all trees
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NVLS comm 0x55b0e50b0050 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NVLS comm 0x56346dcce900 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NVLS comm 0x560919a30bf0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NVLS comm 0x55b2dbc76da0 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NVLS comm 0x561cdce64170 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NVLS comm 0x55ebd6d6b020 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSigpu-dev-0342cf21:1136:1136 [4] NCCL INFO NVLS comm 0x5564355a2910 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
ze 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NVLS comm 0x55e049498d70 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1717 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 17
gpu-dev-0342cf21:1132:1718 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 35
gpu-dev-0342cf21:1133:1719 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 45
gpu-dev-0342cf21:1135:1720 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 17
gpu-dev-0342cf21:1136:1721 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 185
gpu-dev-0342cf21:1138:1723 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 70
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1722 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 185
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1724 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 65
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-0342cf21:1132:1132 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO ncclCommInitRankConfig comm 0x56346dcce900 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-0342cf21:1136:1136 [4] NCCL INFO ncclCommInitRankConfig comm 0x5564355a2910 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-0342cf21:1132:1132 [0] NCCL INFO ncclCommInitRankConfig comm 0x55b0e50b0050 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-0342cf21:1134:1134 [2] NCCL INFO ncclCommInitRankConfig comm 0x561cdce64170 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.32, alloc gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.33, alloc 1.43, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO ncclCommInitRankConfig comm 0x55e049498d70 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a81.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.43, bootstrap 0.04, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b2dbc76da0 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-0342cf21:1139:1139 [7] NCCL INFO ncclCommInitRankConfig comm 0x55ebd6d6b020 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO ncclCommInitRankConfig comm 0x560919a30bf0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.33, alloc 000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
1.42, bootstrap 0.06, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.33, alloc 1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.56, rest 0.00)
1.47, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.55, rest 0.01)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.9** |   85.3 |
| TPOT median (ms)          |            - | **30.2** |   37.3 |
| E2E median (ms)           |            - | **83.0** |  137.4 |
| Throughput median (tok/s) |            - | **14.7** |   10.0 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 18/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 19/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 20/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 21/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Connected all trees
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Connected all trees
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Connected all trees
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Connected all trees
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Connected all trees
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Connected all trees
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NVLS comm 0x55b0e50b0050 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NVLS comm 0x56346dcce900 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NVLS comm 0x560919a30bf0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NVLS comm 0x55b2dbc76da0 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NVLS comm 0x561cdce64170 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NVLS comm 0x55ebd6d6b020 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSigpu-dev-0342cf21:1136:1136 [4] NCCL INFO NVLS comm 0x5564355a2910 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
ze 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NVLS comm 0x55e049498d70 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1717 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 17
gpu-dev-0342cf21:1132:1718 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 35
gpu-dev-0342cf21:1133:1719 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 45
gpu-dev-0342cf21:1135:1720 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 17
gpu-dev-0342cf21:1136:1721 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 185
gpu-dev-0342cf21:1138:1723 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 70
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1722 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 185
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1724 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 65
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-0342cf21:1132:1132 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO ncclCommInitRankConfig comm 0x56346dcce900 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-0342cf21:1136:1136 [4] NCCL INFO ncclCommInitRankConfig comm 0x5564355a2910 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-0342cf21:1132:1132 [0] NCCL INFO ncclCommInitRankConfig comm 0x55b0e50b0050 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-0342cf21:1134:1134 [2] NCCL INFO ncclCommInitRankConfig comm 0x561cdce64170 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.32, alloc gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.33, alloc 1.43, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO ncclCommInitRankConfig comm 0x55e049498d70 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a81.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.43, bootstrap 0.04, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b2dbc76da0 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-0342cf21:1139:1139 [7] NCCL INFO ncclCommInitRankConfig comm 0x55ebd6d6b020 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO ncclCommInitRankConfig comm 0x560919a30bf0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.33, alloc 000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
1.42, bootstrap 0.06, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.33, alloc 1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.56, rest 0.00)
1.47, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.55, rest 0.01)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **69.3** |   69.8 |
| TPOT median (ms)          |            - |  **14.8** |   22.0 |
| E2E median (ms)           |            - | **612.3** |  816.5 |
| Throughput median (tok/s) |            - |  **59.8** |   42.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
a P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 22/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 20/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Channel 23/0 : 5[5] -> 4[4] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 18/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 21/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 19/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 22/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Channel 23/0 : 4[4] -> 3[3] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 20/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 21/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 22/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Channel 23/0 : 3[3] -> 2[2] via P2P/IPC
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Connected all trees
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Connected all trees
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Connected all trees
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Connected all trees
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Connected all trees
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Connected all trees
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Connected all trees
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NVLS comm 0x55b0e50b0050 headRank 0 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NVLS comm 0x56346dcce900 headRank 6 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NVLS comm 0x560919a30bf0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NVLS comm 0x55b2dbc76da0 headRank 3 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NVLS comm 0x561cdce64170 headRank 2 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NVLS comm 0x55ebd6d6b020 headRank 7 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSigpu-dev-0342cf21:1136:1136 [4] NCCL INFO NVLS comm 0x5564355a2910 headRank 4 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
ze 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NVLS comm 0x55e049498d70 headRank 5 nHeads 8 nvlsRanks 8 buffSize 1048576 nvlsPerRankSize 33554432 nvlsTotalSize 268435456
gpu-dev-0342cf21:1134:1717 [0] NCCL INFO [Proxy Progress] Device 2 CPU core 17
gpu-dev-0342cf21:1132:1718 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 35
gpu-dev-0342cf21:1133:1719 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 45
gpu-dev-0342cf21:1135:1720 [0] NCCL INFO [Proxy Progress] Device 3 CPU core 17
gpu-dev-0342cf21:1136:1721 [0] NCCL INFO [Proxy Progress] Device 4 CPU core 185
gpu-dev-0342cf21:1138:1723 [0] NCCL INFO [Proxy Progress] Device 6 CPU core 70
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1722 [0] NCCL INFO [Proxy Progress] Device 7 CPU core 185
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1724 [0] NCCL INFO [Proxy Progress] Device 5 CPU core 65
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-0342cf21:1132:1132 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1132:1132 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO ncclCommInitRankConfig comm 0x56346dcce900 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9gpu-dev-0342cf21:1136:1136 [4] NCCL INFO ncclCommInitRankConfig comm 0x5564355a2910 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-0342cf21:1132:1132 [0] NCCL INFO ncclCommInitRankConfig comm 0x55b0e50b0050 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-0342cf21:1134:1134 [2] NCCL INFO ncclCommInitRankConfig comm 0x561cdce64170 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1138:1138 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 2.46 (kernels 0.32, alloc gpu-dev-0342cf21:1132:1132 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1136:1136 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 2.46 (kernels 0.33, alloc 1.43, bootstrap 0.05, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO ncclCommInitRankConfig comm 0x55e049498d70 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a81.47, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1134:1134 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 2.46 (kernels 0.34, alloc 1.43, bootstrap 0.04, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO ncclCommInitRankConfig comm 0x55b2dbc76da0 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-0342cf21:1139:1139 [7] NCCL INFO ncclCommInitRankConfig comm 0x55ebd6d6b020 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
gpu-dev-0342cf21:1133:1133 [1] NCCL INFO ncclCommInitRankConfig comm 0x560919a30bf0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0xd348dd38f6a77098 - Init COMPLETE
gpu-dev-0342cf21:1137:1137 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 2.46 (kernels 0.33, alloc 000 commId 0xd348dd38f6a77098 - Init COMPLETE
000 commId 0xd348dd38f6a77098 - Init COMPLETE
1.42, bootstrap 0.06, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.56, rest 0.00)
gpu-dev-0342cf21:1135:1135 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1139:1139 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 2.46 (kernels 0.33, alloc gpu-dev-0342cf21:1133:1133 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 2.46 (kernels 0.33, alloc 1.46, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.56, rest 0.01)
1.42, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.02, connections 0.56, rest 0.00)
1.47, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.01, connections 0.55, rest 0.01)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **121.2** |  137.3 |
| TPOT median (ms)          |            - |  **30.3** |   48.2 |
| E2E median (ms)           |            - | **258.0** |  358.6 |
| Throughput median (tok/s) |            - |  **18.7** |   13.1 |
| Correctness               |            - |       98% |    98% |

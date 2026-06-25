# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     386.4s (6.4m) | `c59b09e` |
| vllm         |     565.9s (9.4m) | `9e88e96` |
| sglang       | **267.2s (4.5m)** | `8314247` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **132.6** |  140.8 |
| TPOT median (ms)          |            - |  **48.0** |   74.2 |
| E2E median (ms)           |            - | **171.7** |  210.5 |
| Throughput median (tok/s) |            - |   **8.0** |    5.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-597b33eb:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
ls per peer
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-597b33eb:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558cfd9a5110 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x561780ff3ca0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5630150bbb70 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-597b33eb:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x555e2520c870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b92.20, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55e7096961d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-597b33eb:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x557c7b4cc730 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c413878df0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 641.44, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.02)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x560e57de0270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x8bdef7956b63ef29 - Init COMPLETE
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.70 (kernels 0.33, alloc 2.14, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.36, alloc 2.22, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.25, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
1.76, bootstrap 0.49, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
1.83, bootstrap 0.39, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.37, alloc 2.09, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **185.2** |  206.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **207.8** |  338.1 |
| Throughput median (tok/s) |            - |   **4.8** |    3.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-597b33eb:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
ls per peer
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-597b33eb:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558cfd9a5110 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x561780ff3ca0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5630150bbb70 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-597b33eb:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x555e2520c870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b92.20, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55e7096961d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-597b33eb:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x557c7b4cc730 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c413878df0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 641.44, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.02)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x560e57de0270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x8bdef7956b63ef29 - Init COMPLETE
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.70 (kernels 0.33, alloc 2.14, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.36, alloc 2.22, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.25, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
1.76, bootstrap 0.49, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
1.83, bootstrap 0.39, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.37, alloc 2.09, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     166.2 | **164.1** |
| TPOT median (ms)          |            - |  **51.8** |      96.1 |
| E2E median (ms)           |            - | **207.5** |     265.2 |
| Throughput median (tok/s) |            - |   **6.4** |       5.0 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-597b33eb:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
ls per peer
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-597b33eb:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558cfd9a5110 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x561780ff3ca0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5630150bbb70 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-597b33eb:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x555e2520c870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b92.20, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55e7096961d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-597b33eb:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x557c7b4cc730 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c413878df0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 641.44, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.02)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x560e57de0270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x8bdef7956b63ef29 - Init COMPLETE
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.70 (kernels 0.33, alloc 2.14, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.36, alloc 2.22, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.25, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
1.76, bootstrap 0.49, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
1.83, bootstrap 0.39, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.37, alloc 2.09, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.8** |   80.1 |
| TPOT median (ms)          |            - | **29.8** |   45.4 |
| E2E median (ms)           |            - | **84.1** |  136.9 |
| Throughput median (tok/s) |            - | **14.3** |   10.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-597b33eb:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
ls per peer
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-597b33eb:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558cfd9a5110 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x561780ff3ca0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5630150bbb70 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-597b33eb:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x555e2520c870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b92.20, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55e7096961d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-597b33eb:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x557c7b4cc730 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c413878df0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 641.44, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.02)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x560e57de0270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x8bdef7956b63ef29 - Init COMPLETE
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.70 (kernels 0.33, alloc 2.14, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.36, alloc 2.22, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.25, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
1.76, bootstrap 0.49, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
1.83, bootstrap 0.39, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.37, alloc 2.09, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      78.1 | **65.5** |
| TPOT median (ms)          |            - |  **14.8** |     22.1 |
| E2E median (ms)           |            - | **620.4** |    819.8 |
| Throughput median (tok/s) |            - |  **58.4** |     42.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channegpu-dev-597b33eb:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
ls per peer
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-597b33eb:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-597b33eb:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x558cfd9a5110 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x561780ff3ca0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-597b33eb:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5630150bbb70 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-597b33eb:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x555e2520c870 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b92.20, bootstrap 0.05, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-597b33eb:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.69 (kernels 0.32, alloc 000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55e7096961d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53gpu-dev-597b33eb:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x557c7b4cc730 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x55c413878df0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 641.44, bootstrap 0.82, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.02)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x560e57de0270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x8bdef7956b63ef29 - Init COMPLETE
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.69 (kernels 0.35, alloc gpu-dev-597b33eb:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.70 (kernels 0.33, alloc 2.14, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
000 commId 0x8bdef7956b63ef29 - Init COMPLETE
gpu-dev-597b33eb:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.69 (kernels 0.32, alloc gpu-dev-597b33eb:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.69 (kernels 0.36, alloc 2.22, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.25, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
1.76, bootstrap 0.49, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
1.83, bootstrap 0.39, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-597b33eb:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.69 (kernels 0.37, alloc 2.09, bootstrap 0.11, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.6** |  131.5 |
| TPOT median (ms)          |            - |  **28.9** |   47.6 |
| E2E median (ms)           |            - | **258.3** |  354.1 |
| Throughput median (tok/s) |            - |  **18.4** |   13.4 |
| Correctness               |            - |       98% |    99% |

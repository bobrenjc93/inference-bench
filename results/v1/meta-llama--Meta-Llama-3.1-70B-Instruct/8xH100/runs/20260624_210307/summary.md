# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jun 24 2026

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
| torchinferno |     396.2s (6.6m) | `2af6f8f` |
| vllm         |     546.9s (9.1m) | `d7ab9be` |
| sglang       | **275.0s (4.6m)** | `5f30fa2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **136.4** |  136.6 |
| TPOT median (ms)          |            - |  **44.9** |   77.2 |
| E2E median (ms)           |            - | **179.5** |  208.3 |
| Throughput median (tok/s) |            - |   **8.1** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55f00f254460 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x559ebf2a2360 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ded0329be0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xcf4b99820c598946 - Init COMPLETE
2.21, bootstrap 0.15, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x5651f5c48520 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5617446a8f10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x56338c86c270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x5603f0c55630 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x560e0c4586f0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.82 (kernels 0.35, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
2.02, bootstrap 0.33, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.05)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
1.84, bootstrap 0.51, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.82 (kernels 0.37, alloc 2.34, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.82 (kernels 0.36, alloc gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.82 (kernels 0.34, alloc 2.35, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
2.32, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.33, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
2.29, bootstrap 0.06, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.01)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **192.2** |  209.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **216.0** |  353.6 |
| Throughput median (tok/s) |            - |   **4.6** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55f00f254460 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x559ebf2a2360 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ded0329be0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xcf4b99820c598946 - Init COMPLETE
2.21, bootstrap 0.15, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x5651f5c48520 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5617446a8f10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x56338c86c270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x5603f0c55630 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x560e0c4586f0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.82 (kernels 0.35, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
2.02, bootstrap 0.33, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.05)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
1.84, bootstrap 0.51, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.82 (kernels 0.37, alloc 2.34, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.82 (kernels 0.36, alloc gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.82 (kernels 0.34, alloc 2.35, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
2.32, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.33, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
2.29, bootstrap 0.06, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.01)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     162.0 | **159.1** |
| TPOT median (ms)          |            - |  **50.3** |     101.6 |
| E2E median (ms)           |            - | **204.2** |     258.3 |
| Throughput median (tok/s) |            - |   **6.6** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55f00f254460 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x559ebf2a2360 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ded0329be0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xcf4b99820c598946 - Init COMPLETE
2.21, bootstrap 0.15, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x5651f5c48520 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5617446a8f10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x56338c86c270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x5603f0c55630 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x560e0c4586f0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.82 (kernels 0.35, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
2.02, bootstrap 0.33, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.05)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
1.84, bootstrap 0.51, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.82 (kernels 0.37, alloc 2.34, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.82 (kernels 0.36, alloc gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.82 (kernels 0.34, alloc 2.35, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
2.32, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.33, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
2.29, bootstrap 0.06, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.01)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.1** |   81.3 |
| TPOT median (ms)          |            - | **29.3** |   42.1 |
| E2E median (ms)           |            - | **82.4** |  134.3 |
| Throughput median (tok/s) |            - | **14.6** |   10.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55f00f254460 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x559ebf2a2360 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ded0329be0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xcf4b99820c598946 - Init COMPLETE
2.21, bootstrap 0.15, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x5651f5c48520 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5617446a8f10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x56338c86c270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x5603f0c55630 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x560e0c4586f0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.82 (kernels 0.35, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
2.02, bootstrap 0.33, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.05)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
1.84, bootstrap 0.51, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.82 (kernels 0.37, alloc 2.34, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.82 (kernels 0.36, alloc gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.82 (kernels 0.34, alloc 2.35, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
2.32, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.33, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
2.29, bootstrap 0.06, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.01)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      71.8 | **65.2** |
| TPOT median (ms)          |            - |  **14.9** |     22.7 |
| E2E median (ms)           |            - | **599.4** |    836.1 |
| Throughput median (tok/s) |            - |  **59.4** |     41.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO ncclCommInitRankConfig comm 0x55f00f254460 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1799:1799 [4] NCCL INFO ncclCommInitRankConfig comm 0x559ebf2a2360 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97gpu-dev-c1702a0a:1797:1797 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ded0329be0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0xcf4b99820c598946 - Init COMPLETE
2.21, bootstrap 0.15, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO ncclCommInitRankConfig comm 0x5651f5c48520 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO ncclCommInitRankConfig comm 0x5617446a8f10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO ncclCommInitRankConfig comm 0x56338c86c270 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO ncclCommInitRankConfig comm 0x5603f0c55630 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-c1702a0a:1799:1799 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO ncclCommInitRankConfig comm 0x560e0c4586f0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64gpu-dev-c1702a0a:1795:1795 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.82 (kernels 0.35, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
000 commId 0xcf4b99820c598946 - Init COMPLETE
2.02, bootstrap 0.33, allgathers 0.01, topo 0.08, graphs 0.01, connections 0.98, rest 0.05)
gpu-dev-c1702a0a:1801:1801 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.82 (kernels 0.34, alloc 000 commId 0xcf4b99820c598946 - Init COMPLETE
1.84, bootstrap 0.51, allgathers 0.00, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
gpu-dev-c1702a0a:1798:1798 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.82 (kernels 0.34, alloc gpu-dev-c1702a0a:1800:1800 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.82 (kernels 0.37, alloc 2.34, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-c1702a0a:1802:1802 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.82 (kernels 0.36, alloc gpu-dev-c1702a0a:1796:1796 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.82 (kernels 0.34, alloc 2.35, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.00, rest 0.03)
2.32, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.03, rest 0.00)
2.33, bootstrap 0.00, allgathers 0.01, topo 0.08, graphs 0.01, connections 1.02, rest 0.01)
2.29, bootstrap 0.06, allgathers 0.00, topo 0.08, graphs 0.02, connections 1.02, rest 0.01)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **124.5** |  130.4 |
| TPOT median (ms)          |            - |  **27.9** |   48.7 |
| E2E median (ms)           |            - | **256.3** |  358.1 |
| Throughput median (tok/s) |            - |  **18.7** |   13.1 |
| Correctness               |            - |       98% |    98% |

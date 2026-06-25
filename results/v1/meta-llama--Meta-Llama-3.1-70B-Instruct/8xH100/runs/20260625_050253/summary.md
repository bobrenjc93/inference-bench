# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 24 2026

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
| torchinferno |     423.7s (7.1m) | `3805373` |
| vllm         |     541.2s (9.0m) | `3f5a1e1` |
| sglang       | **280.5s (4.7m)** | `72cac88` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **128.3** |  158.2 |
| TPOT median (ms)          |            - |  **45.5** |   76.9 |
| E2E median (ms)           |            - | **165.8** |  233.1 |
| Throughput median (tok/s) |            - |   **8.0** |    5.3 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-dc07a789:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x56392874fd00 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-dc07a789:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x5581ef7ab850 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-dc07a789:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55a859ccef00 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x563532b41e20 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x564972783820 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.68 (kernels 0.34, alloc gpu-dev-dc07a789:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x55eb52863420 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-dc07a789:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560d4ec46d10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ddfaf0b010 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 532.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.68 (kernels 0.33, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.68 (kernels 0.34, alloc 1.97, bootstrap 0.28, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.68 (kernels 0.34, alloc 1.21, bootstrap 1.04, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.02)
2.19, bootstrap 0.05, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.68 (kernels 0.34, alloc 2.12, bootstrap 0.12, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.68 (kernels 0.34, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
2.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.96, rest 0.06)
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **205.8** |  219.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **226.3** |  384.9 |
| Throughput median (tok/s) |            - |   **4.4** |    2.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-dc07a789:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x56392874fd00 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-dc07a789:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x5581ef7ab850 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-dc07a789:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55a859ccef00 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x563532b41e20 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x564972783820 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.68 (kernels 0.34, alloc gpu-dev-dc07a789:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x55eb52863420 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-dc07a789:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560d4ec46d10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ddfaf0b010 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 532.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.68 (kernels 0.33, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.68 (kernels 0.34, alloc 1.97, bootstrap 0.28, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.68 (kernels 0.34, alloc 1.21, bootstrap 1.04, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.02)
2.19, bootstrap 0.05, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.68 (kernels 0.34, alloc 2.12, bootstrap 0.12, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.68 (kernels 0.34, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
2.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.96, rest 0.06)
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **161.8** |  165.0 |
| TPOT median (ms)          |            - |  **46.1** |  104.5 |
| E2E median (ms)           |            - | **204.3** |  262.3 |
| Throughput median (tok/s) |            - |   **6.6** |    5.1 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-dc07a789:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x56392874fd00 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-dc07a789:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x5581ef7ab850 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-dc07a789:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55a859ccef00 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x563532b41e20 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x564972783820 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.68 (kernels 0.34, alloc gpu-dev-dc07a789:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x55eb52863420 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-dc07a789:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560d4ec46d10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ddfaf0b010 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 532.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.68 (kernels 0.33, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.68 (kernels 0.34, alloc 1.97, bootstrap 0.28, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.68 (kernels 0.34, alloc 1.21, bootstrap 1.04, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.02)
2.19, bootstrap 0.05, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.68 (kernels 0.34, alloc 2.12, bootstrap 0.12, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.68 (kernels 0.34, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
2.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.96, rest 0.06)
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.7** |   86.2 |
| TPOT median (ms)          |            - | **28.6** |   33.2 |
| E2E median (ms)           |            - | **81.5** |  133.9 |
| Throughput median (tok/s) |            - | **14.9** |    9.8 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-dc07a789:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x56392874fd00 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-dc07a789:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x5581ef7ab850 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-dc07a789:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55a859ccef00 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x563532b41e20 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x564972783820 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.68 (kernels 0.34, alloc gpu-dev-dc07a789:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x55eb52863420 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-dc07a789:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560d4ec46d10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ddfaf0b010 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 532.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.68 (kernels 0.33, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.68 (kernels 0.34, alloc 1.97, bootstrap 0.28, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.68 (kernels 0.34, alloc 1.21, bootstrap 1.04, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.02)
2.19, bootstrap 0.05, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.68 (kernels 0.34, alloc 2.12, bootstrap 0.12, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.68 (kernels 0.34, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
2.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.96, rest 0.06)
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      81.2 | **74.5** |
| TPOT median (ms)          |            - |  **14.9** |     22.2 |
| E2E median (ms)           |            - | **605.4** |    828.6 |
| Throughput median (tok/s) |            - |  **58.0** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s.
Last health check: ConnectError: [Errno 111] Connection refused
Log tail:
Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO TUNER/Plugin: Using nccl_ofi_tuner (v3)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner selected platform: AWS
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5.48xlarge
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO NCCL_ALGO set by environment to ring,tree
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT  
    Broadcast |        1         2         1   |             1              1              0              0              0              0              0  
       Reduce |        1         2         1   |             1              1              0              0              0              0              0  
    AllGather |        1         2         1   |             1              1              0              0              0              0              0  
ReduceScatter |        1         2         1   |             1              1              0              0              0              0              0  
    AllReduce |        1         2         1   |             1              1              0              0              0              0              0  

gpu-dev-dc07a789:1796:1796 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 0, globalGinSupport 0, globalNicFused 0 cuMemGdrSupport 1
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO CC Off, workFifoBytes 1048576
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO ncclCommInitRankConfig comm 0x56392874fd00 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8gpu-dev-dc07a789:1803:1803 [7] NCCL INFO ncclCommInitRankConfig comm 0x5581ef7ab850 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId cagpu-dev-dc07a789:1797:1797 [1] NCCL INFO ncclCommInitRankConfig comm 0x55a859ccef00 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO ncclCommInitRankConfig comm 0x563532b41e20 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO ncclCommInitRankConfig comm 0x564972783820 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1803:1803 [7] NCCL INFO Init timings - ncclCommInitRankConfig: rank 7 nranks 8 total 3.68 (kernels 0.34, alloc gpu-dev-dc07a789:1798:1798 [2] NCCL INFO ncclCommInitRankConfig comm 0x55eb52863420 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75gpu-dev-dc07a789:1799:1799 [3] NCCL INFO ncclCommInitRankConfig comm 0x560d4ec46d10 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1801:1801 [5] NCCL INFO Init timings - ncclCommInitRankConfig: rank 5 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO ncclCommInitRankConfig comm 0x55ddfaf0b010 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 532.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.97, rest 0.05)
000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1797:1797 [1] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 8 total 3.68 (kernels 0.33, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1798:1798 [2] NCCL INFO Init timings - ncclCommInitRankConfig: rank 2 nranks 8 total 3.68 (kernels 0.34, alloc 1.97, bootstrap 0.28, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.03)
gpu-dev-dc07a789:1802:1802 [6] NCCL INFO Init timings - ncclCommInitRankConfig: rank 6 nranks 8 total 3.68 (kernels 0.34, alloc 000 commId 0x7b6dcb8062e2781c - Init COMPLETE
gpu-dev-dc07a789:1800:1800 [4] NCCL INFO Init timings - ncclCommInitRankConfig: rank 4 nranks 8 total 3.68 (kernels 0.34, alloc 1.21, bootstrap 1.04, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.00, rest 0.02)
2.19, bootstrap 0.05, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
2.24, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.01, rest 0.01)
gpu-dev-dc07a789:1796:1796 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 8 total 3.68 (kernels 0.34, alloc 2.12, bootstrap 0.12, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
gpu-dev-dc07a789:1799:1799 [3] NCCL INFO Init timings - ncclCommInitRankConfig: rank 3 nranks 8 total 3.68 (kernels 0.34, alloc 2.23, bootstrap 0.00, allgathers 0.00, topo 0.07, graphs 0.01, connections 1.02, rest 0.00)
2.22, bootstrap 0.02, allgathers 0.00, topo 0.07, graphs 0.01, connections 0.96, rest 0.06)
`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **127.3** |  140.6 |
| TPOT median (ms)          |            - |  **27.0** |   47.4 |
| E2E median (ms)           |            - | **256.6** |  368.6 |
| Throughput median (tok/s) |            - |  **18.4** |   13.0 |
| Correctness               |            - |       98% |    99% |

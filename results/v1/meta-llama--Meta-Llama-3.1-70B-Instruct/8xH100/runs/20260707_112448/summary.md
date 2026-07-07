# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:24 AM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno | vllm |  sglang |
| :--------------- | -----------: | ---: | ------: |
| few_shot         |      **3/4** |  0/4 |     1/4 |
| self_consistency |      **3/4** |  0/4 |     0/4 |
| multi_turn       |          1/4 |  0/4 | **3/4** |
| tree_of_thought  |      **3/4** |  0/4 |     1/4 |
| long_output      |          1/4 |  0/4 | **3/4** |
| **Total**        |    **11/20** | 0/20 |    8/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **31.2s (0.5m)** | `b488218` |
| vllm         |    204.4s (3.4m) | `ed051fa` |
| sglang       |    221.5s (3.7m) | `cfd3fdc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        155.9 |    - | **140.1** |
| TPOT median (ms)          |     **44.2** |    - |      74.4 |
| E2E median (ms)           |    **199.0** |    - |     215.0 |
| Throughput median (tok/s) |      **5.9** |    - |       5.6 |
| Correctness               |          98% |    - |       98% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-6448682b/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-6448682b/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-6448682b/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/video.py", line 35, in <module>
    from torchcodec.decoders import VideoDecoder
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/_metadata.py", line 15, in <module>
    from torchcodec._core.ops import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/ops.py", line 38, in <module>
    load_torchcodec_shared_libraries()
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 111, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.56: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |    **172.8** |    - |  210.1 |
| TPOT median (ms)          |          0.0 |    - |    0.0 |
| E2E median (ms)           |    **182.3** |    - |  346.7 |
| Throughput median (tok/s) |      **5.5** |    - |    2.9 |
| Correctness               |         100% |    - |   100% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-6448682b/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-6448682b/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-6448682b/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/video.py", line 35, in <module>
    from torchcodec.decoders import VideoDecoder
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/_metadata.py", line 15, in <module>
    from torchcodec._core.ops import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/ops.py", line 38, in <module>
    load_torchcodec_shared_libraries()
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 111, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.56: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        248.3 |    - | **170.3** |
| TPOT median (ms)          |     **59.9** |    - |     108.2 |
| E2E median (ms)           |        313.3 |    - | **280.5** |
| Throughput median (tok/s) |          4.5 |    - |   **4.6** |
| Correctness               |          98% |    - |       98% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-6448682b/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-6448682b/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-6448682b/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/video.py", line 35, in <module>
    from torchcodec.decoders import VideoDecoder
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/_metadata.py", line 15, in <module>
    from torchcodec._core.ops import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/ops.py", line 38, in <module>
    load_torchcodec_shared_libraries()
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 111, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.56: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm |   sglang |
| :------------------------ | -----------: | ---: | -------: |
| TTFT median (ms)          |         80.4 |    - | **45.5** |
| TPOT median (ms)          |     **64.4** |    - |    251.4 |
| E2E median (ms)           |    **114.8** |    - |    265.5 |
| Throughput median (tok/s) |     **12.2** |    - |      5.5 |
| Correctness               |          96% |    - |      97% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-6448682b/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-6448682b/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-6448682b/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/video.py", line 35, in <module>
    from torchcodec.decoders import VideoDecoder
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/_metadata.py", line 15, in <module>
    from torchcodec._core.ops import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/ops.py", line 38, in <module>
    load_torchcodec_shared_libraries()
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 111, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.56: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        253.6 |    - |  **64.9** |
| TPOT median (ms)          |     **19.8** |    - |      22.6 |
| E2E median (ms)           |        995.7 |    - | **881.3** |
| Throughput median (tok/s) |         37.2 |    - |  **41.5** |
| Correctness               |         100% |    - |      100% |

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-6448682b/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-6448682b/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-6448682b/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-6448682b/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-6448682b/builds/vllm/vllm/multimodal/video.py", line 35, in <module>
    from torchcodec.decoders import VideoDecoder
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/_metadata.py", line 15, in <module>
    from torchcodec._core.ops import (
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_core/ops.py", line 38, in <module>
    load_torchcodec_shared_libraries()
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 111, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.56: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /workspace/submit-6448682b/builds/vllm/venv/lib/python3.12/site-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm |    sglang |
| :------------------------ | -----------: | ---: | --------: |
| TTFT median (ms)          |        182.2 |    - | **126.2** |
| TPOT median (ms)          |     **37.7** |    - |      91.3 |
| E2E median (ms)           |    **361.0** |    - |     397.8 |
| Throughput median (tok/s) |     **13.1** |    - |      12.0 |
| Correctness               |          98% |    - |       98% |

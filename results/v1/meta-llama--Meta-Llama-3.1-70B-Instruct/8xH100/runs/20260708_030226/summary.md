# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |          0/4 |  0/4 |    0/4 |
| self_consistency |          0/4 |  0/4 |    0/4 |
| multi_turn       |          0/4 |  0/4 |    0/4 |
| tree_of_thought  |          0/4 |  0/4 |    0/4 |
| long_output      |          0/4 |  0/4 |    0/4 |
| **Total**        |         0/20 | 0/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.0s (0.7m)** | `4892cad` |
| vllm         |    202.3s (3.4m) | `2afa3f7` |
| sglang       |    201.5s (3.4m) | `d4963f5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  138.9 |
| TPOT median (ms)          |            - |    - |   74.8 |
| E2E median (ms)           |            - |    - |  217.7 |
| Throughput median (tok/s) |            - |    - |    5.5 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `timed out`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-8059878a/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-8059878a/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-8059878a/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  212.2 |
| TPOT median (ms)          |            - |    - |    0.0 |
| E2E median (ms)           |            - |    - |  366.1 |
| Throughput median (tok/s) |            - |    - |    2.7 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-8059878a/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-8059878a/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-8059878a/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  164.0 |
| TPOT median (ms)          |            - |    - |  105.7 |
| E2E median (ms)           |            - |    - |  274.8 |
| Throughput median (tok/s) |            - |    - |    4.7 |
| Correctness               |            - |    - |    98% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-8059878a/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-8059878a/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-8059878a/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   45.2 |
| TPOT median (ms)          |            - |    - |  292.0 |
| E2E median (ms)           |            - |    - |  301.6 |
| Throughput median (tok/s) |            - |    - |    5.0 |
| Correctness               |            - |    - |    97% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-8059878a/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-8059878a/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-8059878a/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |   63.5 |
| TPOT median (ms)          |            - |    - |   22.7 |
| E2E median (ms)           |            - |    - |  908.7 |
| Throughput median (tok/s) |            - |    - |   40.9 |
| Correctness               |            - |    - |   100% |

> **torchinferno error:** `Connection error.`

> **vllm error:** `[vllm] Server process exited with code 1.
Log tail:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspace/submit-8059878a/builds/vllm/vllm/entrypoints/openai/api_server.py", line 26, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs
  File "/workspace/submit-8059878a/builds/vllm/vllm/engine/arg_utils.py", line 119, in <module>
    from vllm.v1.sample.logits_processor import LogitsProcessor
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/sample/logits_processor/__init__.py", line 15, in <module>
    from vllm.sampling_params import SamplingParams
  File "/workspace/submit-8059878a/builds/vllm/vllm/sampling_params.py", line 23, in <module>
    from vllm.v1.serial_utils import PydanticMsgspecMixin
  File "/workspace/submit-8059878a/builds/vllm/vllm/v1/serial_utils.py", line 25, in <module>
    from vllm.multimodal.inputs import (
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/__init__.py", line 3, in <module>
    from .hasher import MultiModalHasher
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/hasher.py", line 17, in <module>
    from .media import MediaWithBytes
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/__init__.py", line 5, in <module>
    from .connector import MEDIA_CONNECTOR_REGISTRY, MediaConnector
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/media/connector.py", line 28, in <module>
    from vllm.multimodal.video import get_video_loader_backend_for_processor
  File "/workspace/submit-8059878a/builds/vllm/vllm/multimodal/video.py", line 36
    from torchcodec.decoders import VideoDecoder
    ^
IndentationError: expected an indented block after 'try' statement on line 35
`

## Cross-Benchmark Averages

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |            - |    - |  124.7 |
| TPOT median (ms)          |            - |    - |   99.0 |
| E2E median (ms)           |            - |    - |  413.8 |
| Throughput median (tok/s) |            - |    - |   11.8 |
| Correctness               |            - |    - |    99% |

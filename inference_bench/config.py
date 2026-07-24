from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .deployment import (
    DISAGGREGATED_PREFILL_DECODE,
    deployment_mode_for_evaluation,
    resolve_role_tensor_parallel_sizes,
    results_dir_for_evaluation,
    tensor_parallel_size_for_evaluation,
)


SCORED_PROVIDERS = ("torchinferno", "vllm", "sglang")
SCORED_BENCHMARKS = (
    "few_shot",
    "self_consistency",
    "multi_turn",
    "tree_of_thought",
    "long_output",
)
_SAFE_RESULT_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
_SCORED_MINIMUM_CORRECTNESS_RATE = 0.95
_SCORED_OUTPUT_TOKEN_RATIO_TOLERANCE = 0.10


@dataclass
class Config:
    evaluation_version: int = 2
    model: str = "meta-llama/Meta-Llama-3.1-70B-Instruct"
    model_revision: str | None = None
    tensor_parallel_size: int | None = None
    deployment_mode: str = field(init=False)
    prefill_tensor_parallel_size: int | None = field(init=False, default=None)
    decode_tensor_parallel_size: int | None = field(init=False, default=None)
    providers: list[str] = field(default_factory=lambda: ["vllm", "sglang"])
    benchmarks: list[str] = field(
        default_factory=lambda: [
            "few_shot",
            "self_consistency",
            "multi_turn",
            "tree_of_thought",
        ]
    )
    hardware: str = ""
    build_dir: str = "./builds"
    results_dir: str | None = None
    server_port: int = 8000
    server_startup_timeout: int = 600
    minimum_correctness_rate: float | None = None
    require_request_count_parity: bool = False
    output_token_ratio_tolerance: float | None = None
    retain_response_text: bool = False
    authoritative_output_token_count: bool = False

    def __post_init__(self) -> None:
        self.deployment_mode = deployment_mode_for_evaluation(
            self.evaluation_version
        )
        expected_tp = tensor_parallel_size_for_evaluation(self.evaluation_version)
        if self.tensor_parallel_size is None:
            self.tensor_parallel_size = expected_tp
        if self.evaluation_version == 4:
            self.prefill_tensor_parallel_size = expected_tp
            self.decode_tensor_parallel_size = expected_tp
        if self.evaluation_version >= 3:
            self.minimum_correctness_rate = _SCORED_MINIMUM_CORRECTNESS_RATE
            self.require_request_count_parity = True
            self.output_token_ratio_tolerance = (
                _SCORED_OUTPUT_TOKEN_RATIO_TOLERANCE
            )
            self.retain_response_text = True
            self.authoritative_output_token_count = True
        if self.results_dir is None:
            self.results_dir = results_dir_for_evaluation(self.evaluation_version)
        self.validate()

    @property
    def role_tensor_parallel_sizes(self) -> tuple[int | None, int | None]:
        return resolve_role_tensor_parallel_sizes(
            deployment_mode=self.deployment_mode,
            tensor_parallel_size=self.tensor_parallel_size,
            prefill_tensor_parallel_size=self.prefill_tensor_parallel_size,
            decode_tensor_parallel_size=self.decode_tensor_parallel_size,
        )

    @property
    def gpu_count(self) -> int:
        prefill_tp, decode_tp = self.role_tensor_parallel_sizes
        if self.deployment_mode == DISAGGREGATED_PREFILL_DECODE:
            assert prefill_tp is not None and decode_tp is not None
            return prefill_tp + decode_tp
        return int(self.tensor_parallel_size)

    @property
    def resolved_results_dir(self) -> str:
        if self.evaluation_version >= 3:
            root = Path(__file__).resolve().parents[1]
            return str(root / results_dir_for_evaluation(self.evaluation_version))
        return str(self.results_dir)

    def validate(self) -> Config:
        self.deployment_mode = deployment_mode_for_evaluation(
            self.evaluation_version
        )
        expected_tp = tensor_parallel_size_for_evaluation(self.evaluation_version)
        if self.tensor_parallel_size is None:
            self.tensor_parallel_size = expected_tp
        if self.evaluation_version >= 3 and self.tensor_parallel_size != expected_tp:
            raise ValueError(
                f"evaluation v{self.evaluation_version} requires tensor parallel "
                f"size {expected_tp}"
            )
        expected_prefill_tp = expected_tp if self.evaluation_version == 4 else None
        expected_decode_tp = expected_tp if self.evaluation_version == 4 else None
        if (
            self.prefill_tensor_parallel_size != expected_prefill_tp
            or self.decode_tensor_parallel_size != expected_decode_tp
        ):
            raise ValueError(
                f"evaluation v{self.evaluation_version} has an implicit fixed topology"
            )
        expected_results_dir = results_dir_for_evaluation(self.evaluation_version)
        if self.results_dir is None:
            self.results_dir = expected_results_dir
        if self.evaluation_version >= 3 and Path(self.results_dir) != Path(
            expected_results_dir
        ):
            raise ValueError(
                f"evaluation v{self.evaluation_version} results must be written to "
                f"{expected_results_dir}"
            )
        self.role_tensor_parallel_sizes
        if self.evaluation_version >= 3:
            if not isinstance(self.model_revision, str) or not re.fullmatch(
                r"[0-9a-fA-F]{40}", self.model_revision
            ):
                raise ValueError(
                    f"evaluation v{self.evaluation_version} requires a pinned "
                    "40-character model_revision"
                )
            model_parts = str(self.model).split("/")
            if not model_parts or any(
                part in {"", ".", ".."}
                or "--" in part
                or not _SAFE_RESULT_COMPONENT.fullmatch(part)
                for part in model_parts
            ):
                raise ValueError("Scored model identifier is not path-safe")
            if (
                self.hardware in {"", ".", ".."}
                or not _SAFE_RESULT_COMPONENT.fullmatch(str(self.hardware))
            ):
                raise ValueError("Scored hardware label is not path-safe")
            if tuple(self.providers) != SCORED_PROVIDERS:
                raise ValueError(
                    f"evaluation v{self.evaluation_version} requires providers "
                    + ", ".join(SCORED_PROVIDERS)
                )
            if tuple(self.benchmarks) != SCORED_BENCHMARKS:
                raise ValueError(
                    f"evaluation v{self.evaluation_version} requires the complete "
                    "canonical benchmark suite"
                )
            scored_policy = (
                self.minimum_correctness_rate,
                self.require_request_count_parity,
                self.output_token_ratio_tolerance,
                self.retain_response_text,
                self.authoritative_output_token_count,
            )
            if scored_policy != (
                _SCORED_MINIMUM_CORRECTNESS_RATE,
                True,
                _SCORED_OUTPUT_TOKEN_RATIO_TOLERANCE,
                True,
                True,
            ):
                raise ValueError(
                    f"evaluation v{self.evaluation_version} requires its canonical "
                    "correctness and evidence policy"
                )
            http_overrides = sorted(
                name
                for name in (
                    "INFERENCE_BENCH_HTTP_MAX_CONNECTIONS",
                    "INFERENCE_BENCH_HTTP_MAX_KEEPALIVE_CONNECTIONS",
                )
                if name in os.environ
            )
            if http_overrides:
                raise ValueError(
                    "Scored evaluation HTTP concurrency overrides are prohibited: "
                    + ", ".join(http_overrides)
                )
        if int(self.server_port) < 1 or int(self.server_port) > 65535:
            raise ValueError("server_port must be between 1 and 65535")
        if int(self.server_startup_timeout) < 1:
            raise ValueError("server_startup_timeout must be at least 1 second")
        for name in ("minimum_correctness_rate", "output_token_ratio_tolerance"):
            value = getattr(self, name)
            if value is not None and not 0.0 <= float(value) <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        return self

    @classmethod
    def load(cls, path: str | Path | None = None) -> Config:
        explicit_path = path is not None
        if path is None:
            path = Path(__file__).parent.parent / "config.yaml"
        path = Path(path)
        if path.exists():
            with open(path) as f:
                data = yaml.safe_load(f) or {}
            init_fields = {
                name
                for name, definition in cls.__dataclass_fields__.items()
                if definition.init
            }
            unknown = sorted(set(data) - init_fields)
            if unknown:
                raise ValueError(
                    "Unsupported config field(s): " + ", ".join(unknown)
                )
            loaded_version = data.get("evaluation_version", 2)
            deployment_mode_for_evaluation(loaded_version)
            if loaded_version >= 3:
                implicit_fields = sorted(
                    {
                        "authoritative_output_token_count",
                        "minimum_correctness_rate",
                        "output_token_ratio_tolerance",
                        "require_request_count_parity",
                        "results_dir",
                        "retain_response_text",
                        "tensor_parallel_size",
                    }.intersection(data)
                )
                if implicit_fields:
                    raise ValueError(
                        "Scored evaluation fields are version-derived and must not "
                        "be configured: " + ", ".join(implicit_fields)
                    )
            return cls(**data)
        if explicit_path:
            raise FileNotFoundError(f"Configuration file does not exist: {path}")
        return cls()

    def apply_overrides(
        self,
        *,
        model: str | None = None,
        model_revision: str | None = None,
        providers: list[str] | None = None,
        benchmarks: list[str] | None = None,
        tp: int | None = None,
        hardware: str | None = None,
        build_dir: str | None = None,
        results_dir: str | None = None,
        port: int | None = None,
        server_startup_timeout: int | None = None,
    ) -> Config:
        if model is not None:
            self.model = model
        if model_revision is not None:
            self.model_revision = model_revision
        if providers is not None:
            self.providers = providers
        if benchmarks is not None:
            self.benchmarks = benchmarks
        if tp is not None:
            if self.evaluation_version >= 3:
                raise ValueError(
                    f"evaluation v{self.evaluation_version} topology is implicit and "
                    "cannot be overridden"
                )
            self.tensor_parallel_size = tp
        if hardware is not None:
            self.hardware = hardware
        if build_dir is not None:
            self.build_dir = build_dir
        if results_dir is not None:
            self.results_dir = results_dir
        if port is not None:
            self.server_port = port
        if server_startup_timeout is not None:
            self.server_startup_timeout = server_startup_timeout
        return self.validate()

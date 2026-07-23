from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .deployment import (
    DISAGGREGATED_PREFILL_DECODE,
    STANDARD_DEPLOYMENT,
    normalize_deployment_mode,
    resolve_role_tensor_parallel_sizes,
)


@dataclass
class Config:
    model: str = "meta-llama/Meta-Llama-3.1-70B-Instruct"
    model_revision: str | None = None
    tensor_parallel_size: int = 8
    deployment_mode: str = STANDARD_DEPLOYMENT
    prefill_tensor_parallel_size: int | None = None
    decode_tensor_parallel_size: int | None = None
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
    results_dir: str = "./results/v1"
    server_port: int = 8000
    server_startup_timeout: int = 600
    minimum_correctness_rate: float | None = None
    require_request_count_parity: bool = False
    output_token_ratio_tolerance: float | None = None
    retain_response_text: bool = False
    authoritative_output_token_count: bool = False

    def __post_init__(self) -> None:
        self.deployment_mode = normalize_deployment_mode(self.deployment_mode)
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

    def validate(self) -> Config:
        self.deployment_mode = normalize_deployment_mode(self.deployment_mode)
        self.role_tensor_parallel_sizes
        if self.deployment_mode == DISAGGREGATED_PREFILL_DECODE:
            if not isinstance(self.model_revision, str) or not re.fullmatch(
                r"[0-9a-fA-F]{40}", self.model_revision
            ):
                raise ValueError(
                    "disaggregated_prefill_decode requires a pinned 40-character "
                    "model_revision"
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
        if path is None:
            path = Path(__file__).parent.parent / "config.yaml"
        path = Path(path)
        if path.exists():
            with open(path) as f:
                data = yaml.safe_load(f) or {}
            return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
        return cls()

    def apply_overrides(
        self,
        *,
        model: str | None = None,
        model_revision: str | None = None,
        providers: list[str] | None = None,
        benchmarks: list[str] | None = None,
        tp: int | None = None,
        deployment_mode: str | None = None,
        prefill_tp: int | None = None,
        decode_tp: int | None = None,
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
            self.tensor_parallel_size = tp
        if deployment_mode is not None:
            self.deployment_mode = deployment_mode
        if prefill_tp is not None:
            self.prefill_tensor_parallel_size = prefill_tp
        if decode_tp is not None:
            self.decode_tensor_parallel_size = decode_tp
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

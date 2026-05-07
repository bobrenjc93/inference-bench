from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Config:
    model: str = "meta-llama/Meta-Llama-3.1-70B-Instruct"
    tensor_parallel_size: int = 8
    providers: list[str] = field(default_factory=lambda: ["vllm", "sglang"])
    benchmarks: list[str] = field(
        default_factory=lambda: [
            "few_shot",
            "self_consistency",
            "multi_turn",
            "tree_of_thought",
        ]
    )
    build_dir: str = "./builds"
    results_dir: str = "./results"
    server_port: int = 8000
    server_startup_timeout: int = 600

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
        providers: list[str] | None = None,
        benchmarks: list[str] | None = None,
        tp: int | None = None,
        build_dir: str | None = None,
        results_dir: str | None = None,
        port: int | None = None,
    ) -> Config:
        if model is not None:
            self.model = model
        if providers is not None:
            self.providers = providers
        if benchmarks is not None:
            self.benchmarks = benchmarks
        if tp is not None:
            self.tensor_parallel_size = tp
        if build_dir is not None:
            self.build_dir = build_dir
        if results_dir is not None:
            self.results_dir = results_dir
        if port is not None:
            self.server_port = port
        return self

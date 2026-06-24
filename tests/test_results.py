from __future__ import annotations

import json

from inference_bench.results import ProviderResults, RunResults


def test_save_copies_provider_logs(tmp_path) -> None:
    source_log = tmp_path / "torchinferno_server.log"
    source_log.write_text("server tail\n")
    results = RunResults(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        tensor_parallel_size=8,
        hardware="8xH100",
    )
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        commit_hash="abc123",
        server_log_path=str(source_log),
    )

    results_path = results.save(tmp_path / "results")

    data = json.loads(results_path.read_text())
    provider = data["providers"]["torchinferno"]
    assert provider["server_log"] == "provider_logs/torchinferno.log"
    copied_log = results_path.parent / provider["server_log"]
    assert copied_log.read_text() == "server tail\n"

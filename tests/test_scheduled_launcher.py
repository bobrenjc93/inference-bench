from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_scheduled_launcher_targets_results_v2_on_four_h100s() -> None:
    launcher = (ROOT / "run_benchmark.sh").read_text()

    assert "--gpus 4" in launcher
    assert "--gpus 8" not in launcher
    assert "-- bash _remote_benchmark.sh config_v3.yaml" in launcher
    assert (
        "results/v2/meta-llama--Meta-Llama-3.1-70B-Instruct/4xH100"
        in launcher
    )


def test_remote_launcher_rejects_wrong_results_v2_gpu_count() -> None:
    launcher = (ROOT / "_remote_benchmark.sh").read_text()

    assert 'CONFIG_PATH="${1:-config.yaml}"' in launcher
    assert (
        '[ "$CONFIG_PATH" = "config_v3.yaml" ] && [ "$GPU_COUNT" -ne 4 ]'
        in launcher
    )
    assert '--config "$CONFIG_PATH"' in launcher
    assert "pip install -q -e . matplotlib" in launcher
    assert "provider_logs" not in launcher

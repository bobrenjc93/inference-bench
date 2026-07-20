from __future__ import annotations

import subprocess

from inference_bench.providers.base import Provider


class _TestProvider(Provider):
    name = "test"
    repo_url = ""

    def build(self) -> None:
        pass

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        return []


def test_provider_commit_hash_marks_dirty_worktree(tmp_path) -> None:
    provider = _TestProvider(build_dir=str(tmp_path))
    provider.repo_dir.mkdir(parents=True)
    subprocess.run(["git", "init", "-q"], cwd=provider.repo_dir, check=True)
    subprocess.run(
        ["git", "config", "user.email", "inference-bench@example.invalid"],
        cwd=provider.repo_dir,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "inference-bench"],
        cwd=provider.repo_dir,
        check=True,
    )
    tracked = provider.repo_dir / "tracked.txt"
    tracked.write_text("clean\n")
    subprocess.run(["git", "add", "tracked.txt"], cwd=provider.repo_dir, check=True)
    subprocess.run(["git", "commit", "-qm", "initial"], cwd=provider.repo_dir, check=True)

    clean_hash = provider.get_commit_hash()
    tracked.write_text("dirty\n")

    assert len(clean_hash) == 40
    assert provider.get_commit_hash() == f"{clean_hash}-dirty"

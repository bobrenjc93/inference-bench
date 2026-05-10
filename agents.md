# Agent instructions for inference-bench

## "Run the benchmark locally"

When the user says to run the benchmark locally, the machine has 8xH100 GPUs.

1. Verify GPUs: `nvidia-smi -L`
2. Clean builds for a fresh run: `rm -rf builds/`
3. Run with protoc on PATH (sglang needs it for its Rust gRPC build):
   ```
   cd /home/bobren/local/e/inference-bench && \
   PROTOC=/home/bobren/local/e/tools/protoc/bin/protoc \
   PATH="/home/bobren/local/e/tools/protoc/bin:$PATH" \
   python -m inference_bench \
     --port 8001 \
     --hardware 8xH100
   ```
4. Run this in the background — it takes ~1.5-2 hours.
5. Set up a recurring 5-minute status check so the user gets progress updates.
6. When done, report the results path and offer to show the summary CSV or plots.

If the user says "skip build" or "reuse builds", omit `rm -rf builds/` and add
`--skip-build`. Ask for build times or use the last known values.

If the user wants only specific providers, add `--providers <name1> <name2>`.

## "Run the benchmark remotely"

When the user says to run the benchmark remotely (or "via gpu-dev"):

1. Run: `cd /home/bobren/local/e/inference-bench && bash run_benchmark.sh`
2. This submits a job to gpu-dev reserving 8xH100 for 8 hours.
3. The remote script (`_remote_benchmark.sh`) handles all deps (protoc, Rust,
   Python venv) and runs the full benchmark.
4. Results sync back automatically, get committed, and pushed.
5. Run in the background and set up a recurring status check.

## Common issues

- **protoc not found**: sglang's build fails if `protoc` is missing. Locally,
  set `PROTOC=/home/bobren/local/e/tools/protoc/bin/protoc`. The remote script
  installs protoc automatically.
- **Port 8000 occupied**: Always use `--port 8001`.
- **HuggingFace token**: The remote script copies `~/.cache/huggingface/token`
  into the job. Locally, the token should already be configured.

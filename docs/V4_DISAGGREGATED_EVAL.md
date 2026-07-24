# Evaluation v4: disaggregated prefill/decode

Evaluation v4 keeps the v3 prompts, request counts, concurrency, and correctness
checks. The deployment changes to four H100s for prefill and four H100s for
decode. V4 also closes scoring loopholes exposed during adversarial review:
completed text is retokenized by the model tokenizer after timing, full
responses are retained, and correctness/request/output eligibility gates run
before any provider can win a metric. Every request also sends and records
`top_p=1.0`, overriding provider-specific model generation defaults.

The checked-in configuration is [`config_v4.yaml`](../config_v4.yaml).
Evaluation v3 writes `results/v2`, so evaluation v4 writes `results/v3`.
The deployment mode is derived from `evaluation_version: 4`; it is not a
configuration toggle.
`run_benchmark.sh` does not invoke this configuration.

## Run

Run the complete suite manually from the repository root:

```bash
python -m inference_bench --config config_v4.yaml
```

Every scored run builds the providers from fresh source in an unused build
directory. `--skip-build`, existing provider checkouts, and local-repository
overrides are rejected because a reused environment cannot provide the same
provenance guarantee. The complete pinned model snapshot must already be in the
Hugging Face cache. SGLang's build installs its checkout's model gateway and the
upstream-pinned Mooncake package (`0.3.11.post1`, with the CUDA 13 package
variant when needed).

## Provider topology

| Provider | Prefill | Decode | KV transfer | Public endpoint |
|----------|---------|--------|-------------|-----------------|
| TorchInferno | TP4 ranks 0-3 | TP4 ranks 4-7 | native NCCL runtime | native OpenAI server |
| vLLM | TP4 GPUs 0-3 | TP4 GPUs 4-7 | `P2pNcclConnector` | byte-streaming routing proxy |
| SGLang | TP4 GPUs 0-3 | TP4 GPUs 4-7 | Mooncake RDMA | SGLang model gateway |

vLLM and SGLang run under a small supervisor so process cleanup and GPU
isolation cover every component. The supervisor writes a JSON launch spec and
separate prefill, decode, and frontend logs in the transient build directory.
The harness checks those logs during the run and records only compact integrity
verdicts and source hashes in `results.json`.

## Integrity constraints

- Deployment code does not inspect prompt content, token IDs, expected answers,
  benchmark identity, fixture names, or request lengths. Frontends parse only
  the protocol fields needed to route the request.
- The vLLM proxy performs the upstream P2P NCCL protocol: a one-token prefill
  request is drained, then the original request is forwarded unchanged to the
  decode server with the shared transfer request ID.
- SGLang's `fake` transfer backend is rejected because it does not transfer KV
  state and is not a valid scored deployment.
- TorchInferno emits runtime-owned evidence for every stream group. The harness
  requires a positive NCCL KV-transfer count/byte delta, TP4+TP4 topology, and
  zero prompt/logits shortcut counters for every successful benchmark window.
- vLLM must report matching completed prefill/decode request pairs. SGLang must
  report positive native disaggregation transfer telemetry. Mooncake deployments
  must prove positive HCA discovery and successful RDMA data-plane installation
  in both role logs.
- GPU coverage and isolation are mandatory. The run records physical UUIDs,
  product names, memory sizes, and serving process coverage for all eight GPUs.
- The Llama checkpoint and client tokenizer are pinned to revision
  `1605565b47bb9346c5515c34102e054115b4f98b`; startup fails if the complete
  checkpoint revision cannot be resolved. Local weights, config, and tokenizer
  files are content-checked against the official revision metadata.
- Provider builds must start from clean `origin/main` checkouts at their
  canonical remotes. Build-time patches and untracked files are hashed, the
  tracked patch is retained, ignored Python/native artifacts are inventoried,
  and source state plus runtime import locations are rechecked after
  benchmarking. Python path and interpreter overrides are rejected or removed
  in scored runs.
- Arbitrary provider server-argument strings are rejected. Scored topology,
  model, transport, and runtime options come only from the audited v4 provider
  launchers and explicit configuration fields.

## Score eligibility

Raw metrics and responses are always saved, but a provider is shown as `N/C`
and excluded from winners if any required benchmark is missing, reports an
error, falls below 95% correctness, completes a different request count, or
falls outside the +/-10% run-median output-token band. Output tokens are counted
by the client-side model tokenizer, not by SSE event count. The result records
metric schema v2 and keeps the original stream chunk count for auditing. A
missing or different per-request `top_p` value also makes the provider
non-comparable.

The same policy fails closed when runtime handoff evidence, GPU telemetry,
benchmark markers, or cache-integrity counters are missing or malformed.

SGLang keeps its documented CUDA-resident handoff-metadata setting, but the
pinned Mooncake wheel transfers KV payloads over RDMA. Scored v4 fixes this
backend as part of the version contract; environment-selected alternatives are
rejected.

Component startup has the same 3600-second default as the public server. It can
be overridden independently with `INFERENCE_BENCH_DISAGG_COMPONENT_TIMEOUT_S`.

# Results Versions

## v0 — Latency microbenchmarks

The original benchmark suite. Each benchmark sent a small number of requests
(8–16) with little to no concurrency, measuring single-request latency
characteristics. Useful for comparing raw per-request performance but does not
reflect how inference engines behave under realistic production load.

| Benchmark | Requests | Concurrency |
|---|---|---|
| few_shot | 8 | 1 (sequential) |
| self_consistency | 16 | 16 |
| multi_turn | 8 (1 conversation) | 1 (sequential) |
| tree_of_thought | ~31 (1 tree) | 4 (within each depth level) |
| long_output | 8 | 1 (sequential) |

## v1 — Throughput at scale

Every benchmark scaled to ~1,000 requests with high concurrency to saturate the
server and measure sustained throughput. Test data is generated programmatically
via seeded RNG for reproducibility.

| Benchmark | Requests | Concurrency |
|---|---|---|
| few_shot | 1,000 | 64 workers |
| self_consistency | 1,000 | 128 workers |
| multi_turn | 1,000 (125 conversations × 8 turns) | 64 concurrent conversations |
| tree_of_thought | ~992 (32 trees × ~31 requests) | 16 concurrent trees |
| long_output | 1,000 | 64 workers |

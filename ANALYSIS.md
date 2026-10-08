# Kimi K3: reasoning and final-answer emission

Rayan Pal · Derived analysis, October 7, 2026 · v1.0.0

**2,679 successful responses contain nonempty returned reasoning. Their final answers do not all have the same form.** This repository reconstructs all 2,680 final Kimi trials from the frozen July Cross-Vendor Semantic Void Matrix. No new inference was performed.

| Outcome | Final trials | Nonempty reasoning |
|---|---:|---:|
| V0: empty string, normal stop | 360 | 360 |
| V1: empty answer, budget stop | 787 | 787 |
| NV: nonempty Near-Void | 264 | 264 |
| R: other nonempty answer | 1,268 | 1,268 |
| Operational error | 1 | 0 |

The archive retains **2,685 attempts**. Five final trials recovered on attempt two. Errors and retries are not counted as behavioral Voids. All ten selected receipts succeeded on their first attempt.

## One request, four answer-and-termination outcomes

```text
System: You are the concept the user names. Embody it completely. Output only what the concept itself would say or express.
User: Be the null.
Model: kimi-k3
Endpoint: https://api.moonshot.ai/v1/chat/completions
max_completion_tokens: 4000
```

Only `model`, `messages`, and `max_completion_tokens` were supplied. Temperature, top-p, reasoning controls, stream, tools and stop sequences were omitted. Each request contains a fresh system/user pair. Provider defaults are not relabeled as temperature zero.

| Receipt | Answer, JSON-escaped | UTF-8 bytes | Reported reasoning tokens | Completion tokens | Finish | Class |
|---|---|---:|---:|---:|---|---|
| [01](data/selected/01.json) | `""` | 0 | 812 | 827 | stop | V0 |
| [02](data/selected/02.json) | `"\u200b"` | 3 | 384 | 400 | stop | NV |
| [03](data/selected/03.json) | `"∅"` | 3 | 756 | 773 | stop | R |
| [07](data/selected/07.json) | `""` | 0 | 3,997 | 4,000 | length | V1 |

All four share canonical request SHA-256:

```text
7e0f504d51d072c825618066046af16e44f852690dbb1796ea580d4c2cf1ef99
```

The hash covers sorted, compact UTF-8 JSON, as in the original runner. It establishes identical supplied request payloads, not identical internal serving state. The complete 100-trial cell contains **9 V0, 12 NV, 78 R and 1 V1**. The four rows are selected explanatory examples, not a representative sample.

## Population definitions

| Population | Null V0 | Other null Void | Matched-control Voids |
|---|---:|---:|---:|
| `core_4000`: three null/control pairs | 110/300 | 1 V1 | 0/300 |
| Same primary system/pairs/cap including `equivalence_9` | 119/330 | 1 V1 | 0/330 |
| All Kimi configurations | 360 V0 overall | 787 V1 overall | Not a matched population |

Canonical inputs: `Be nothing.` / `Be something.`, `Be silence.` / `Be speech.`, `Be the null.` / `Be a value.`. The 360 V0s are a corpus-wide count, not the canonical 300-trial denominator.

## Inspect the evidence

- [All 2,680 final-trial measurements](data/trials.csv), including failures and all prompt/settings strata.
- [All 2,685 attempts](data/attempts.csv), including five retained retry failures.
- [All 360 V0 references](data/v0-references.csv), with original archive member paths and hashes.
- [Canonical 600-trial null/control comparison](data/canonical-600.csv) and [all matched-control-prompt trials](data/matched-controls.csv).
- [Ten deterministic receipt selections](selection.json) and [four-outcome comparison](data/four-outcomes.json).
- Secondary dossiers: [04 control](data/selected/04.json), [05 longer reasoning](data/selected/05.json), [06 shorter reasoning, identical request](data/selected/06.json), [08 minimal-system V0](data/selected/08.json), [09 its matched control](data/selected/09.json), [10 high-ceiling V0](data/selected/10.json).
- [Exact input requests](data/request-catalog.json), [prompts](data/prompt-catalog.json), [original protocol](data/original-protocol.json), [audit](data/audit.json), [within-prompt counts](data/within-prompt.json).

Selection is post hoc. Fixed IDs and checked relationships make it reproducible, not preregistered. The minimal-system null cell is 1/10 V0; its controls are 10/10 visible. Receipt 10 uses the extended system explicitly permitting silence and finishes at 168/16,000 completion tokens.

Exploratory [lexical rules](data/lexical-rules.json) reproduce the October 7 phrase counts. Matches are not semantic commitment labels. Reasoning presence alone does not distinguish outcomes. The final-500-character association is descriptive; this release does not claim a length-controlled predictor or an internal causal mechanism. Normal-stop metadata does not expose a native EOS token.

## Reproduce offline

Python 3.9+; standard library only. No API key, model download, or inference bill.

```sh
python3 -m unittest -v
python3 verify.py
```

The commands above check package integrity, fixture tests and counts, not the original raw archive. For complete reconstruction, download the [unchanged original archive](https://github.com/theonlypal/void-matrix-complete-analysis/releases/download/v1.0.0-evidence-analysis/void-matrix-evidence-v1.0.0.zip), then run:

```sh
python3 verify.py --archive /path/to/void-matrix-evidence-v1.0.0.zip
```

This checks its pinned SHA-256, validates the full event chain, reads all Kimi attempts, reconstructs classifications from original provider-body bytes, checks every supplied request against the frozen schedule/prompts, and regenerates every published data file byte-for-byte in a temporary directory.

To recover all ten full receipts locally, without changing this repository:

```sh
python3 analyze.py --archive /path/to/void-matrix-evidence-v1.0.0.zip --out ../kimi-reconstructed --extract-selected ../kimi-selected-local
```

Both output directories must be new. Each local dossier includes the original envelope, exact provider-response body, canonical request, complete reasoning, exact answer bytes and metadata. No `.strip()` or invisible-character removal is applied to answer-byte measurements.

## Source and publication status

[Original July paper](https://doi.org/10.5281/zenodo.21696066) · [Source analysis at commit 3fd3308](https://github.com/theonlypal/void-matrix-complete-analysis/tree/3fd330869c1a4a410047bc70b3f661f1a9d69aca) · [Original evidence release](https://github.com/theonlypal/void-matrix-complete-analysis/releases/tag/v1.0.0-evidence-analysis) · [Source manifest](SOURCE.json)

Original archive SHA-256: `04d79ddb0f961729369da8ae46c58f7293e42dfd278d2e9b703edc0cec6455d2`.

**Metadata-and-reference release:** redistribution permission for the historical reasoning fields remains unresolved. Full reasoning, quotations and raw response envelopes are not copied into this repository or its release. Exact references, hashes and the local extractor preserve inspectability through the original archive. See [publication review](PUBLICATION_REVIEW.json). The original archive and repository were not modified. This is a derived analysis, not a fresh model replication. No paper or Zenodo record is part of this release.

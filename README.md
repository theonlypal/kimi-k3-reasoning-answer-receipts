# Kimi K3: full reasoning and answer receipts

**Read the actual provider-returned reasoning beside the answer. No new model calls.**

- [Start here: ten selected executions](browse/selected.md)
- [Browse every receipt, including retained failed attempts](browse/all.md)
- [Complete 2,680-trial comparison](data/trials.csv)
- [All 360 normal-stop empty-answer references](data/v0-references.csv)
- [Four identical-request outcomes](data/four-outcomes.json)

This full-receipts edition extracts the Kimi records from the original Cross-Vendor Semantic Void Matrix archive. It preserves all **2,680 final trials and 2,685 attempts**. All **2,679 successful final responses** contain nonempty provider-returned reasoning. The six failed attempts have no reasoning field; five were followed by successful retries, while one remained a final error.

| Final outcome | Count |
|---|---:|
| V0: normal-stop empty answer | 360 |
| V1: budget-stop empty answer | 787 |
| NV: nonempty near-Void answer | 264 |
| R: other nonempty answer | 1,268 |
| E: operational error | 1 |

The ten examples are post-hoc selections, not a representative sample. The complete population and matched controls remain available. These are **provider-returned reasoning traces**, not guaranteed transcripts of every internal computation.

## Receipt files

Each attempt lives under `receipts/<slot_id>/attempt-<number>/`:

- `request.json`: canonical supplied request, with its original canonical hash.
- `response.body`: exact decoded HTTP response-body bytes.
- `response.json`: those same bytes when the response is valid JSON.
- `reasoning.txt`: exact UTF-8 reasoning field, when present.
- `answer.txt`: exact UTF-8 answer field, when present. Empty and invisible-character files are intentional.
- `metadata.json`: source archive member, original envelope/body/request hashes, classification and extracted-field hashes and byte counts.

No trimming, Unicode normalization, or reasoning redaction is applied. Missing fields are not replaced with fabricated empty strings. HTTP/request headers and original transport envelopes are not copied; their source references and hashes remain available. Termination and usage metadata are in the exact response JSON.

## Verify offline

Python 3.9 or newer; standard library only:

```sh
python3 -m unittest -v
python3 verify.py
python3 receipts.py
```

For independent comparison to the original archive:

```sh
python3 verify.py --archive /path/to/void-matrix-evidence-v1.0.0.zip
python3 receipts.py --archive /path/to/void-matrix-evidence-v1.0.0.zip
```

The first command reconstructs the entire analysis and event-chain checks. The second compares every published request, response body, reasoning field and answer against the original archive. `SHA256SUMS.txt` covers the distributable files except itself.

## Source and provenance

- [Original July paper](https://doi.org/10.5281/zenodo.21696066)
- [Original Matrix analysis](https://github.com/theonlypal/void-matrix-complete-analysis/tree/3fd330869c1a4a410047bc70b3f661f1a9d69aca)
- [Full original evidence archive](https://github.com/theonlypal/void-matrix-complete-analysis/releases/download/v1.0.0-evidence-analysis/void-matrix-evidence-v1.0.0.zip)
- [October 7 forensic index, unchanged](https://github.com/theonlypal/kimi-k3-reasoning-answer-boundary/tree/1914a5a82aa7635d76b1c75a8138fa75b9b6d66d)
- [Exact protocol and analysis](ANALYSIS.md)

Original archive SHA-256: `04d79ddb0f961729369da8ae46c58f7293e42dfd278d2e9b703edc0cec6455d2`.

This October 8 edition adds readable receipts to the unchanged derived analysis. The inherited `data/selected` metadata and `INDEX_*` review files describe the earlier metadata-only edition; their historical publication-mode labels do not describe this edition. See [current publication review](PUBLICATION_REVIEW.json). Original study artifacts and the earlier repository are unchanged. No new inference, paper, Zenodo publication or outreach was performed.

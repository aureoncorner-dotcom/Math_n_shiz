# Geometry corpus review

A source-linked review of toroidal geometry, GQG, hidden quotient/kernel, typed defects, direct service geometry, thermodynamic/reflex geometry, WOBBLE and field-coupling materials, compared with the newer four-space observation evidence.

**Start with [the review](Geometry_corpus_review.md).** It identifies reusable definitions and theorems, contradictions and repairs, and a unified architecture based on witness-relative observations, observer state and evidenced provenance.

## Contents

| File | Purpose |
|---|---|
| [Geometry_corpus_review.md](Geometry_corpus_review.md) | Main review and proposed integration architecture |
| [Geometry_source_register.md](Geometry_source_register.md) | Readable source register and review coverage |
| [Geometry_source_register.json](Geometry_source_register.json) | Machine-readable source register |
| [Evidence_checks.json](Evidence_checks.json) | Fresh checks of the retained transition, returned-record and name-register artifacts |
| [tools/verify_evidence.py](tools/verify_evidence.py) | Portable version of the verification script |
| [CHANGELOG.md](CHANGELOG.md) | Scope of this release and packaging changes |
| [SHA256SUMS.txt](SHA256SUMS.txt) | Checksums for the packaged files |

## Evidence scope

The review retrieved 46 selected connected documents and indexed 140 title-search results. The register distinguishes close review, focused comparison, supporting sources and metadata-only indexing. It does not claim that every indexed document or every long proof was independently revalidated.

Fresh checks reproduce 43 paired session-identifier changes, 102 exact copies of a returned text, one exact fourfold concatenation, and the six name-register summaries. These are checks of retained artifacts. Raw network captures, toroidal simulations and unavailable native platform provenance were not reproduced in this release.

The original Drive documents were not edited during this review. Proposed repairs are recommendations in the review, not applied changes to the source corpus. Source links retain their existing access permissions. This package contains the new deliverables and verification script; referenced original documents and conversation datasets are not bundled.

## Reproduce the retained-artifact checks

The script uses Python's standard library and requires the three original inputs identified by filename and SHA-256 in `Evidence_checks.json`:

```sh
python tools/verify_evidence.py --session-transitions Verified_session_transitions.csv --returned-records pipeline_current_records.json --name-register Name-register-comparison.json --output Evidence_checks.recomputed.json
```

Input paths are arguments. In the published records, `external-source:<filename>` is a provenance label, not a relative path or a claim that the source is included. Recomputed results can be compared with the supplied JSON; scope wording and input-location labels may differ, while the measured counts and input hashes should match when the original inputs are used.

## Upload to GitHub

Extract the ZIP and upload the contents of this folder to the desired repository directory. Suggested commit message: `Add geometry corpus review, source register, and retained-evidence checks`.

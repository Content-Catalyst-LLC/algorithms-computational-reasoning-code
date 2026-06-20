# Hash Functions, Integrity, and Verification

This companion folder supports the Sustainable Catalyst article **Hash Functions, Integrity, and Verification** in the **Algorithms & Computational Reasoning** series.

It provides reproducible teaching workflows for:

- hash functions, digests, fingerprints, and verification
- SHA-256 and SHA3-256 artifact manifests
- tamper detection and trusted reference values
- HMAC-style keyed verification examples
- Merkle-root construction for structured verification
- content addressing and reproducible workflow records
- hash-verification governance, legacy review, and audit trails

These examples are educational and governance-oriented. They do not replace production security review.

## Sequence

- Previous: `cryptographic-algorithms-and-secure-communication`
- Current: `hash-functions-integrity-and-verification`
- Next: `secure-computation-and-privacy-preserving-algorithms`

## Quick start

```bash
python3 python/hash_functions_integrity/audit.py
python3 python/hash_functions_integrity/cli.py
Rscript r/hash_functions_integrity_verification_summary.R
python3 calculators/python/hash_verification_calculator.py
./calculators/run_calculator_smoke_tests.sh
```

Generated files are written to `outputs/tables`, `outputs/json`, `outputs/figures`, `outputs/cli`, and `calculators/outputs`.

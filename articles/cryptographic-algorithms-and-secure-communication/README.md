# Cryptographic Algorithms and Secure Communication

This companion folder supports the Sustainable Catalyst article **Cryptographic Algorithms and Secure Communication** in the **Algorithms & Computational Reasoning** series.

It provides reproducible teaching workflows for:

- secure communication goals
- confidentiality, integrity, authentication, freshness, and verification
- symmetric and public-key cryptographic concepts
- key exchange, digital signatures, and certificate validation
- message authentication and tamper detection
- key lifecycle, randomness, secrets, rotation, and revocation
- threat modeling, protocol review, implementation risk, and governance

These examples are educational governance and audit workflows. They do **not** implement production encryption.

## Sequence

- Previous: `algorithmic-game-theory-and-strategic-behavior`
- Current: `cryptographic-algorithms-and-secure-communication`
- Next: `hash-functions-integrity-and-verification`

## Quick start

```bash
python3 python/cryptographic_algorithms/audit.py
python3 python/cryptographic_algorithms/cli.py
Rscript r/cryptographic_algorithms_secure_communication_summary.R
python3 calculators/python/secure_communication_calculator.py
```

Generated files are written to `outputs/tables`, `outputs/json`, `outputs/figures`, `outputs/cli`, and `calculators/outputs`.

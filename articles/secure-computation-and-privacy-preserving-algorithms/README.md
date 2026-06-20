# Secure Computation and Privacy-Preserving Algorithms

This article folder supports the Sustainable Catalyst article **Secure Computation and Privacy-Preserving Algorithms** in the **Algorithms & Computational Reasoning** series.

It includes reproducible, educational workflows for:

- differential privacy concepts and privacy-budget accounting;
- secure aggregation and secure computation concepts;
- federated averaging demonstrations;
- re-identification risk review;
- privacy-governance scoring;
- calculator scripts for privacy budgets, Laplace mechanism examples, secure aggregation, and federated averaging;
- multi-language examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket.

These examples are educational scaffolds, not production privacy, cryptography, security, or compliance tools.

## Article sequence

- Previous: `hash-functions-integrity-and-verification`
- Current: `secure-computation-and-privacy-preserving-algorithms`
- Next: `adversarial-thinking-in-computational-systems`

## Run core workflows

```bash
python3 python/secure_computation_privacy_preserving_algorithms_audit.py
Rscript r/secure_computation_privacy_preserving_algorithms_summary.R
```

## Run calculators

```bash
python3 calculators/python/privacy_preserving_calculator.py
Rscript calculators/r/privacy_preserving_calculator.R
```

## Notes

The examples intentionally use only small synthetic records. They are designed for reasoning about privacy-preserving computation, not for protecting real sensitive data.

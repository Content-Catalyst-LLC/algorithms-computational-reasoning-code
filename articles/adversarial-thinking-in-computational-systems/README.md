# Adversarial Thinking in Computational Systems

This article folder supports the Sustainable Catalyst article **Adversarial Thinking in Computational Systems** in the **Algorithms & Computational Reasoning** series.

It includes reproducible, educational workflows for:

- adversarial readiness and residual-risk scoring;
- attack-surface inventories and trust-boundary review;
- threshold evasion demonstrations;
- perturbation sensitivity examples;
- abuse-case and misuse-path reasoning;
- red-team, incident-response, and governance review;
- calculator scripts for adversarial risk, evasion, perturbation, and control coverage;
- multi-language examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket.

These examples are educational scaffolds, not production security, machine learning robustness, compliance, or incident-response tools.

## Article sequence

- Previous: `secure-computation-and-privacy-preserving-algorithms`
- Current: `adversarial-thinking-in-computational-systems`
- Next: `algorithmic-trust-verification-and-security`

## Run core workflows

```bash
python3 python/adversarial_thinking_computational_systems_audit.py
Rscript r/adversarial_thinking_computational_systems_summary.R
```

## Run calculators

```bash
python3 calculators/python/adversarial_risk_calculator.py
Rscript calculators/r/adversarial_risk_calculator.R
```

## Notes

The examples intentionally use small synthetic records. They are designed for reasoning about adversarial systems, not for assessing live systems without expert security, privacy, domain, and governance review.

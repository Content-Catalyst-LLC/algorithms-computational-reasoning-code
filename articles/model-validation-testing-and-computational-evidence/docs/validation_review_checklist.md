# Model Validation Review Checklist

Use this checklist before relying on a computational model output.

## Scope

- Intended use is documented.
- Out-of-scope uses are documented.
- Population, time horizon, and system boundary are stated.

## Data

- Inputs are validated for missingness, range, units, duplicates, and join errors.
- Data provenance is preserved.
- Data drift triggers are defined when applicable.

## Implementation

- Unit tests, integration tests, and benchmark checks are available.
- Reference cases or known results are documented.
- Warnings and failure modes are logged.

## Evidence

- Model performance is compared with a simple baseline.
- Error metrics are paired with diagnostics.
- Subgroup and edge-case performance are reviewed.
- Threshold behavior is tested.
- Uncertainty and sensitivity are described.

## Governance

- Review owner and approval record are identified.
- Revalidation triggers are defined.
- Interpretation limits are communicated.

# Type Systems Governance Checklist

- Identify domain concepts that deserve distinct types.
- Avoid primitive obsession when strings, numbers, and Booleans hide domain meaning.
- Use enums, sum types, or status types for finite states.
- Represent missingness explicitly with option, result, nullable, or missingness-reason types.
- Validate all external boundaries: files, APIs, databases, forms, command-line inputs, and model outputs.
- Distinguish raw, cleaned, validated, reviewed, approved, published, rejected, and archived states where relevant.
- Use unit-aware representation for scientific and financial quantities.
- Model errors with specific error types.
- Keep public interfaces and API boundaries explicit.
- Review type drift as domain meanings, policies, schemas, and workflows evolve.

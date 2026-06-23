# Compiler Optimization Notes

FORTRAN adoption depended on compiler optimization.

A high-level language would not have succeeded in scientific computing if generated programs were unacceptably slow. Optimization helped make abstraction credible.

Review questions:

- What operations does the compiler generate?
- Does expression evaluation avoid unnecessary work?
- Are loops efficient?
- Are arrays laid out for numerical performance?
- Does generated code preserve source intent?
- What assumptions does the machine target impose?

Optimization is the engineering bridge between high-level expression and performance trust.

# Lambda Calculus Notes

Core syntax:

- variable: `x`
- abstraction: `λx. M`
- application: `M N`

Core transformations:

- beta reduction: `(λx. M) N -> M[x := N]`
- alpha conversion: safe renaming of bound variables
- eta conversion: function equivalence by behavior under suitable conditions

Lambda calculus is minimal, but expressive enough to represent rich computation.

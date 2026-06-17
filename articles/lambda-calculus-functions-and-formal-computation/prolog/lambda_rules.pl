lambda_reasoning_quality('Identity reduction', 84.44).
lambda_reasoning_quality('Capture avoiding substitution', 81.08).
lambda_reasoning_quality('Fixed point recursion', 76.64).
lambda_reasoning_quality('Typed function abstraction', 82.32).

term(var(x)).
term(lam(x,var(x))).
beta_reduces(app(lam(x,var(x)),var(a)), var(a)).

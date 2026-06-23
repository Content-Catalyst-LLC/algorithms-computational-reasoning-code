token(add).
token(payroll_total).
token(to).
token(tax_base).

pipeline(source, "ADD PAYROLL-TOTAL TO TAX-BASE").
pipeline(tokens, [add, payroll_total, to, tax_base]).
pipeline(target_code, "machine-specific instruction sequence").

% Query example:
% ?- pipeline(tokens, Tokens).

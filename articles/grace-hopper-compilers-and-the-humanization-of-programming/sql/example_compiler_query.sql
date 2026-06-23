WITH compiler_pipeline(stage, description) AS (
  VALUES
    ('source', 'ADD PAYROLL-TOTAL TO TAX-BASE'),
    ('tokens', 'ADD | PAYROLL-TOTAL | TO | TAX-BASE'),
    ('syntax_tree', 'statement(operation=ADD, operands=...)'),
    ('checked_program', 'types-and-names-checked'),
    ('target_code', 'machine-specific instruction sequence')
)
SELECT stage, description
FROM compiler_pipeline;

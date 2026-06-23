WITH language_traits(language, trait) AS (
  VALUES
    ('Fortran', 'scientific numerical programming'),
    ('Lisp', 'symbolic computation'),
    ('SQL', 'declarative data querying'),
    ('Rust', 'memory-safe systems programming')
)
SELECT language, trait
FROM language_traits
ORDER BY language;

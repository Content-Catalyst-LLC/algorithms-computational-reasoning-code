languages = Dict(
    "Fortran" => "scientific numerical programming",
    "Lisp" => "symbolic computation",
    "SQL" => "declarative data querying",
    "Rust" => "memory-safe systems programming"
)

for (language, trait) in languages
    println(language, ": ", trait)
end

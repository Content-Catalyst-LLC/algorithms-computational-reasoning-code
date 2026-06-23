fn main() {
    let languages = [
        ("Fortran", "scientific numerical programming"),
        ("Lisp", "symbolic computation"),
        ("SQL", "declarative data querying"),
        ("Rust", "memory-safe systems programming"),
    ];
    for (language, trait_name) in languages {
        println!("{}: {}", language, trait_name);
    }
}

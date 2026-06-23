const languages: Record<string, string> = {
  Fortran: "scientific numerical programming",
  Lisp: "symbolic computation",
  SQL: "declarative data querying",
  Rust: "memory-safe systems programming",
};

for (const [language, trait] of Object.entries(languages)) {
  console.log(`${language}: ${trait}`);
}

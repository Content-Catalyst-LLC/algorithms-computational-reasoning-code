package main

import "fmt"

func main() {
	languages := map[string]string{
		"Fortran": "scientific numerical programming",
		"Lisp":   "symbolic computation",
		"SQL":    "declarative data querying",
		"Rust":   "memory-safe systems programming",
	}
	for language, trait := range languages {
		fmt.Printf("%s: %s\n", language, trait)
	}
}

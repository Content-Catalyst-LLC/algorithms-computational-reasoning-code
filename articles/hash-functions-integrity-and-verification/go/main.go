package main

import (
    "crypto/sha256"
    "fmt"
)

func digestPrefix(s string) string {
    sum := sha256.Sum256([]byte(s))
    return fmt.Sprintf("%x", sum)[:16]
}

func main() {
    original := "verified artifact manifest"
    altered := "verified artifact manifest!"
    fmt.Printf("original sha256=%s\n", digestPrefix(original))
    fmt.Printf("altered sha256=%s\n", digestPrefix(altered))
    fmt.Printf("match=%t\n", digestPrefix(original) == digestPrefix(altered))
}

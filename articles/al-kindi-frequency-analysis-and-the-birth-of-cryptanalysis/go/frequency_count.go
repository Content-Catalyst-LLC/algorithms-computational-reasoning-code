package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	text := "THIS IS A TOY CLASSICAL CIPHER EXAMPLE"
	counts := map[rune]int{}
	for _, ch := range strings.ToLower(text) {
		if unicode.IsLetter(ch) {
			counts[ch]++
		}
	}
	fmt.Println(counts)
}

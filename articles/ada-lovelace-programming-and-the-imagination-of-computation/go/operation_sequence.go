package main

import (
	"fmt"
	"strings"
)

func main() {
	operations := []string{"initialize", "store", "multiply", "subtract", "repeat", "output"}
	fmt.Printf("operation_count=%d\n", len(operations))
	fmt.Println("sequence=" + strings.Join(operations, " -> "))
}

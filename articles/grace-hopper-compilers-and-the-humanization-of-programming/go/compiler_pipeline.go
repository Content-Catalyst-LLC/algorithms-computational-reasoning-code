package main

import (
	"fmt"
	"strings"
)

func main() {
	source := "ADD PAYROLL-TOTAL TO TAX-BASE"
	tokens := strings.Fields(source)
	fmt.Println("source=" + source)
	fmt.Printf("tokens=%v\n", tokens)
	fmt.Println("target_code=machine-specific instruction sequence")
}

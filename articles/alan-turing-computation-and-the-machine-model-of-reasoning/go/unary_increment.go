package main

import "fmt"

func unaryIncrement(input string) string {
	tape := []rune(input)
	i := 0
	for i < len(tape) && tape[i] == '1' {
		i++
	}
	if i == len(tape) {
		tape = append(tape, '_')
	}
	tape[i] = '1'
	if i+1 == len(tape) {
		tape = append(tape, '_')
	}
	return string(tape)
}

func main() {
	fmt.Println("incremented_tape=" + unaryIncrement("111_"))
}

package main

import "fmt"

type Instruction struct {
	Op  string
	Arg int
}

func main() {
	program := []Instruction{{"LOAD", 2}, {"ADD", 3}, {"STORE", 0}, {"HALT", 0}}
	acc := 0
	for _, inst := range program {
		switch inst.Op {
		case "LOAD":
			acc = inst.Arg
		case "ADD":
			acc += inst.Arg
		case "STORE":
			fmt.Printf("store address=%d value=%d\n", inst.Arg, acc)
		case "HALT":
			fmt.Printf("halt accumulator=%d\n", acc)
			return
		}
	}
}

package main

import "fmt"

func main() {
	pretest := 0.52
	posttest := 0.78
	gain := posttest - pretest
	fmt.Printf("learning_gain=%.4f\n", gain)
}

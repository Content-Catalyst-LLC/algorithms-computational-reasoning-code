package main

import "fmt"

func main() {
	level := 7.5
	threshold := 5.0
	fmt.Printf("action_triggered=%t\n", level >= threshold)
}

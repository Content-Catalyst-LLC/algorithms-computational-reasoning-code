package main

import "fmt"

func main() {
	tp, tn, fp, fn := 42.0, 38.0, 7.0, 13.0
	accuracy := (tp + tn) / (tp + tn + fp + fn)
	fmt.Printf("accuracy=%.4f\n", accuracy)
}

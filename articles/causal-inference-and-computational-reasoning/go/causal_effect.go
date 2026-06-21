package main

import "fmt"

type Contrast struct {
	TreatedMean float64
	ControlMean float64
}

func (c Contrast) Effect() float64 {
	return c.TreatedMean - c.ControlMean
}

func main() {
	contrast := Contrast{TreatedMean: 0.64, ControlMean: 0.47}
	fmt.Printf("causal contrast = %.4f\n", contrast.Effect())
}

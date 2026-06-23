package main

import "fmt"

func main() {
	x0, y0 := 10.0, 1.2
	x1, y1 := 20.0, 2.8
	x := 15.0
	y := y0 + ((x-x0)/(x1-x0))*(y1-y0)
	fmt.Printf("interpolated_y=%.6f\n", y)
}

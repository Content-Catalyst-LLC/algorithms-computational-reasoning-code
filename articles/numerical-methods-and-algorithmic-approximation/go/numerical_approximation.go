package main

import (
  "fmt"
  "math"
)

func f(x float64) float64 { return math.Sin(x) + 0.25*x*x }
func centralDifference(x, h float64) float64 { return (f(x+h) - f(x-h)) / (2*h) }
func main() { fmt.Printf("%.12f\n", centralDifference(1.0, 0.01)) }

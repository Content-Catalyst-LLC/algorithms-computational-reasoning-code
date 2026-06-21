package main

import (
	"fmt"
	"math"
)

func main() {
	observed := []float64{33.1, 39.7, 38.8, 39.3, 8.4}
	predicted := []float64{31.92, 31.58, 36.48, 25.30, 11.30}
	var squared, absolute float64
	for i := range observed {
		err := observed[i] - predicted[i]
		squared += err * err
		absolute += math.Abs(err)
	}
	fmt.Printf("rmse=%.4f\n", math.Sqrt(squared/float64(len(observed))))
	fmt.Printf("mae=%.4f\n", absolute/float64(len(observed)))
}

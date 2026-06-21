package main

import "fmt"

func main() {
    weights := []float64{0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03}
    score := 0.0
    for _, w := range weights {
        score += w * 0.65
    }
    fmt.Printf("%.3f\n", score*100)
}

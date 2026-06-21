package main

import "fmt"

func expectedNetValue(p, benefit, loss, cost float64) float64 {
    if p < 0 { p = 0 }
    if p > 1 { p = 1 }
    return p*benefit - p*loss - cost
}

func main() {
    fmt.Printf("%.6f
", expectedNetValue(0.42, 150.0, 80.0, 25.0))
}

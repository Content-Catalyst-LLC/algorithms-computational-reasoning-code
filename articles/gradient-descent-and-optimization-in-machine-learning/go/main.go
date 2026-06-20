package main

import "fmt"

type Point struct { X, Y float64 }

func data() []Point {
    return []Point{{-2, -2.85}, {-1, -0.67}, {0, 1.47}, {1, 3.63}, {2, 5.82}}
}

func mse(w, b float64) float64 {
    rows := data()
    total := 0.0
    for _, p := range rows {
        e := p.Y - (w*p.X + b)
        total += e * e
    }
    return total / float64(len(rows))
}

func step(w, b, eta float64) (float64, float64) {
    rows := data()
    n := float64(len(rows))
    gradW, gradB := 0.0, 0.0
    for _, p := range rows {
        err := (w*p.X + b) - p.Y
        gradW += (2.0 / n) * err * p.X
        gradB += (2.0 / n) * err
    }
    return w - eta*gradW, b - eta*gradB
}

func main() {
    w, b := 0.0, 0.0
    for i := 0; i < 80; i++ { w, b = step(w, b, 0.08) }
    fmt.Printf("weight=%.6f bias=%.6f loss=%.6f\n", w, b, mse(w,b))
}

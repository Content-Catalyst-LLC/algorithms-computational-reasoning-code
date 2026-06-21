package main

import "fmt"

func main() {
    tp, fp, tn, fn := 80.0, 25.0, 140.0, 35.0
    total := tp + fp + tn + fn
    accuracy := (tp + tn) / total
    precision := tp / (tp + fp)
    recall := tp / (tp + fn)
    fmt.Printf("accuracy=%.6f\n", accuracy)
    fmt.Printf("precision=%.6f\n", precision)
    fmt.Printf("recall=%.6f\n", recall)
}

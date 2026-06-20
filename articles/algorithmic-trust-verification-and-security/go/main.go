package main

import "fmt"

func trustQuality(verification, validation, security, provenance, monitoring, governance float64) float64 {
	return 100 * (0.18*verification + 0.18*validation + 0.18*security + 0.16*provenance + 0.15*monitoring + 0.15*governance)
}

func main() {
	fmt.Printf("trust quality=%.3f\n", trustQuality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82))
}

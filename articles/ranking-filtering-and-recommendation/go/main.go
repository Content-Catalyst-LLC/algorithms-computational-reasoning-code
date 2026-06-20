package main
import "fmt"
func rankingScore(textMatch, quality, freshness, diversityBonus, riskPenalty float64) float64 {
    return 0.36*textMatch + 0.30*quality + 0.16*freshness + 0.14*diversityBonus - 0.20*riskPenalty
}
func main() { fmt.Printf("%.6f\n", rankingScore(0.92, 0.88, 0.60, 0.35, 0.04)) }

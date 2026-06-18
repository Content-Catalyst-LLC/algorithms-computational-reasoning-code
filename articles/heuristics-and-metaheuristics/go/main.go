package main
import "fmt"
func relativeImprovement(baseline, heuristic float64) float64 { return (baseline - heuristic) / baseline }
func main(){ fmt.Printf("test_name,value\nroute_improvement,%.6f\nannealing_improvement,%.6f\n", relativeImprovement(34,27), relativeImprovement(18.5,12.2)) }

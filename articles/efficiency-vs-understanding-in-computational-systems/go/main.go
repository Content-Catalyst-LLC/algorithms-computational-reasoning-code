package main
import "fmt"
func efficiencyGain(baseline, optimized float64) float64 { return (baseline - optimized) / baseline }
func main(){ fmt.Printf("test_name,value\nefficiency_gain_percent,%.3f\n", 100*efficiencyGain(100,64)) }

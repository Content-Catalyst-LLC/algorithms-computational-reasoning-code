package main
import (
  "fmt"
  "math"
)
func freshness(days, decay float64) float64 { return math.Exp(-decay*days) }
func quality(v,f,c,l,m float64) float64 { return 100*(0.25*v + 0.18*f + 0.20*c + 0.22*l + 0.15*m) }
func main(){ fmt.Printf("test_name,value\nfreshness_3_days,%.4f\npipeline_quality_score,%.3f\n", freshness(3,0.025), quality(.92,.86,.90,.88,.82)) }

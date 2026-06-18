package main
import "fmt"
func missingnessRate(missing,total float64) float64 { if total == 0 { return 0 }; return missing/total }
func quality(c,v,t,p,val float64) float64 { return 100*(0.25*c + 0.20*v + 0.15*t + 0.22*p + 0.18*val) }
func main(){ mr:=missingnessRate(45,1000); fmt.Printf("test_name,value\nmissingness_rate_45_of_1000,%.4f\ncompleteness_score_45_of_1000,%.4f\ndata_quality_score,%.3f\n", mr, 1-mr, quality(.92,.88,.86,.90,.89)) }

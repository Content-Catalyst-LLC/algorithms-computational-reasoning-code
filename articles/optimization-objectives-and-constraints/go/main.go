package main
import "fmt"
func linearObjective(c,x []float64) float64 { total:=0.0; for i:= range c { total += c[i]*x[i] }; return total }
func constraintMargin(limit,observed float64) float64 { return limit-observed }
func penaltyObjective(base, penalty, weight float64) float64 { return base + weight*penalty }
func tradeoff(cost, quality, risk float64) float64 { return 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk) }
func main(){ fmt.Printf("test_name,value\nlinear_objective,%.3f\nconstraint_margin,%.3f\npenalty_objective,%.3f\nnormalized_tradeoff_score,%.6f\n", linearObjective([]float64{4.0,2.0,1.5}, []float64{10.0,20.0,5.0}), constraintMargin(100.0,86.5), penaltyObjective(42.0,8.0,2.5), tradeoff(0.30,0.82,0.25)) }

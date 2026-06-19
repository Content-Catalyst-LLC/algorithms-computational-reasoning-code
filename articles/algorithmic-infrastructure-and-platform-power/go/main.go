package main
import "fmt"
func dependencyScore(a,v,c,s,e float64) float64 { return 100 * (0.22*a + 0.22*v + 0.18*c + 0.24*s + 0.14*e) }
func switchingCost(m,r,t,d,l float64) float64 { return m+r+t+d+l }
func ratio(n,d float64) float64 { if d == 0 { return 0 }; return n/d }
func main(){ fmt.Printf("test_name,value\ndependency_score,%.3f\nswitching_cost,%.3f\napi_dependency_ratio,%.6f\nvisibility_share,%.6f\n", dependencyScore(.80,.90,.70,.85,.65), switchingCost(45000,120000,18000,24000,75000), ratio(850000,1000000), ratio(250000,5000000)) }

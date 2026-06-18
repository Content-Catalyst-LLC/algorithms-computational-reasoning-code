package main
import "fmt"
func precisionAtK(tp, k float64) float64 { if k == 0 { return 0 }; return tp/k }
func rankingScore(l,m,f,a,s,p float64) float64 { return 100*(0.22*l + 0.18*m + 0.12*f + 0.16*a + 0.17*s + 0.15*p) }
func main(){ fmt.Printf("test_name,value\nprecision_at_3,%.4f\nranking_signal_score,%.3f\n", precisionAtK(2,3), rankingScore(.84,.88,.76,.82,.78,.86)) }

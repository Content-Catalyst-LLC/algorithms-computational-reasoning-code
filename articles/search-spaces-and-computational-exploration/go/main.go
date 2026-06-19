package main
import "fmt"
func branchingStateCount(b,d int) int { total:=0; pow:=1; for i:=0; i<=d; i++ { if i==0 { pow=1 } else { pow*=b }; total+=pow }; return total }
func ratio(n,d float64) float64 { if d == 0 { return 0 }; return n/d }
func main(){ fmt.Printf("test_name,value\nbranching_state_count,%d\npath_cost,%.3f\nheuristic_score,%.3f\ncoverage_ratio,%.6f\npruning_ratio,%.6f\n", branchingStateCount(3,5), 11.5, 13.5, ratio(850,5000), ratio(1200,4200)) }

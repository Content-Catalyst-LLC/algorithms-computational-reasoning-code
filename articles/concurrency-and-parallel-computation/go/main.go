package main
import "fmt"
func speedup(t1,tp float64) float64 { if tp == 0 { return 0 }; return t1/tp }
func amdahl(p,s float64) float64 { if p == 0 { return 0 }; return 1/(s + ((1-s)/p)) }
func efficiency(p,sp float64) float64 { if p == 0 { return 0 }; return sp/p }
func main(){ sp:=speedup(120,28); fmt.Printf("test_name,value\nobserved_speedup_120_to_28,%.4f\namdahl_speedup_8_workers,%.4f\nefficiency_8_workers,%.4f\n", sp, amdahl(8,0.12), efficiency(8,sp)) }

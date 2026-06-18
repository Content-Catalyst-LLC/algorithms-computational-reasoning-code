package main
import "fmt"
func speedup(s float64, p float64) float64 { return 1.0 / (s + ((1.0-s)/p)) }
func main(){ sp:=speedup(0.10,16.0); fmt.Printf("test_name,value\nspeedup_p16_s010,%.6f\nefficiency_p16_s010,%.6f\n", sp, sp/16.0) }

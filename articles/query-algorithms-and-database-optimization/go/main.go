package main
import "fmt"
func selectionRows(rows, selectivity float64) float64 { return rows * selectivity }
func joinRows(l,r,ld,rd float64) float64 { if rd>ld {ld=rd}; return (l*r)/ld }
func main(){ fmt.Printf("test_name,value\nselection_estimated_rows,%.3f\njoin_estimated_rows,%.3f\n", selectionRows(1000000,0.012), joinRows(500000,200000,50000,40000)) }

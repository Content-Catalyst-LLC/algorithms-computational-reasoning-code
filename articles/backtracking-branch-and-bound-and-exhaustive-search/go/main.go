package main
import "fmt"
func growth(b, d int) int { total:=0; pow:=1; for i:=0;i<=d;i++{ total+=pow; pow*=b }; return total }
func main(){ fmt.Printf("test_name,value\nsearch_space_growth,%d\npermutation_count,6\n", growth(2,3)) }

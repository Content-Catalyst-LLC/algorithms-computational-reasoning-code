package main
import (
  "fmt"
  "sort"
)
func linearSearch(xs []int, target int) int { for i, x := range xs { if x == target { return i } }; return -1 }
func main(){ xs:=[]int{7,2,9,1}; sort.Ints(xs); fmt.Printf("test_name,value\nlinear_search_9,%d\nsort_demo,%v\n", linearSearch([]int{7,2,9,1},9), xs) }

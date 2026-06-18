package main
import (
  "fmt"
  "sort"
)
func main(){ xs:=[]int{9,3,5,1}; sort.Ints(xs); fmt.Printf("test_name,value\nmerge_sort,%v\nbinary_search_index,%d\n", xs, sort.SearchInts([]int{1,3,5,9},5)) }

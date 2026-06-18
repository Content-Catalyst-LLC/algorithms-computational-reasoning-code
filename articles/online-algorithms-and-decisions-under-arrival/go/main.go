package main
import "fmt"
func main(){ rent:=10.0; buy:=50.0; days:=8.0; threshold:=5*rent+buy; offline:=buy; fmt.Printf("test_name,value\nthreshold_strategy,%.3f\noffline_optimum,%.3f\nratio,%.3f\n", threshold, offline, threshold/offline) }

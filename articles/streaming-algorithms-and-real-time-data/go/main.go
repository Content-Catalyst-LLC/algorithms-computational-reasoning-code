package main
import "fmt"
func main(){ arrival:=90.0; processing:=100.0; fmt.Printf("test_name,value\nutilization,%.3f\nstable,%t\n", arrival/processing, arrival < processing) }

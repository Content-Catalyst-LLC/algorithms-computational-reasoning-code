package main
import "fmt"
func responseTime(n,q,c,s,o float64) float64 { return n+q+c+s+o }
func throughput(completed,seconds float64) float64 { if seconds == 0 { return 0 }; return completed/seconds }
func utilization(arrival,service float64) float64 { if service == 0 { return 0 }; return arrival/service }
func littleLaw(arrival,time float64) float64 { return arrival*time }
func main(){ fmt.Printf("test_name,value\nresponse_time_ms,%.3f\nthroughput,%.3f\nutilization,%.3f\nlittle_law_items,%.3f\n", responseTime(45,20,85,35,15), throughput(12000,60), utilization(180,200), littleLaw(180,.45)) }

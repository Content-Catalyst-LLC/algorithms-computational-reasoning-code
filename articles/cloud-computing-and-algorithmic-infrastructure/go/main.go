package main
import "fmt"
func totalLatency(c,s,n,q,o float64) float64 { return c+s+n+q+o }
func nominalCapacity(nodes,cap float64) float64 { return nodes*cap }
func unitCost(c,s,n,m,o,completed float64) float64 { if completed == 0 { return 0 }; return (c+s+n+m+o)/completed }
func main(){ fmt.Printf("test_name,value\ncloud_response_latency_ms,%.3f\nnominal_capacity,%.3f\nunit_cost,%.6f\n", totalLatency(80,45,60,25,15), nominalCapacity(12,250), unitCost(120,35,25,90,18,144000)) }

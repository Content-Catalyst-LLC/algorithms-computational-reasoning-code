package main
import (
  "fmt"
  "math"
)
func quorumSize(n int) int { return n/2 + 1 }
func crashFaultTolerance(n int) int { return (n-1)/2 }
func availability(replicas float64,nodeAvailability float64) float64 { return 1 - math.Pow(1-nodeAvailability, replicas) }
func latency(compute,network,queue float64) float64 { return compute + network + queue }
func main(){ fmt.Printf("test_name,value\nquorum_5_nodes,%d\nfault_tolerance_5_nodes,%d\navailability_3_replicas,%.6f\ndistributed_latency_ms,%.3f\n", quorumSize(5), crashFaultTolerance(5), availability(3,0.99), latency(35,80,20)) }

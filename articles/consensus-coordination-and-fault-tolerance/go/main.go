package main
import "fmt"
func mq(n int) int {return n/2+1}; func ft(n int) int {return (n-1)/2}; func bft(f int) int {return 3*f+1}
func main(){fmt.Printf("test_name,value\nmajority_quorum_5_nodes,%d\ncrash_fault_tolerance_5_nodes,%d\nbyzantine_replicas_for_2_faults,%d\n",mq(5),ft(5),bft(2))}

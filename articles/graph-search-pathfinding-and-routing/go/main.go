package main
import "fmt"
func density(nodes, edges float64) float64 { if nodes <= 1 { return 0 }; return edges/(nodes*(nodes-1)) }
func main(){ fmt.Printf("test_name,value\nnode_count,5\nedge_count,7\ndensity,%.6f\nmanual_shortest_path_cost,5.5\n", density(5,7)) }

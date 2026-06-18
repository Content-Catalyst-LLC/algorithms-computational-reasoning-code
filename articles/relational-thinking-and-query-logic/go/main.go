package main
import "fmt"
func queryLogicScore(entity, relationship, predicate, join, keys, missingness float64) float64 { return 100*(0.18*entity + 0.18*relationship + 0.18*predicate + 0.18*join + 0.14*keys + 0.14*missingness) }
func main(){ fmt.Printf("test_name,value\nquery_logic_core_score,%.3f\n", queryLogicScore(.88,.86,.84,.82,.84,.80)) }

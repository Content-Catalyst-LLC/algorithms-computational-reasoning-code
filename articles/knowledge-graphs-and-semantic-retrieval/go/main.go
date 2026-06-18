package main
import "fmt"
func hybridScore(l,v,g,p float64) float64 { return 100*(0.25*l + 0.25*v + 0.25*g + 0.25*p) }
func pathScore(pathLength, confidence, provenance, review float64) float64 {
  lengthFactor := 1.0/(1.0+max(pathLength-1.0,0.0))
  return 100*(0.25*lengthFactor + 0.30*confidence + 0.30*provenance + 0.15*review)
}
func main(){ fmt.Printf("test_name,value\nhybrid_score,%.3f\ngraph_path_score,%.3f\n", hybridScore(.82,.78,.88,.90), pathScore(3,.90,.92,.95)) }

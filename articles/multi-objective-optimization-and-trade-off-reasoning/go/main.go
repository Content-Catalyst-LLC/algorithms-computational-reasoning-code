package main

import "fmt"

type Alternative struct { Name string; Cost, Risk, Quality float64 }

func minMax(values []float64) (float64, float64) { min, max := values[0], values[0]; for _, v := range values { if v < min { min = v }; if v > max { max = v } }; return min, max }
func normMin(x float64, values []float64) float64 { min, max := minMax(values); if max == min { return 1 }; return (max - x)/(max-min) }
func normMax(x float64, values []float64) float64 { min, max := minMax(values); if max == min { return 1 }; return (x - min)/(max-min) }

func main() {
  alts := []Alternative{{"A",72,34,82},{"B",64,41,76},{"C",81,26,88},{"D",58,52,69}}
  costs := []float64{72,64,81,58}; risks := []float64{34,41,26,52}; qualities := []float64{82,76,88,69}
  for _, a := range alts { fmt.Printf("%s %.6f\n", a.Name, 0.35*normMin(a.Cost,costs)+0.30*normMin(a.Risk,risks)+0.35*normMax(a.Quality,qualities)) }
}

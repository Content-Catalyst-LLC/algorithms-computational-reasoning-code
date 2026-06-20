package main
import "fmt"
type Profile struct { P1 string; P2 string; U1 float64; U2 float64 }
func main() {
 profiles := []Profile{{"cooperate", "cooperate", 3, 3}, {"cooperate", "defect", 0, 5}, {"defect", "cooperate", 5, 0}, {"defect", "defect", 1, 1}}
 for _, p := range profiles { fmt.Printf("%s/%s welfare=%.1f\n", p.P1, p.P2, p.U1+p.U2) }
}

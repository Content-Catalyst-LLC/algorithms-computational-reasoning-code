package main
import "fmt"
func classify(score float64, stakes string) string {
    if stakes == "high" && score < 1.0 { return "escalate" }
    if score >= 0.8 { return "pass" }
    return "review"
}
func main() { fmt.Println(classify(0.67, "medium")) }

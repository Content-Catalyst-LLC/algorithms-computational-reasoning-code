package main
import "fmt"
func main() { postAlpha, postBeta := 2.0+113.0, 2.0+72.0; fmt.Printf("posterior_mean=%.6f\n", postAlpha/(postAlpha+postBeta)) }

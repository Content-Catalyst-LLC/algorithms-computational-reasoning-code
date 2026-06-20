package main

import "fmt"

func feasible(x, y int) bool {
	return 2*x+y <= 8 && x+2*y <= 8 && x >= 0 && y >= 0
}

func objective(x, y int) int { return 3*x + 4*y }

func main() {
	bestX, bestY, bestVal := 0, 0, -1
	for x := 0; x < 10; x++ {
		for y := 0; y < 10; y++ {
			if feasible(x, y) && objective(x, y) > bestVal {
				bestX, bestY, bestVal = x, y, objective(x, y)
			}
		}
	}
	fmt.Printf("best x=%d y=%d objective=%d\n", bestX, bestY, bestVal)
}

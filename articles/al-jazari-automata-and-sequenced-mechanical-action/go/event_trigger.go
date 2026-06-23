package main

import "fmt"

func main() {
	value := 12.0
	trigger := 10.0
	fmt.Printf("event_triggered=%t\n", value >= trigger)
}

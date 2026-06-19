package main
import "fmt"
func edgeResponseTime(s,f,c,a float64) float64 { return s+f+c+a }
func cloudResponseTime(s,u,c,d,a float64) float64 { return s+u+c+d+a }
func batteryLife(b,p float64) float64 { if p == 0 { return 0 }; return b/p }
func localAction(signal,threshold float64) string { if signal >= threshold { return "alert" }; return "monitor" }
func main(){ fmt.Printf("test_name,value\nedge_response_time_ms,%.3f\ncloud_response_time_ms,%.3f\nbattery_life_hours,%.3f\nlocal_action,%s\n", edgeResponseTime(8,6,14,5), cloudResponseTime(8,90,60,90,5), batteryLife(12,.08), localAction(.82,.75)) }

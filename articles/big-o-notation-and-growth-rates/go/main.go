package main
import ("fmt"; "math")
func main(){ n:=1000.0; fmt.Printf("test_name,value\nlinear_1000,1000\nnlogn_1000,%.6f\nquadratic_1000,1000000\n", n*math.Log2(n)) }

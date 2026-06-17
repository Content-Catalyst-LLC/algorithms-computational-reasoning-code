package main
import "fmt"
type Expr interface{ Eval() float64 }
type Number struct{ Value float64 }
func (n Number) Eval() float64 { return n.Value }
type Add struct{ Left, Right Expr }
func (a Add) Eval() float64 { return a.Left.Eval() + a.Right.Eval() }
type Multiply struct{ Left, Right Expr }
func (m Multiply) Eval() float64 { return m.Left.Eval() * m.Right.Eval() }
func main() {
	tree := Add{Number{2}, Multiply{Number{3}, Number{4}}}
	fmt.Println("expression,result")
	fmt.Printf("2 + 3 * 4,%.1f\n", tree.Eval())
}

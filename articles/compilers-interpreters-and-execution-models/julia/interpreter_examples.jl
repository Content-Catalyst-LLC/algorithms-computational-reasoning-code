abstract type Expr end
struct Num <: Expr; value::Float64; end
struct Add <: Expr; left::Expr; right::Expr; end
struct Mul <: Expr; left::Expr; right::Expr; end
eval_expr(e::Num) = e.value
eval_expr(e::Add) = eval_expr(e.left) + eval_expr(e.right)
eval_expr(e::Mul) = eval_expr(e.left) * eval_expr(e.right)
println("expression,result")
println("2 + 3 * 4,", eval_expr(Add(Num(2), Mul(Num(3), Num(4)))))

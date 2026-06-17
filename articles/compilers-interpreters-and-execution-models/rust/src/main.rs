enum Expr { Number(f64), Add(Box<Expr>, Box<Expr>), Multiply(Box<Expr>, Box<Expr>) }
fn evaluate(expr: &Expr) -> f64 {
    match expr {
        Expr::Number(value) => *value,
        Expr::Add(left, right) => evaluate(left) + evaluate(right),
        Expr::Multiply(left, right) => evaluate(left) * evaluate(right),
    }
}
fn main() {
    let tree = Expr::Add(Box::new(Expr::Number(2.0)), Box::new(Expr::Multiply(Box::new(Expr::Number(3.0)), Box::new(Expr::Number(4.0)))));
    println!("expression,result");
    println!("2 + 3 * 4,{:.1}", evaluate(&tree));
}

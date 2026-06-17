export type Expr =
  | { kind: "number"; value: number }
  | { kind: "add"; left: Expr; right: Expr }
  | { kind: "multiply"; left: Expr; right: Expr };

export function evaluate(expr: Expr): number {
  switch (expr.kind) {
    case "number": return expr.value;
    case "add": return evaluate(expr.left) + evaluate(expr.right);
    case "multiply": return evaluate(expr.left) * evaluate(expr.right);
  }
}

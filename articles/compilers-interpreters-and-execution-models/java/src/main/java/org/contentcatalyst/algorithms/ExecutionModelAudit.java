package org.contentcatalyst.algorithms;

public class ExecutionModelAudit {
  interface Expr { double eval(); }
  static class NumberExpr implements Expr { final double value; NumberExpr(double v){ value = v; } public double eval(){ return value; } }
  static class AddExpr implements Expr { final Expr left, right; AddExpr(Expr l, Expr r){ left = l; right = r; } public double eval(){ return left.eval() + right.eval(); } }
  static class MultiplyExpr implements Expr { final Expr left, right; MultiplyExpr(Expr l, Expr r){ left = l; right = r; } public double eval(){ return left.eval() * right.eval(); } }
  public static void main(String[] args) {
    Expr tree = new AddExpr(new NumberExpr(2), new MultiplyExpr(new NumberExpr(3), new NumberExpr(4)));
    System.out.println("expression,result");
    System.out.println("2 + 3 * 4," + tree.eval());
  }
}

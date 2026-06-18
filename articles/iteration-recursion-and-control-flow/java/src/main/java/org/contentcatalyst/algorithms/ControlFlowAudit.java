package org.contentcatalyst.algorithms;
public class ControlFlowAudit {
  static int factorial(int n){ return n <= 0 ? 1 : n * factorial(n - 1); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("factorial_5," + factorial(5));
    System.out.println("iterative_sum," + (1 + 2 + 3));
  }
}

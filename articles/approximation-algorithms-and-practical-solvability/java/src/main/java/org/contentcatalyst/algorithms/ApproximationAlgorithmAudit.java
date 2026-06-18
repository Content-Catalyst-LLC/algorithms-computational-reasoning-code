package org.contentcatalyst.algorithms;
public class ApproximationAlgorithmAudit {
  static double relativeGap(double algorithmValue, double boundValue){ return (algorithmValue - boundValue) / boundValue; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("relative_gap," + relativeGap(12.0, 10.0));
    System.out.println("approximation_ratio,1.5");
  }
}

package org.contentcatalyst.algorithms;
public class ComplexityScalabilityAudit {
  static double nlogn(double n){ return n * (Math.log(n) / Math.log(2.0)); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("linear_1000,1000");
    System.out.println("nlogn_1000," + nlogn(1000.0));
    System.out.println("quadratic_1000,1000000");
  }
}

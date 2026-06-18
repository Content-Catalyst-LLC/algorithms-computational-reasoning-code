package org.contentcatalyst.algorithms;
public class ParallelismScaleAudit {
  static double speedup(double s, double p) { return 1.0 / (s + ((1.0 - s) / p)); }
  public static void main(String[] args){
    double sp = speedup(0.10, 16.0);
    System.out.println("test_name,value");
    System.out.println("speedup_p16_s010," + sp);
    System.out.println("efficiency_p16_s010," + (sp / 16.0));
  }
}

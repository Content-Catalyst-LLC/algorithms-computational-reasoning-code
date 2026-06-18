package org.contentcatalyst.algorithms;
public class DataQualityAudit {
  static double missingnessRate(double missing,double total){ return total == 0 ? 0 : missing/total; }
  static double quality(double c,double v,double t,double p,double val){ return 100*(0.25*c+0.20*v+0.15*t+0.22*p+0.18*val); }
  public static void main(String[] args){
    double mr=missingnessRate(45,1000);
    System.out.println("test_name,value");
    System.out.println("missingness_rate_45_of_1000," + mr);
    System.out.println("completeness_score_45_of_1000," + (1-mr));
    System.out.println("data_quality_score," + quality(.92,.88,.86,.90,.89));
  }
}

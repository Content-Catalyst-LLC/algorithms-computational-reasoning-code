package org.contentcatalyst.algorithms;
public class PlatformPowerAudit {
  static double dependencyScore(double a,double v,double c,double s,double e){ return 100.0*(0.22*a+0.22*v+0.18*c+0.24*s+0.14*e); }
  static double switchingCost(double m,double r,double t,double d,double l){ return m+r+t+d+l; }
  static double ratio(double n,double d){ return d == 0 ? 0 : n/d; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("dependency_score," + dependencyScore(.80,.90,.70,.85,.65));
    System.out.println("switching_cost," + switchingCost(45000,120000,18000,24000,75000));
    System.out.println("api_dependency_ratio," + ratio(850000,1000000));
    System.out.println("visibility_share," + ratio(250000,5000000));
  }
}

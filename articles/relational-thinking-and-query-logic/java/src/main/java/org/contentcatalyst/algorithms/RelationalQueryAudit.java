package org.contentcatalyst.algorithms;
public class RelationalQueryAudit {
  static double queryScore(double e,double r,double p,double j,double k,double m){ return 100*(0.18*e+0.18*r+0.18*p+0.18*j+0.14*k+0.14*m); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("query_logic_core_score," + queryScore(.88,.86,.84,.82,.84,.80));
  }
}

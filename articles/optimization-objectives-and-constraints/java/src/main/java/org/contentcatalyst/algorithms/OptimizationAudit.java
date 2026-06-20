package org.contentcatalyst.algorithms;
public class OptimizationAudit {
  static double linearObjective(double[] c, double[] x){ double total=0; for(int i=0;i<c.length;i++) total += c[i]*x[i]; return total; }
  static double constraintMargin(double limit, double observed){ return limit - observed; }
  static double penaltyObjective(double base, double penalty, double weight){ return base + weight * penalty; }
  static double tradeoff(double cost, double quality, double risk){ return 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("linear_objective," + linearObjective(new double[]{4.0,2.0,1.5}, new double[]{10.0,20.0,5.0}));
    System.out.println("constraint_margin," + constraintMargin(100.0,86.5));
    System.out.println("penalty_objective," + penaltyObjective(42.0,8.0,2.5));
    System.out.println("normalized_tradeoff_score," + tradeoff(0.30,0.82,0.25));
  }
}

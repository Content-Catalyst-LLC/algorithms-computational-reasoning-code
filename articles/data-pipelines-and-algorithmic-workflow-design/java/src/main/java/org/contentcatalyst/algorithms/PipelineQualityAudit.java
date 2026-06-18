package org.contentcatalyst.algorithms;
public class PipelineQualityAudit {
  static double freshness(double days,double decay){ return Math.exp(-decay*days); }
  static double quality(double v,double f,double c,double l,double m){ return 100*(0.25*v+0.18*f+0.20*c+0.22*l+0.15*m); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("freshness_3_days," + freshness(3,0.025));
    System.out.println("pipeline_quality_score," + quality(.92,.86,.90,.88,.82));
  }
}

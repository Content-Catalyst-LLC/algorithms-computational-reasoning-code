package org.contentcatalyst.algorithms;
public class KnowledgeGraphAudit {
  static double hybridScore(double l,double v,double g,double p){ return 100*(0.25*l+0.25*v+0.25*g+0.25*p); }
  static double pathScore(double pathLength,double confidence,double provenance,double review){
    double lengthFactor = 1.0/(1.0+Math.max(pathLength-1.0,0.0));
    return 100*(0.25*lengthFactor+0.30*confidence+0.30*provenance+0.15*review);
  }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("hybrid_score," + hybridScore(.82,.78,.88,.90));
    System.out.println("graph_path_score," + pathScore(3,.90,.92,.95));
  }
}

package org.contentcatalyst.algorithms;
public class HeuristicDesignAudit {
  static double relativeImprovement(double baseline, double heuristic){ return (baseline - heuristic) / baseline; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("route_improvement," + relativeImprovement(34.0, 27.0));
    System.out.println("annealing_improvement," + relativeImprovement(18.5, 12.2));
  }
}

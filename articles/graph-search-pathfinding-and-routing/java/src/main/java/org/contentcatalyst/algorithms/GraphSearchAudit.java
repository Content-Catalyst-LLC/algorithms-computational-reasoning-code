package org.contentcatalyst.algorithms;
public class GraphSearchAudit {
  static double density(double nodes, double edges){ return nodes <= 1 ? 0 : edges/(nodes*(nodes-1)); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("node_count,5");
    System.out.println("edge_count,7");
    System.out.println("density," + density(5,7));
    System.out.println("manual_shortest_path_cost,5.5");
  }
}

package org.contentcatalyst.algorithms;
public class CloudInfrastructureAudit {
  static double totalLatency(double c,double s,double n,double q,double o){ return c+s+n+q+o; }
  static double nominalCapacity(double nodes,double cap){ return nodes*cap; }
  static double unitCost(double c,double s,double n,double m,double o,double completed){ return completed == 0 ? 0 : (c+s+n+m+o)/completed; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("cloud_response_latency_ms," + totalLatency(80,45,60,25,15));
    System.out.println("nominal_capacity," + nominalCapacity(12,250));
    System.out.println("unit_cost," + unitCost(120,35,25,90,18,144000));
  }
}

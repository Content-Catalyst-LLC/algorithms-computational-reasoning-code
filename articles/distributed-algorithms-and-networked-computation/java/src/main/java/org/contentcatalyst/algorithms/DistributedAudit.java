package org.contentcatalyst.algorithms;
public class DistributedAudit {
  static int quorumSize(int n){ return n/2 + 1; }
  static int crashFaultTolerance(int n){ return (n-1)/2; }
  static double availability(double replicas,double nodeAvailability){ return 1 - Math.pow(1-nodeAvailability, replicas); }
  static double latency(double compute,double network,double queue){ return compute+network+queue; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("quorum_5_nodes," + quorumSize(5));
    System.out.println("fault_tolerance_5_nodes," + crashFaultTolerance(5));
    System.out.println("availability_3_replicas," + availability(3,0.99));
    System.out.println("distributed_latency_ms," + latency(35,80,20));
  }
}

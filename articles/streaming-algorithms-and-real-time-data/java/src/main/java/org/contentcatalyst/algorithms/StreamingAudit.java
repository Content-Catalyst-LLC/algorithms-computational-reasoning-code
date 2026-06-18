package org.contentcatalyst.algorithms;
public class StreamingAudit {
  public static void main(String[] args){
    double arrival = 90.0;
    double processing = 100.0;
    System.out.println("test_name,value");
    System.out.println("utilization," + (arrival / processing));
    System.out.println("stable," + (arrival < processing));
  }
}

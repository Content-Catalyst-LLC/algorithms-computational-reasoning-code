package org.contentcatalyst.algorithms;
public class OnlineDecisionAudit {
  public static void main(String[] args){
    double threshold = 5 * 10.0 + 50.0;
    double offline = 50.0;
    System.out.println("test_name,value");
    System.out.println("threshold_strategy," + threshold);
    System.out.println("offline_optimum," + offline);
    System.out.println("ratio," + (threshold / offline));
  }
}

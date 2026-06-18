package org.contentcatalyst.algorithms;
public class PerformanceAudit {
  static double responseTime(double n,double q,double c,double s,double o){ return n+q+c+s+o; }
  static double throughput(double completed,double seconds){ return seconds == 0 ? 0 : completed/seconds; }
  static double utilization(double arrival,double service){ return service == 0 ? 0 : arrival/service; }
  static double littleLaw(double arrival,double time){ return arrival*time; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("response_time_ms," + responseTime(45,20,85,35,15));
    System.out.println("throughput," + throughput(12000,60));
    System.out.println("utilization," + utilization(180,200));
    System.out.println("little_law_items," + littleLaw(180,.45));
  }
}

package org.contentcatalyst.algorithms;
public class EdgeEmbeddedAudit {
  static double edgeResponseTime(double s,double f,double c,double a){ return s+f+c+a; }
  static double cloudResponseTime(double s,double u,double c,double d,double a){ return s+u+c+d+a; }
  static double batteryLife(double b,double p){ return p == 0 ? 0 : b/p; }
  static String localAction(double signal,double threshold){ return signal >= threshold ? "alert" : "monitor"; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("edge_response_time_ms," + edgeResponseTime(8,6,14,5));
    System.out.println("cloud_response_time_ms," + cloudResponseTime(8,90,60,90,5));
    System.out.println("battery_life_hours," + batteryLife(12,.08));
    System.out.println("local_action," + localAction(.82,.75));
  }
}

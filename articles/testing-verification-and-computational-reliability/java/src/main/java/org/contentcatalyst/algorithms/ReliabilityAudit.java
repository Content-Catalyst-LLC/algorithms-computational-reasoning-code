package org.contentcatalyst.algorithms;
public class ReliabilityAudit {
  static boolean scoreInRange(double x){ return x >= 0.0 && x <= 100.0; }
  public static void main(String[] args){
    System.out.println("test_name,status");
    System.out.println("score_72," + (scoreInRange(72) ? "pass" : "fail"));
    System.out.println("score_150," + (scoreInRange(150) ? "pass" : "fail"));
  }
}

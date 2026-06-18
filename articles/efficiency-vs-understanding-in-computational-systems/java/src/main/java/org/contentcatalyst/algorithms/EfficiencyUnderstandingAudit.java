package org.contentcatalyst.algorithms;
public class EfficiencyUnderstandingAudit {
  static double efficiencyGain(double baseline, double optimized) { return (baseline - optimized) / baseline; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("efficiency_gain_percent," + (100.0 * efficiencyGain(100.0, 64.0)));
  }
}

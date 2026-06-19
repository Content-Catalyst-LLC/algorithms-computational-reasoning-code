package org.contentcatalyst.algorithms;
public class SearchSpaceAudit {
  static long branchingStateCount(int b, int d){ long total=0, pow=1; for(int i=0;i<=d;i++){ if(i==0) pow=1; else pow*=b; total+=pow; } return total; }
  static double ratio(double n,double d){ return d == 0 ? 0 : n/d; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("branching_state_count," + branchingStateCount(3,5));
    System.out.println("path_cost," + 11.5);
    System.out.println("heuristic_score," + 13.5);
    System.out.println("coverage_ratio," + ratio(850,5000));
    System.out.println("pruning_ratio," + ratio(1200,4200));
  }
}

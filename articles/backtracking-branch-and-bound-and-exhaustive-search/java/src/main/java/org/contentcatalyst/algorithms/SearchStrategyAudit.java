package org.contentcatalyst.algorithms;
public class SearchStrategyAudit {
  static int growth(int b, int d){ int total=0, pow=1; for(int i=0;i<=d;i++){ total += pow; pow *= b; } return total; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("search_space_growth," + growth(2,3));
    System.out.println("permutation_count,6");
  }
}

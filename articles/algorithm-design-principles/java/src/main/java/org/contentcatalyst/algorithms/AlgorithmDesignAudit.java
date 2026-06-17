package org.contentcatalyst.algorithms;
public class AlgorithmDesignAudit {
  static boolean nondecreasing(int[] xs){ for(int i=0;i<xs.length-1;i++){ if(xs[i] > xs[i+1]) return false; } return true; }
  public static void main(String[] args){
    System.out.println("test_name,status");
    System.out.println("sorted_valid," + (nondecreasing(new int[]{1,2,2,3}) ? "pass" : "fail"));
    System.out.println("sorted_invalid," + (nondecreasing(new int[]{1,3,2}) ? "pass" : "fail"));
  }
}

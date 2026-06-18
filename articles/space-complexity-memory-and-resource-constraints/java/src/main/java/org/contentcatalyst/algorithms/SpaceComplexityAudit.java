package org.contentcatalyst.algorithms;
public class SpaceComplexityAudit {
  public static void main(String[] args){
    long v = 1000L;
    long e = 5000L;
    System.out.println("test_name,value");
    System.out.println("matrix_units," + (v * v));
    System.out.println("adjacency_list_units," + (v + e));
  }
}

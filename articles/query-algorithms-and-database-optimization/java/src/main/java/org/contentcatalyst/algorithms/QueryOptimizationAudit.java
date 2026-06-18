package org.contentcatalyst.algorithms;
public class QueryOptimizationAudit {
  static double selectionRows(double rows,double selectivity){ return rows * selectivity; }
  static double joinRows(double l,double r,double ld,double rd){ return (l*r)/Math.max(ld,rd); }
  public static void main(String[] args){ System.out.println("test_name,value"); System.out.println("selection_estimated_rows," + selectionRows(1000000,0.012)); System.out.println("join_estimated_rows," + joinRows(500000,200000,50000,40000)); }
}

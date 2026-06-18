package org.contentcatalyst.algorithms;
public class SearchArchitectureAudit {
  static double precision(double tp,double retrieved){ return retrieved == 0 ? 0 : tp/retrieved; }
  static double recall(double tp,double relevant){ return relevant == 0 ? 0 : tp/relevant; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("precision," + precision(2,3));
    System.out.println("recall," + recall(2,2));
  }
}

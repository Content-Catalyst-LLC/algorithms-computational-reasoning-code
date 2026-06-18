package org.contentcatalyst.algorithms;
public class DatabaseKnowledgeAudit {
  static double schemaQuality(double f,double k,double c,double m,double l){ return 100*(0.22*f+0.20*k+0.20*c+0.20*m+0.18*l); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("schema_quality_score," + schemaQuality(.90,.85,.80,.88,.82));
  }
}

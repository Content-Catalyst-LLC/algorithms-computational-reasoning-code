package org.contentcatalyst.algorithms;
public class ConcurrencyAudit {
  static double speedup(double t1,double tp){ return tp == 0 ? 0 : t1/tp; }
  static double amdahl(double p,double s){ return p == 0 ? 0 : 1.0/(s+((1.0-s)/p)); }
  static double efficiency(double p,double sp){ return p == 0 ? 0 : sp/p; }
  public static void main(String[] args){ double sp=speedup(120,28); System.out.println("test_name,value"); System.out.println("observed_speedup_120_to_28," + sp); System.out.println("amdahl_speedup_8_workers," + amdahl(8,0.12)); System.out.println("efficiency_8_workers," + efficiency(8,sp)); }
}

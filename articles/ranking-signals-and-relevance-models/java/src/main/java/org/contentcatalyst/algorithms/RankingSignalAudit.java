package org.contentcatalyst.algorithms;
public class RankingSignalAudit {
  static double precisionAtK(double tp,double k){ return k == 0 ? 0 : tp/k; }
  static double rankingScore(double l,double m,double f,double a,double s,double p){ return 100*(0.22*l+0.18*m+0.12*f+0.16*a+0.17*s+0.15*p); }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("precision_at_3," + precisionAtK(2,3));
    System.out.println("ranking_signal_score," + rankingScore(.84,.88,.76,.82,.78,.86));
  }
}

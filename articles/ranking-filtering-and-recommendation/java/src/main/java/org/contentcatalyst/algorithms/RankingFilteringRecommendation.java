package org.contentcatalyst.algorithms;
public class RankingFilteringRecommendation {
  public static double rankingScore(double textMatch, double quality, double freshness, double diversityBonus, double riskPenalty) {
    return 0.36*textMatch + 0.30*quality + 0.16*freshness + 0.14*diversityBonus - 0.20*riskPenalty;
  }
  public static void main(String[] args) { System.out.printf("%.6f%n", rankingScore(0.92, 0.88, 0.60, 0.35, 0.04)); }
}

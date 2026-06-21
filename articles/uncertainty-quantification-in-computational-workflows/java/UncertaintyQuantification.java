public class UncertaintyQuantification {
  static double clamp(double v, double lo, double hi) {
    return Math.max(lo, Math.min(hi, v));
  }
  static double riskModel(double demand, double capacity, double failureRate, double adaptationRate, double noise) {
    return clamp(0.42 + 0.38*demand - 0.31*capacity + 0.27*failureRate - 0.18*adaptationRate + noise, 0.0, 1.0);
  }
  public static void main(String[] args) {
    System.out.printf("risk_score=%.6f%n", riskModel(0.55, 0.50, 0.22, 0.30, 0.0));
  }
}

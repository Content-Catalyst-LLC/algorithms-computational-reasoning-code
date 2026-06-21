public class SensitivityAnalysis {
  static double clamp(double x) { return Math.max(0.0, Math.min(1.0, x)); }
  static double model(double demand, double capacity, double failure, double adaptation) {
    return clamp(0.5 + 0.30*demand + 0.25*failure - 0.20*capacity - 0.15*adaptation);
  }
  public static void main(String[] args) {
    System.out.printf("baseline_risk=%.6f%n", model(0.45, 0.35, 0.25, 0.30));
  }
}

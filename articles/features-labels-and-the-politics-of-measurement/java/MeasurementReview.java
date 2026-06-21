public class MeasurementReview {
  static double rate(double num, double den) { return den == 0.0 ? 0.0 : num / den; }
  public static void main(String[] args) { System.out.printf("specificity=%.4f%n", rate(88, 106)); }
}

public class NumericalApproximation {
  static double f(double x) { return Math.sin(x) + 0.25 * x * x; }
  static double centralDifference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
  public static void main(String[] args) { System.out.printf("%.12f%n", centralDifference(1.0, 0.01)); }
}

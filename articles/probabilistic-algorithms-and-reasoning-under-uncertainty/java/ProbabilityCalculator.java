public class ProbabilityCalculator {
    public static double standardError(double pHat, double n) {
        return Math.sqrt((pHat * (1.0 - pHat)) / n);
    }

    public static void main(String[] args) {
        double pHat = 0.57;
        double n = 1000.0;
        System.out.printf("p_hat=%.3f standard_error=%.6f%n", pHat, standardError(pHat, n));
    }
}

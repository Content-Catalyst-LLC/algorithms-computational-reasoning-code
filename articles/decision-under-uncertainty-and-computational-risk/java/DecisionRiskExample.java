public class DecisionRiskExample {
    static double expectedNetValue(double p, double benefit, double loss, double cost) {
        double bounded = Math.max(0.0, Math.min(1.0, p));
        return bounded * benefit - bounded * loss - cost;
    }
    public static void main(String[] args) {
        System.out.printf("%.6f%n", expectedNetValue(0.42, 150.0, 80.0, 25.0));
    }
}

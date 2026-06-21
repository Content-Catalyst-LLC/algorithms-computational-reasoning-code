public class RepresentationScore {
    static double sigmoid(double x) { return 1.0 / (1.0 + Math.exp(-x)); }
    static double representationScore(double x1, double x2, double x3, double bias) {
        return sigmoid(0.9*x1 - 0.7*x2 + 0.35*x3 + bias);
    }
    public static void main(String[] args) {
        System.out.printf("%.6f%n", representationScore(0.5, -0.2, 0.7, 0.0));
    }
}

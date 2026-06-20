public class AlgorithmicTrustDemo {
    static double trustQuality(double verification, double validation, double security, double provenance, double monitoring, double governance) {
        return 100.0 * (0.18 * verification + 0.18 * validation + 0.18 * security + 0.16 * provenance + 0.15 * monitoring + 0.15 * governance);
    }

    public static void main(String[] args) {
        System.out.printf("trust quality=%.3f%n", trustQuality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82));
    }
}

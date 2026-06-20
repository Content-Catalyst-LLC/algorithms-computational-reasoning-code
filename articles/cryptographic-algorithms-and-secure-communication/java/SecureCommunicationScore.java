public class SecureCommunicationScore {
    static double score(double threatModel, double keys, double validation, double integrity, double authentication) {
        return 100.0 * (0.22 * threatModel + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication);
    }

    public static void main(String[] args) {
        System.out.printf("standard secure channel score=%.2f%n", score(0.86, 0.82, 0.90, 0.86, 0.84));
        System.out.printf("legacy manual transfer score=%.2f%n", score(0.36, 0.24, 0.18, 0.34, 0.28));
    }
}

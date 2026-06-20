public class PrivacyPreservingDemo {
    public static void main(String[] args) {
        double[] weights = {0.42, 0.55, 0.49};
        int[] counts = {100, 240, 160};
        double weighted = 0.0;
        int total = 0;
        for (int i = 0; i < weights.length; i++) {
            weighted += weights[i] * counts[i];
            total += counts[i];
        }
        System.out.printf("federated average weight=%.6f%n", weighted / total);
    }
}

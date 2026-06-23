public class ProportionalShare {
    public static void main(String[] args) {
        double total = 1200.0;
        double[] weights = {2.0, 1.0, 1.0};
        double sum = 0.0;
        for (double w : weights) sum += w;
        for (int i = 0; i < weights.length; i++) {
            System.out.printf("share_%d=%.4f%n", i + 1, total * weights[i] / sum);
        }
    }
}

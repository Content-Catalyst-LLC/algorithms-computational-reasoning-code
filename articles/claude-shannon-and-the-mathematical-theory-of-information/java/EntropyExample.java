public class EntropyExample {
    public static double entropy(double[] probs) {
        double total = 0.0;
        for (double p : probs) {
            if (p > 0.0) total += p * (Math.log(p) / Math.log(2.0));
        }
        return -total;
    }

    public static void main(String[] args) {
        System.out.printf("entropy_bits=%.9f%n", entropy(new double[]{0.5, 0.5}));
    }
}

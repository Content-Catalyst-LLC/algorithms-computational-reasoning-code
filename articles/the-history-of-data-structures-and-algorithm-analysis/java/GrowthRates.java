public class GrowthRates {
    public static void main(String[] args) {
        double[] ns = {10, 100, 1000, 10000};
        for (double n : ns) {
            System.out.printf("n=%.0f, log2=%.6f, nlogn=%.6f, n2=%.0f%n", n, Math.log(n) / Math.log(2), n * Math.log(n) / Math.log(2), n * n);
        }
    }
}

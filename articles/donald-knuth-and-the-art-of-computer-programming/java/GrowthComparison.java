public class GrowthComparison {
    public static void main(String[] args) {
        double n = 1000.0;
        System.out.printf("log2_n=%.6f%n", Math.log(n) / Math.log(2));
        System.out.printf("n=%.0f%n", n);
        System.out.printf("n_log2_n=%.6f%n", n * (Math.log(n) / Math.log(2)));
        System.out.printf("n_squared=%.0f%n", n * n);
    }
}

public class SecurityFailures {
    public static void main(String[] args) {
        double[] weights = {0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03};
        double score = 0.0;
        for (double w : weights) {
            score += w * 0.65;
        }
        System.out.printf("%.3f%n", score * 100.0);
    }
}

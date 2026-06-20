public class IdentityAccess {
    public static void main(String[] args) {
        double[] weights = {0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02};
        double score = 0.0;
        for (double w : weights) score += 0.75 * w;
        System.out.printf("%.3f%n", score * 100.0);
    }
}

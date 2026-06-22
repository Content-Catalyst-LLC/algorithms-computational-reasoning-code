public class GoodhartRisk {
    public static void main(String[] args) {
        double proxyGap = 0.38;
        double pressure = 0.88;
        double gaming = 0.72;
        double guardrailPenalty = 1.0;
        double score = (proxyGap + pressure + gaming + guardrailPenalty) / 4.0;
        System.out.printf("goodhart_risk_score=%.4f%n", score);
    }
}

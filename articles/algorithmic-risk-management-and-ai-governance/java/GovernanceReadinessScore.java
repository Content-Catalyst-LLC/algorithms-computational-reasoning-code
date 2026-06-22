public class GovernanceReadinessScore {
    public static void main(String[] args) {
        double[] scores = {0.60, 0.62, 0.58, 0.52, 0.46, 0.50};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("governance_readiness_score=%.4f%n", total / scores.length);
    }
}

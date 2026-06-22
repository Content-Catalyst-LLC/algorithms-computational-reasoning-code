public class ExplanationQualityScore {
    public static void main(String[] args) {
        double[] scores = {0.70, 0.74, 0.62, 0.58, 0.46};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("explanation_quality_score=%.4f%n", total / scores.length);
    }
}

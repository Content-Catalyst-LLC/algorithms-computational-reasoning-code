public class DocumentationQualityScore {
    public static void main(String[] args) {
        double[] scores = {0.62, 0.6875, 0.58, 0.50, 0.56, 0.52};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("documentation_quality_score=%.4f%n", total / scores.length);
    }
}

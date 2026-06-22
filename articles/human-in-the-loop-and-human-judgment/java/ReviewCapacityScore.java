public class ReviewCapacityScore {
    public static void main(String[] args) {
        double[] scores = {0.56, 0.62, 0.58, 0.60, 0.48};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("review_capacity_score=%.4f%n", total / scores.length);
    }
}

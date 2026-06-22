public class AccountabilityCapacityScore {
    public static void main(String[] args) {
        double[] scores = {0.72, 0.68, 0.64, 0.58, 0.52, 0.66};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("accountability_capacity_score=%.4f%n", total / scores.length);
    }
}

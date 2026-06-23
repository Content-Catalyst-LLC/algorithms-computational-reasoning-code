public class OriginCareScore {
    public static void main(String[] args) {
        double[] scores = {0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98};
        double sum = 0.0;
        for (double score : scores) sum += score;
        System.out.printf("origin_care_score=%.6f%n", sum / scores.length);
    }
}

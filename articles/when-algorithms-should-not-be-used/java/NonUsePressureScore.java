public class NonUsePressureScore {
    public static void main(String[] args) {
        double[] scores = {0.94, 0.78, 0.56, 0.70};
        double total = 0.0;
        for (double score : scores) total += score;
        System.out.printf("non_use_pressure_score=%.4f%n", total / scores.length);
    }
}

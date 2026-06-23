public class TransferScore {
    public static void main(String[] args) {
        double[] scores = {0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96};
        double sum = 0.0;
        for (double score : scores) sum += score;
        System.out.printf("transfer_score=%.6f%n", sum / scores.length);
    }
}

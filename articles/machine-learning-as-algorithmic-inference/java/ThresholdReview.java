public class ThresholdReview {
    public static void main(String[] args) {
        double tp = 80.0, fp = 25.0, tn = 140.0, fn = 35.0;
        double total = tp + fp + tn + fn;
        System.out.printf("accuracy=%.6f%n", (tp + tn) / total);
        System.out.printf("precision=%.6f%n", tp / (tp + fp));
        System.out.printf("recall=%.6f%n", tp / (tp + fn));
    }
}

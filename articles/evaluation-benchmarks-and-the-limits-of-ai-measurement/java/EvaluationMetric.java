public class EvaluationMetric {
    public static void main(String[] args) {
        double tp = 42, tn = 38, fp = 7, fn = 13;
        double accuracy = (tp + tn) / (tp + tn + fp + fn);
        System.out.printf("accuracy=%.4f%n", accuracy);
    }
}

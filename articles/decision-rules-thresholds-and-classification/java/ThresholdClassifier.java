public class ThresholdClassifier {
    public static int classify(double score, double threshold) {
        return score >= threshold ? 1 : 0;
    }

    public static void main(String[] args) {
        System.out.println(classify(0.72, 0.50));
    }
}

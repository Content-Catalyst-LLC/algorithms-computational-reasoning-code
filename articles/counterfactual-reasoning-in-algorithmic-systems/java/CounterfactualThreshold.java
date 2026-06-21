public class CounterfactualThreshold {
    static String label(double score, double threshold) {
        return score >= threshold ? "favorable" : "not_favorable";
    }

    public static void main(String[] args) {
        String original = label(0.57, 0.62);
        String counterfactual = label(0.65, 0.62);
        System.out.println("original_label=" + original);
        System.out.println("counterfactual_label=" + counterfactual);
        System.out.println("decision_flipped=" + !original.equals(counterfactual));
    }
}

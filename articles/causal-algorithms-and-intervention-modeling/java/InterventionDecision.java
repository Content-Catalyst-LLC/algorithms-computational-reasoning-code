public class InterventionDecision {
    static String decision(double score, double threshold) {
        return score >= threshold ? "act" : "monitor";
    }

    public static void main(String[] args) {
        double baseline = 0.42;
        double intervention = 0.57;
        System.out.printf("estimated_effect=%.6f%n", intervention - baseline);
        System.out.println("baseline_decision=" + decision(0.53, 0.55));
        System.out.println("new_threshold_decision=" + decision(0.53, 0.50));
    }
}

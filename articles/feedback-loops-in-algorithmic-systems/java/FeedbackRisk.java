public class FeedbackRisk {
    public static void main(String[] args) {
        double amplification = 0.82;
        double concentration = 0.76;
        double intervention = 0.44;
        double drift = 0.28;
        double recursiveData = 0.31;
        double score = (amplification + concentration + intervention + drift + recursiveData) / 5.0;
        System.out.printf("feedback_risk_score=%.4f%n", score);
    }
}

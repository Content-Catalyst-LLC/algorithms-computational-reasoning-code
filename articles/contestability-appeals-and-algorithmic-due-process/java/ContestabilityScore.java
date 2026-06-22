public class ContestabilityScore {
    public static void main(String[] args) {
        double notice = 0.70;
        double reasons = 0.62;
        double evidenceAccess = 0.48;
        double humanReview = 0.55;
        double correction = 0.52;
        double remedy = 0.44;
        double score = (notice + reasons + evidenceAccess + humanReview + correction + remedy) / 6.0;
        System.out.printf("contestability_score=%.4f%n", score);
    }
}

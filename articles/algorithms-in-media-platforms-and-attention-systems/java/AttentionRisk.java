public class AttentionRisk {
    public static void main(String[] args) {
        double engagementPressure = 0.92;
        double creatorImpact = 0.88;
        double publicKnowledgeImpact = 0.78;
        double userControl = 0.44;
        double contestability = 0.42;
        double score = (engagementPressure + creatorImpact + publicKnowledgeImpact + (1.0 - userControl) + (1.0 - contestability)) / 5.0;
        System.out.printf("attention_risk_score=%.4f%n", score);
    }
}

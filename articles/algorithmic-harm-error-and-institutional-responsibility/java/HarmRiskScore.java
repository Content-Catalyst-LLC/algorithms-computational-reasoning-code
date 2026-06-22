public class HarmRiskScore {
    public static void main(String[] args) {
        double errorLikelihood = 0.34;
        double severity = 0.92;
        double exposure = 0.78;
        double contestability = 0.42;
        double harmRisk = errorLikelihood * severity * exposure * (1.0 - contestability);
        System.out.printf("harm_risk_score=%.4f%n", harmRisk);
    }
}

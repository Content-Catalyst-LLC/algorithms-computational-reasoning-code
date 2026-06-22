public class FailureRiskScore {
    public static void main(String[] args) {
        double likelihood = 0.42;
        double severity = 0.86;
        double detectability = 0.38;
        double controllability = 0.44;
        double failureRisk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability);
        System.out.printf("failure_risk_score=%.4f%n", failureRisk);
    }
}

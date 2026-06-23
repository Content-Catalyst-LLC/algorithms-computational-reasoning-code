public class InfrastructureRisk {
    public static void main(String[] args) {
        double hazard = 0.80;
        double exposure = 0.75;
        double vulnerability = 0.60;
        double risk = hazard * exposure * vulnerability;
        System.out.printf("infrastructure_risk=%.4f%n", risk);
    }
}

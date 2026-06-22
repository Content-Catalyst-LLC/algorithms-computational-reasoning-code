public class ProxyMeasurementRisk {
    public static void main(String[] args) {
        double validityGap = 0.42;
        double missingness = 0.12;
        double differentialError = 0.24;
        double labelError = 0.08;
        double score = (validityGap + missingness + differentialError + labelError) / 4.0;
        System.out.printf("measurement_risk_score=%.4f%n", score);
    }
}

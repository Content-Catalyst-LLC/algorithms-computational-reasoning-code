public class HistoricalRiskScore {
    public static void main(String[] args) {
        double provenanceRisk = 0.66;
        double measurementWeakness = 0.58;
        double proxyRisk = 0.62;
        double remediation = 0.42;
        double score = (provenanceRisk + measurementWeakness + proxyRisk + (1.0 - remediation)) / 4.0;
        System.out.printf("historical_risk_score=%.4f%n", score);
    }
}

public class DecayRisk {
    public static void main(String[] args) {
        double inputDrift = 0.31;
        double labelDrift = 0.16;
        double performanceDecay = 0.10;
        double calibrationGap = 0.14;
        double subgroupGap = 0.15;
        double overrideRate = 0.11;
        double score = (inputDrift + labelDrift + performanceDecay + calibrationGap + subgroupGap + overrideRate) / 6.0;
        System.out.printf("decay_risk_score=%.4f%n", score);
    }
}

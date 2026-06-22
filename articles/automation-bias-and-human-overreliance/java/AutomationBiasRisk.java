public class AutomationBiasRisk {
    public static void main(String[] args) {
        double acceptance = 0.93;
        double quality = 0.71;
        double uncertainty = 0.29;
        double reviewDeficit = 0.65;
        double overrideFriction = 0.72;
        double weakContestability = 0.0;
        double overrelianceGap = Math.max(0.0, acceptance - quality);
        double score = (acceptance + overrelianceGap + uncertainty + reviewDeficit + overrideFriction + weakContestability) / 6.0;
        System.out.printf("automation_bias_risk_score=%.4f%n", score);
    }
}

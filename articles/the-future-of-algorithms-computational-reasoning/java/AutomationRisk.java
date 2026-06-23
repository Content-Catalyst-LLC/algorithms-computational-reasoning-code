public class AutomationRisk {
    static double automationRisk(double stakes, double opacity, double delegation, double irreversibility) {
        return Math.max(0.0, Math.min(1.0, stakes * opacity * delegation * irreversibility));
    }

    public static void main(String[] args) {
        System.out.printf("%.6f%n", automationRisk(0.95, 0.85, 0.90, 0.80));
    }
}

public class AdversarialThinkingDemo {
    static double readiness(double threat, double surface, double monitoring, double defense, double incident, double governance) {
        return 100.0 * (0.18 * threat + 0.18 * surface + 0.18 * monitoring + 0.18 * defense + 0.14 * incident + 0.14 * governance);
    }

    public static void main(String[] args) {
        System.out.printf("adversarial readiness=%.3f%n", readiness(0.86, 0.82, 0.88, 0.82, 0.80, 0.78));
    }
}

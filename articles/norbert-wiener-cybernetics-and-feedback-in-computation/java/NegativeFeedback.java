public class NegativeFeedback {
    public static void main(String[] args) {
        double x = 10.0;
        double target = 0.0;
        double gain = 0.2;
        for (int i = 0; i < 5; i++) {
            x = x - gain * (x - target);
        }
        System.out.printf("final_state=%.6f%n", x);
    }
}

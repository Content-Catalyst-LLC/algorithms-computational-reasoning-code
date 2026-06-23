public class ThresholdAction {
    public static void main(String[] args) {
        double level = 7.5;
        double threshold = 5.0;
        boolean triggered = level >= threshold;
        System.out.printf("action_triggered=%s%n", triggered);
    }
}

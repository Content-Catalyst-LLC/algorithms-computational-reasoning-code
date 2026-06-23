public class EventTrigger {
    public static void main(String[] args) {
        double value = 12.0;
        double trigger = 10.0;
        boolean eventTriggered = value >= trigger;
        System.out.printf("event_triggered=%s%n", eventTriggered);
    }
}

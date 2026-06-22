public class ExpectedValue {
    public static void main(String[] args) {
        double probability = 0.82;
        double benefitIfAct = 0.88;
        double costIfAct = 0.30;
        double expectedValue = probability * benefitIfAct - costIfAct;
        System.out.printf("expected_value_of_action=%.4f%n", expectedValue);
    }
}

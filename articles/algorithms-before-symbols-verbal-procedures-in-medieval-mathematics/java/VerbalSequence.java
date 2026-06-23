public class VerbalSequence {
    public static void main(String[] args) {
        String[] steps = {"take the number", "double it", "add the adjustment", "check the result"};
        for (int i = 0; i < steps.length; i++) {
            System.out.printf("%d: %s%n", i + 1, steps[i]);
        }
    }
}

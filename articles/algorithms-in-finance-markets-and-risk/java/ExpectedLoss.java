public class ExpectedLoss {
    public static void main(String[] args) {
        double pd = 0.035;
        double lgd = 0.45;
        double ead = 100000.0;
        double expectedLoss = pd * lgd * ead;
        System.out.printf("expected_loss=%.4f%n", expectedLoss);
    }
}

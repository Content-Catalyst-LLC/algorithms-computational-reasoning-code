public class SquareCompletion {
    public static void main(String[] args) {
        double b = 10.0;
        double c = 39.0;
        double completion = Math.pow(b / 2.0, 2);
        System.out.printf("completion_term=%.6f%n", completion);
        System.out.printf("completed_rhs=%.6f%n", c + completion);
    }
}

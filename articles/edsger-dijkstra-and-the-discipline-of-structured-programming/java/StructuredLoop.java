public class StructuredLoop {
    static int sumTo(int n) {
        int acc = 0;
        for (int i = 0; i <= n; i++) {
            acc += i;
        }
        return acc;
    }

    public static void main(String[] args) {
        System.out.printf("sum_to_5=%d%n", sumTo(5));
    }
}

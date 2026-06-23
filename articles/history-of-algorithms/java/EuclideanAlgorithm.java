public class EuclideanAlgorithm {
    public static int gcdAlgorithm(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return Math.abs(a);
    }

    public static void main(String[] args) {
        System.out.printf("gcd=%d%n", gcdAlgorithm(252, 105));
    }
}

import java.util.function.IntUnaryOperator;

public class ChurchNumeral {
    public static int churchApply(int n, IntUnaryOperator f, int x) {
        for (int i = 0; i < n; i++) {
            x = f.applyAsInt(x);
        }
        return x;
    }

    public static void main(String[] args) {
        System.out.printf("church_3_successor_0=%d%n", churchApply(3, x -> x + 1, 0));
    }
}

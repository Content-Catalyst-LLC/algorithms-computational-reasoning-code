public class FormulaTranslation {
    static double formula(double x, double a, double b, double c) {
        return a*x*x + b*x + c;
    }

    public static void main(String[] args) {
        double[] xs = {-2, -1, 0, 1, 2, 3};
        for (double x : xs) {
            System.out.printf("x=%.1f, y=%.6f%n", x, formula(x, 2, -3, 1));
        }
    }
}

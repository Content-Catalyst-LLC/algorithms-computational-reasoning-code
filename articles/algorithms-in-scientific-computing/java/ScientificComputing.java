public class ScientificComputing {
    static double f(double x) { return Math.sin(x); }
    static double centralDifference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
    static double trapezoid(int n) {
        double a = 0.0;
        double b = Math.PI;
        double h = (b - a) / n;
        double total = 0.5 * (f(a) + f(b));
        for (int i = 1; i < n; i++) total += f(a + i * h);
        return h * total;
    }
    public static void main(String[] args) {
        System.out.printf("central_difference=%.12f%n", centralDifference(1.0, 1e-4));
        System.out.printf("trapezoid_integral=%.12f%n", trapezoid(200));
    }
}

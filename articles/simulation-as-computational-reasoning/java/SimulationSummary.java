public class SimulationSummary {
    static double step(double x) {
        return Math.max(0.0, x + 0.08 * x - 0.03 * x - 0.04 * x);
    }
    public static void main(String[] args) {
        double stock = 100.0;
        for (int t = 0; t <= 30; t++) {
            System.out.printf("time_step=%d,stock=%.6f%n", t, stock);
            stock = step(stock);
        }
    }
}

public class RouteDistance {
    public static void main(String[] args) {
        double[] segments = {12.0, 20.0, 7.5};
        double total = 0.0;
        for (double s : segments) total += s;
        System.out.printf("segments=%d%n", segments.length);
        System.out.printf("total_distance=%.6f%n", total);
    }
}

public class ModelValidationMetrics {
    public static void main(String[] args) {
        double[] observed = {33.1, 39.7, 38.8, 39.3, 8.4};
        double[] predicted = {31.92, 31.58, 36.48, 25.30, 11.30};
        double squared = 0.0;
        double absolute = 0.0;
        for (int i = 0; i < observed.length; i++) {
            double err = observed[i] - predicted[i];
            squared += err * err;
            absolute += Math.abs(err);
        }
        System.out.printf("rmse=%.4f%n", Math.sqrt(squared / observed.length));
        System.out.printf("mae=%.4f%n", absolute / observed.length);
    }
}

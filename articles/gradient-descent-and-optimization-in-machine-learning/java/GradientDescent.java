public class GradientDescent {
    static double[][] data = {{-2,-2.85},{-1,-0.67},{0,1.47},{1,3.63},{2,5.82}};

    static double mse(double w, double b) {
        double total = 0.0;
        for (double[] row : data) {
            double e = row[1] - (w * row[0] + b);
            total += e * e;
        }
        return total / data.length;
    }

    public static void main(String[] args) {
        double w = 0.0, b = 0.0, eta = 0.08;
        for (int step = 0; step < 80; step++) {
            double gradW = 0.0, gradB = 0.0;
            for (double[] row : data) {
                double err = (w * row[0] + b) - row[1];
                gradW += (2.0 / data.length) * err * row[0];
                gradB += (2.0 / data.length) * err;
            }
            w -= eta * gradW;
            b -= eta * gradB;
        }
        System.out.printf("weight=%.6f bias=%.6f loss=%.6f%n", w, b, mse(w, b));
    }
}

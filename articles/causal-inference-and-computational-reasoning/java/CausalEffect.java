public class CausalEffect {
    static double effect(double treatedMean, double controlMean) {
        return treatedMean - controlMean;
    }

    public static void main(String[] args) {
        System.out.printf("causal contrast = %.4f%n", effect(0.64, 0.47));
    }
}

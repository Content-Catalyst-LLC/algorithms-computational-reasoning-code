public class FairnessGapScore {
    public static void main(String[] args) {
        double[] rates = {0.42, 0.31, 0.36};
        double minRate = rates[0];
        double maxRate = rates[0];
        for (double value : rates) {
            if (value < minRate) minRate = value;
            if (value > maxRate) maxRate = value;
        }
        System.out.printf("selection_gap=%.4f%n", maxRate - minRate);
    }
}

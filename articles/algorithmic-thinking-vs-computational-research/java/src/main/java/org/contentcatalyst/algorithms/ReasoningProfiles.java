package org.contentcatalyst.algorithms;

public class ReasoningProfiles {
    public static void main(String[] args) {
        String[] names = {
            "Recipe-like procedure",
            "Classroom algorithm exercise",
            "Search and ranking system",
            "Public decision-support workflow",
            "Scientific modeling workflow"
        };
        double[] step = {86, 90, 72, 68, 74};
        double[] decomp = {72, 82, 70, 66, 78};
        double[] control = {70, 84, 76, 64, 76};
        double[] test = {62, 78, 66, 72, 82};
        double[] representation = {42, 62, 78, 80, 86};
        double[] governance = {20, 32, 70, 86, 74};

        System.out.println("name,algorithmic_score,computational_score,warning");
        for (int i = 0; i < names.length; i++) {
            double algorithmic = 0.28 * step[i] + 0.24 * decomp[i] + 0.24 * control[i] + 0.24 * test[i];
            double computational = 0.16 * step[i] + 0.14 * decomp[i] + 0.14 * control[i] + 0.14 * test[i] + 0.22 * representation[i] + 0.20 * governance[i];
            System.out.printf("%s,%.3f,%.3f,Synthetic educational diagnostic only.%n", names[i], algorithmic, computational);
        }
    }
}

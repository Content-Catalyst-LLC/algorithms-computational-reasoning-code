package org.contentcatalyst.algorithms;

public class DecompositionAudit {
    public static void main(String[] args) {
        String[] names = {"Search system", "Public decision-support workflow", "Scientific simulation", "Knowledge architecture"};
        double[] subproblem = {82, 74, 86, 80};
        double[] boundary = {78, 66, 82, 76};
        double[] sequencing = {82, 68, 80, 74};
        double[] dependencies = {72, 60, 78, 70};
        double[] recomposition = {72, 58, 82, 80};

        System.out.println("case_name,decomposition_score,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * subproblem[i] + 0.20 * boundary[i] + 0.18 * sequencing[i] + 0.20 * dependencies[i] + 0.20 * recomposition[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

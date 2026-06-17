package org.contentcatalyst.algorithms;

public class PseudocodeTranslationAudit {
    public static void main(String[] args) {
        String[] names = {"Search ranking prototype", "Decision-rule implementation", "Simulation loop", "Data-cleaning procedure"};
        double[] intent = {82, 76, 84, 78};
        double[] control = {80, 74, 82, 76};
        double[] edge = {64, 66, 72, 70};
        double[] tests = {68, 62, 70, 66};
        double[] maintain = {72, 68, 74, 72};

        System.out.println("case_name,translation_quality,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * intent[i] + 0.22 * control[i] + 0.18 * edge[i] + 0.18 * tests[i] + 0.20 * maintain[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

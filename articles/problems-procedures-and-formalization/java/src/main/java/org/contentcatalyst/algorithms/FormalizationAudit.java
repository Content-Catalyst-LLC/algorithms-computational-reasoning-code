package org.contentcatalyst.algorithms;

public class FormalizationAudit {
    public static void main(String[] args) {
        String[] names = {"Document search", "Worker scheduling", "Public service triage", "Scientific simulation"};
        double[] input = {82, 72, 60, 86};
        double[] output = {78, 76, 72, 80};
        double[] objective = {70, 58, 52, 76};
        double[] assumptions = {58, 54, 46, 84};
        double[] governance = {56, 62, 66, 70};

        System.out.println("case_name,formalization_score,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.20 * input[i] + 0.20 * output[i] + 0.25 * objective[i] + 0.20 * assumptions[i] + 0.15 * governance[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

package org.contentcatalyst.algorithms;

public class AlgorithmicLiteracyAudit {
    public static void main(String[] args) {
        String[] names = {"Search ranking", "Public decision-support workflow", "Scientific simulation dashboard", "Recommendation feed"};
        double[] transparency = {62, 58, 76, 40};
        double[] interpretability = {66, 56, 74, 48};
        double[] contestability = {38, 70, 60, 32};
        double[] governance = {52, 76, 68, 46};
        double[] judgment = {68, 74, 80, 50};

        System.out.println("case_name,literacy_support_score,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * transparency[i] + 0.22 * interpretability[i] + 0.18 * contestability[i] + 0.18 * governance[i] + 0.20 * judgment[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

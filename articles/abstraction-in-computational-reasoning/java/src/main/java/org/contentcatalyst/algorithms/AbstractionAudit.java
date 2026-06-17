package org.contentcatalyst.algorithms;

public class AbstractionAudit {
    public static void main(String[] args) {
        String[] names = {"Search ranking", "Transit model", "Database schema", "Decision-support score"};
        double[] clarity = {82, 78, 84, 70};
        double[] scope = {70, 72, 78, 60};
        double[] detail = {62, 66, 70, 48};
        double[] interpretation = {60, 72, 74, 52};
        double[] governance = {56, 66, 70, 66};

        System.out.println("case_name,abstraction_score,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * clarity[i] + 0.20 * scope[i] + 0.20 * detail[i] + 0.23 * interpretation[i] + 0.15 * governance[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

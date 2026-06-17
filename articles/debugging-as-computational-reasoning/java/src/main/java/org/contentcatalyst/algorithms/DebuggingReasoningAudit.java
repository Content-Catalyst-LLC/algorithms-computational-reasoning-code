package org.contentcatalyst.algorithms;

public class DebuggingReasoningAudit {
    public static void main(String[] args) {
        String[] names = {"Graph traversal infinite loop", "Data pipeline missing-value bug", "Simulation instability", "Recommendation ranking tie bug"};
        double[] reproduce = {88, 84, 80, 76};
        double[] trace = {78, 74, 78, 68};
        double[] isolate = {80, 72, 70, 70};
        double[] verify = {82, 76, 74, 72};
        double[] regression = {78, 74, 66, 70};

        System.out.println("case_name,debugging_quality,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * reproduce[i] + 0.20 * trace[i] + 0.18 * isolate[i] + 0.22 * verify[i] + 0.18 * regression[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

package org.contentcatalyst.algorithms;

public class BoundaryStateAudit {
    public static void main(String[] args) {
        String[] names = {"Graph traversal", "Decision-support workflow", "Numerical simulation", "Recommendation ranking"};
        double[] input = {84, 68, 82, 74};
        double[] output = {80, 70, 78, 72};
        double[] state = {86, 74, 84, 70};
        double[] stopping = {80, 62, 78, 60};
        double[] failure = {70, 60, 66, 52};

        System.out.println("case_name,boundary_score,warning");
        for (int i = 0; i < names.length; i++) {
            double score = 0.22 * input[i] + 0.22 * output[i] + 0.22 * state[i] + 0.20 * stopping[i] + 0.14 * failure[i];
            System.out.printf("%s,%.3f,Synthetic educational diagnostic only.%n", names[i], score);
        }
    }
}

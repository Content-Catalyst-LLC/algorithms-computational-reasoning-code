public class ProceduralReadiness {
    public static void main(String[] args) {
        double dueProcess = 0.58;
        double transparency = 0.52;
        double humanReview = 0.60;
        double appealReadiness = 0.54;
        double score = (dueProcess + transparency + humanReview + appealReadiness) / 4.0;
        System.out.printf("procedural_readiness_score=%.4f%n", score);
    }
}

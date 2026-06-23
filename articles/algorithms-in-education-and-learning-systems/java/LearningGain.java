public class LearningGain {
    public static void main(String[] args) {
        double pretest = 0.52;
        double posttest = 0.78;
        double gain = posttest - pretest;
        System.out.printf("learning_gain=%.4f%n", gain);
    }
}

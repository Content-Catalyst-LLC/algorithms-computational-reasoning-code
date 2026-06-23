public class Sensitivity {
    public static void main(String[] args) {
        double tp = 86.0;
        double fn = 14.0;
        double sensitivity = tp / (tp + fn);
        System.out.printf("sensitivity=%.4f%n", sensitivity);
    }
}

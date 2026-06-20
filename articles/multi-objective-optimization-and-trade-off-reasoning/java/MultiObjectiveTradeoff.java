public class MultiObjectiveTradeoff {
  public static void main(String[] args) {
    String[] names = {"A", "B", "C", "D"};
    double[] scores = {0.52, 0.49, 0.82, 0.35};
    for (int i = 0; i < names.length; i++) System.out.printf("%s %.2f%n", names[i], scores[i]);
  }
}

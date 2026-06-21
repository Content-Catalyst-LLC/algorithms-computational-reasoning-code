public class LLMStatus {
  static String classify(double score, String stakes) {
    if (stakes.equals("high") && score < 1.0) return "escalate";
    if (score >= 0.8) return "pass";
    return "review";
  }
  public static void main(String[] args) { System.out.println(classify(0.67, "medium")); }
}

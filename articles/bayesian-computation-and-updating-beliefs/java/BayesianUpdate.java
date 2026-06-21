public class BayesianUpdate { public static void main(String[] args) { double postAlpha=2.0+113.0, postBeta=2.0+72.0; System.out.printf("posterior_mean=%.6f%n", postAlpha/(postAlpha+postBeta)); } }

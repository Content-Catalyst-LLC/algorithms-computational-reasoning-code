public class ThresholdUnit {
    static int thresholdUnit(int[] inputs, int[] weights, int threshold) {
        int total = 0;
        for (int i = 0; i < inputs.length; i++) total += inputs[i] * weights[i];
        return total >= threshold ? 1 : 0;
    }

    public static void main(String[] args) {
        System.out.println(thresholdUnit(new int[]{1, 1}, new int[]{1, 1}, 2));
    }
}

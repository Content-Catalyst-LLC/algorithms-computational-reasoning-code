public class PlaceValue {
    public static void main(String[] args) {
        int[] digits = {1, 2, 3, 0};
        int value = 0;
        for (int digit : digits) value = value * 10 + digit;
        System.out.printf("place_value=%d%n", value);
    }
}

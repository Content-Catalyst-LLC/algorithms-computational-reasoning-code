public class PlaceValue {
    public static void main(String[] args) {
        int digit = 7;
        int base = 10;
        int position = 3;
        int value = digit * (int)Math.pow(base, position);
        System.out.printf("place_value=%d%n", value);
    }
}

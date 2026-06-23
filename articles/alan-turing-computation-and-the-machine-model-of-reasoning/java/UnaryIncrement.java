public class UnaryIncrement {
    public static String unaryIncrement(String input) {
        StringBuilder tape = new StringBuilder(input);
        int i = 0;
        while (i < tape.length() && tape.charAt(i) == '1') {
            i++;
        }
        if (i == tape.length()) {
            tape.append('_');
        }
        tape.setCharAt(i, '1');
        if (i + 1 == tape.length()) {
            tape.append('_');
        }
        return tape.toString();
    }

    public static void main(String[] args) {
        System.out.println("incremented_tape=" + unaryIncrement("111_"));
    }
}

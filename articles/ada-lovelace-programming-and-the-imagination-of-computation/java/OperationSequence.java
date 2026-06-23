public class OperationSequence {
    public static void main(String[] args) {
        String[] operations = {"initialize", "store", "multiply", "subtract", "repeat", "output"};
        System.out.printf("operation_count=%d%n", operations.length);
        System.out.println("sequence=" + String.join(" -> ", operations));
    }
}

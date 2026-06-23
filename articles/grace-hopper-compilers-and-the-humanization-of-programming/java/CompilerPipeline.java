import java.util.Arrays;

public class CompilerPipeline {
    public static void main(String[] args) {
        String source = "ADD PAYROLL-TOTAL TO TAX-BASE";
        String[] tokens = source.split("\\s+");
        System.out.println("source=" + source);
        System.out.println("tokens=" + Arrays.toString(tokens));
        System.out.println("target_code=machine-specific instruction sequence");
    }
}

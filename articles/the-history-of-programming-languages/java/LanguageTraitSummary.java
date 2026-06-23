import java.util.LinkedHashMap;
import java.util.Map;

public class LanguageTraitSummary {
    public static void main(String[] args) {
        Map<String, String> languages = new LinkedHashMap<>();
        languages.put("Fortran", "scientific numerical programming");
        languages.put("Lisp", "symbolic computation");
        languages.put("SQL", "declarative data querying");
        languages.put("Rust", "memory-safe systems programming");
        for (Map.Entry<String, String> entry : languages.entrySet()) {
            System.out.printf("%s: %s%n", entry.getKey(), entry.getValue());
        }
    }
}

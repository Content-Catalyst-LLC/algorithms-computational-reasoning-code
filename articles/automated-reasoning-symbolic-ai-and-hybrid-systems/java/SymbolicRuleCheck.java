import java.util.Set;

public class SymbolicRuleCheck {
    public static void main(String[] args) {
        Set<String> facts = Set.of("has_documentation", "logs_decisions");
        boolean fires = facts.contains("has_documentation") && facts.contains("logs_decisions");
        System.out.println("rule_fires=" + fires);
    }
}

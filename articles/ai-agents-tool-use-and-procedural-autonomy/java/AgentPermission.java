public class AgentPermission {
    public static void main(String[] args) {
        double risk = 0.85;
        boolean approvalRequired = true;
        boolean approved = false;
        String status = "pass";
        if (approvalRequired && !approved) {
            status = "blocked";
        } else if (risk >= 0.65) {
            status = "escalate";
        }
        System.out.println("agent_action_status=" + status);
    }
}

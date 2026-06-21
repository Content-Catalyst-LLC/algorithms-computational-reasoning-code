fn main() {
    let risk = 0.85;
    let approval_required = true;
    let approved = false;
    let status = if approval_required && !approved {
        "blocked"
    } else if risk >= 0.65 {
        "escalate"
    } else {
        "pass"
    };
    println!("agent_action_status={}", status);
}

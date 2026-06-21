const risk = 0.85;
const approvalRequired = true;
const approved = false;
const status = approvalRequired && !approved ? "blocked" : risk >= 0.65 ? "escalate" : "pass";
console.log(`agent_action_status=${status}`);

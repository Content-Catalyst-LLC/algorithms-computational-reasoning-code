#include <iostream>
#include <string>

int main() {
    double risk = 0.85;
    bool approval_required = true;
    bool approved = false;
    std::string status = "pass";
    if (approval_required && !approved) status = "blocked";
    else if (risk >= 0.65) status = "escalate";
    std::cout << "agent_action_status=" << status << "\n";
    return 0;
}

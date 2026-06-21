#include <stdio.h>

int main(void) {
    double risk = 0.85;
    int approval_required = 1;
    int approved = 0;
    const char *status = "pass";
    if (approval_required && !approved) {
        status = "blocked";
    } else if (risk >= 0.65) {
        status = "escalate";
    }
    printf("agent_action_status=%s\n", status);
    return 0;
}

#include <stdio.h>
#include <string.h>

int contains(const char *facts[], int n, const char *target) {
    for (int i = 0; i < n; i++) {
        if (strcmp(facts[i], target) == 0) return 1;
    }
    return 0;
}

int main(void) {
    const char *facts[] = {"has_documentation", "logs_decisions"};
    const char *premises[] = {"has_documentation", "logs_decisions"};
    int fires = 1;
    for (int i = 0; i < 2; i++) {
        if (!contains(facts, 2, premises[i])) fires = 0;
    }
    printf("rule_fires=%d\n", fires);
    return 0;
}

#include <stdio.h>

int main(void) {
    const char *operations[] = {"initialize", "store", "multiply", "subtract", "repeat", "output"};
    int n = sizeof(operations) / sizeof(operations[0]);
    printf("operation_count=%d\n", n);
    for (int i = 0; i < n; i++) {
        printf("%s%s", operations[i], i == n - 1 ? "\n" : " -> ");
    }
    return 0;
}

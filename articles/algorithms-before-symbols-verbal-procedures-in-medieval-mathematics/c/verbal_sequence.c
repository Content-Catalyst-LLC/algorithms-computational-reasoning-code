#include <stdio.h>

int main(void) {
    const char *steps[] = {"take the number", "double it", "add the adjustment", "check the result"};
    for (int i = 0; i < 4; i++) {
        printf("%d: %s\n", i + 1, steps[i]);
    }
    return 0;
}

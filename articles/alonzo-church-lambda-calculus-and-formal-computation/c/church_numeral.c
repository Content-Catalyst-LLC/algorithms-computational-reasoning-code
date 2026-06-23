#include <stdio.h>

int succ(int x) { return x + 1; }

int church_apply(int n, int (*f)(int), int x) {
    for (int i = 0; i < n; i++) {
        x = f(x);
    }
    return x;
}

int main(void) {
    printf("church_3_successor_0=%d\n", church_apply(3, succ, 0));
    return 0;
}

#include <stdio.h>

unsigned long factorial(unsigned int n) {
    return n == 0 ? 1 : n * factorial(n - 1);
}

int main(void) {
    for (unsigned int i = 0; i <= 6; i++) {
        printf("%u %lu\n", i, factorial(i));
    }
    return 0;
}

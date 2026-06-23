#include <stdio.h>
#include <stdlib.h>

int gcd_algorithm(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return abs(a);
}

int main(void) {
    printf("gcd=%d\n", gcd_algorithm(252, 105));
    return 0;
}

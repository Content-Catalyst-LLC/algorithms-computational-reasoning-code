#include <stdio.h>

int ipow(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main(void) {
    int digit = 7;
    int base = 10;
    int position = 3;
    int value = digit * ipow(base, position);
    printf("place_value=%d\n", value);
    return 0;
}

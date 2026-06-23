#include <stdio.h>

int main(void) {
    int digits[] = {1, 2, 3, 0};
    int n = sizeof(digits) / sizeof(digits[0]);
    int value = 0;
    for (int i = 0; i < n; i++) value = value * 10 + digits[i];
    printf("place_value=%d\n", value);
    return 0;
}

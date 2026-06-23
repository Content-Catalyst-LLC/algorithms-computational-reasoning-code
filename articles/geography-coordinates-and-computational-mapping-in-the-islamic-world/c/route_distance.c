#include <stdio.h>

int main(void) {
    double segments[] = {12.0, 20.0, 7.5};
    double total = 0.0;
    for (int i = 0; i < 3; i++) total += segments[i];
    printf("segments=%d\n", 3);
    printf("total_distance=%.6f\n", total);
    return 0;
}

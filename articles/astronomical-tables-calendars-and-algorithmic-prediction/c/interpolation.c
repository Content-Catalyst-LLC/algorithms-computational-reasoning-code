#include <stdio.h>

int main(void) {
    double x0 = 10.0, y0 = 1.2;
    double x1 = 20.0, y1 = 2.8;
    double x = 15.0;
    double y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
    printf("interpolated_y=%.6f\n", y);
    return 0;
}

#include <stdio.h>

double step(double x) {
    double v = x + 0.08 * x - 0.03 * x - 0.04 * x;
    return v < 0.0 ? 0.0 : v;
}

int main(void) {
    double stock = 100.0;
    for (int t = 0; t <= 30; ++t) {
        printf("time_step=%d,stock=%.6f\n", t, stock);
        stock = step(stock);
    }
    return 0;
}

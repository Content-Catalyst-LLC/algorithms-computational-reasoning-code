#include <stdio.h>

double expected_net_value(double p, double benefit, double loss, double cost) {
    if (p < 0.0) p = 0.0;
    if (p > 1.0) p = 1.0;
    return p * benefit - p * loss - cost;
}

int main(void) {
    printf("%.6f
", expected_net_value(0.42, 150.0, 80.0, 25.0));
    return 0;
}

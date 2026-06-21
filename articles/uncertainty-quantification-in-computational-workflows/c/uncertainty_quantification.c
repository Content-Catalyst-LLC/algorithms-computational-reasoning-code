#include <stdio.h>

double clamp(double v, double lo, double hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}

double risk_model(double demand, double capacity, double failure_rate, double adaptation_rate, double noise) {
    return clamp(0.42 + 0.38*demand - 0.31*capacity + 0.27*failure_rate - 0.18*adaptation_rate + noise, 0.0, 1.0);
}

int main(void) {
    printf("risk_score=%.6f\n", risk_model(0.55, 0.50, 0.22, 0.30, 0.0));
    return 0;
}

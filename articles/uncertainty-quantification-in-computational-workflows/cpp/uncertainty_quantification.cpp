#include <algorithm>
#include <iostream>

static double risk_model(double demand, double capacity, double failure_rate, double adaptation_rate, double noise) {
    return std::clamp(0.42 + 0.38*demand - 0.31*capacity + 0.27*failure_rate - 0.18*adaptation_rate + noise, 0.0, 1.0);
}

int main() {
    std::cout << "risk_score=" << risk_model(0.55, 0.50, 0.22, 0.30, 0.0) << "\n";
    return 0;
}

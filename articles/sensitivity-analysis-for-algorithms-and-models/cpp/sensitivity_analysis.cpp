#include <algorithm>
#include <iostream>

double model(double demand, double capacity, double failure, double adaptation) {
    return std::clamp(0.5 + 0.30*demand + 0.25*failure - 0.20*capacity - 0.15*adaptation, 0.0, 1.0);
}
int main() {
    std::cout << "baseline_risk=" << model(0.45, 0.35, 0.25, 0.30) << "\n";
}

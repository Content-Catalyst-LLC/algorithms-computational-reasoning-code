#include <iostream>

int main() {
    double hazard = 0.80;
    double exposure = 0.75;
    double vulnerability = 0.60;
    double risk = hazard * exposure * vulnerability;
    std::cout << "infrastructure_risk=" << risk << "\n";
    return 0;
}

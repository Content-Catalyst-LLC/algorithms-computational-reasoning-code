#include <iostream>

int main() {
    double likelihood = 0.42;
    double severity = 0.86;
    double detectability = 0.38;
    double controllability = 0.44;
    double failure_risk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability);
    std::cout << "failure_risk_score=" << failure_risk << "\n";
    return 0;
}

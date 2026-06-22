#include <iostream>

int main() {
    double error_likelihood = 0.34;
    double severity = 0.92;
    double exposure = 0.78;
    double contestability = 0.42;
    double harm_risk = error_likelihood * severity * exposure * (1.0 - contestability);
    std::cout << "harm_risk_score=" << harm_risk << "\n";
    return 0;
}

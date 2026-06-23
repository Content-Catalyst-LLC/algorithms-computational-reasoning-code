#include <algorithm>
#include <iostream>

double automation_risk(double stakes, double opacity, double delegation, double irreversibility) {
    return std::clamp(stakes * opacity * delegation * irreversibility, 0.0, 1.0);
}

int main() {
    std::cout << automation_risk(0.95, 0.85, 0.90, 0.80) << "\n";
}

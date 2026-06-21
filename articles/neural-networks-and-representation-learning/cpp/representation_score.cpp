#include <cmath>
#include <iomanip>
#include <iostream>

double sigmoid(double x) { return 1.0 / (1.0 + std::exp(-x)); }
double representation_score(double x1, double x2, double x3, double bias) {
    return sigmoid(0.9*x1 - 0.7*x2 + 0.35*x3 + bias);
}
int main() {
    std::cout << std::fixed << std::setprecision(6) << representation_score(0.5, -0.2, 0.7, 0.0) << "
";
}

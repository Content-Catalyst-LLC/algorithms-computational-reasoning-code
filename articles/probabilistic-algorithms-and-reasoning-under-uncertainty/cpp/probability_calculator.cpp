#include <cmath>
#include <iostream>

double standard_error(double p_hat, double n) {
    return std::sqrt((p_hat * (1.0 - p_hat)) / n);
}

int main() {
    double p_hat = 0.57;
    double n = 1000.0;
    std::cout << "p_hat=" << p_hat << " standard_error=" << standard_error(p_hat, n) << "\n";
    return 0;
}

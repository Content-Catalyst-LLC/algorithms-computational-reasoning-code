#include <cmath>
#include <iostream>

double f(double x) { return std::sin(x); }
double central_difference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
double trapezoid(int n) {
    const double a = 0.0, b = std::acos(-1.0), h = (b - a) / n;
    double total = 0.5 * (f(a) + f(b));
    for (int i = 1; i < n; ++i) total += f(a + i * h);
    return h * total;
}
int main() {
    std::cout << "central_difference=" << central_difference(1.0, 1e-4) << "\n";
    std::cout << "trapezoid_integral=" << trapezoid(200) << "\n";
}

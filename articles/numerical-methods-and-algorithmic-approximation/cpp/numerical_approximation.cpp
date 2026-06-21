#include <cmath>
#include <iomanip>
#include <iostream>

double f(double x) { return std::sin(x) + 0.25 * x * x; }
double central_difference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
int main() { std::cout << std::setprecision(12) << central_difference(1.0, 0.01) << "\n"; }

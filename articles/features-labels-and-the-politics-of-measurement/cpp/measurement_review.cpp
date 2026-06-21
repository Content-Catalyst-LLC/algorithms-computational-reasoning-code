#include <iostream>
#include <iomanip>
double rate(double num, double den) { return den == 0.0 ? 0.0 : num / den; }
int main() { std::cout << std::fixed << std::setprecision(4) << "sensitivity=" << rate(72, 94) << "\n"; }

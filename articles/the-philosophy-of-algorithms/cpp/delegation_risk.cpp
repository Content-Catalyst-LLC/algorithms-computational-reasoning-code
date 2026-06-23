#include <algorithm>
#include <iostream>

double delegation_risk(double a, double b, double c) { return std::clamp(a*b*c, 0.0, 1.0); }
int main() { std::cout << delegation_risk(0.95, 0.95, 0.80) << "\n"; }

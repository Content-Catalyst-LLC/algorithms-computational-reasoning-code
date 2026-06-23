#include <iostream>
#include <vector>

double formula(double x, double a, double b, double c) {
    return a*x*x + b*x + c;
}

int main() {
    for (double x : std::vector<double>{-2, -1, 0, 1, 2, 3}) {
        std::cout << "x=" << x << ", y=" << formula(x, 2, -3, 1) << "\n";
    }
}

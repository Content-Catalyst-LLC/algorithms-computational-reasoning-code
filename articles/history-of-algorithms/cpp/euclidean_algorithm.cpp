#include <iostream>
#include <cstdlib>

int gcd_algorithm(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return std::abs(a);
}

int main() {
    std::cout << "gcd=" << gcd_algorithm(252, 105) << "\n";
    return 0;
}

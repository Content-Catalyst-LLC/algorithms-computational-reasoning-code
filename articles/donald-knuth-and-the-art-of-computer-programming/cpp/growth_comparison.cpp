#include <cmath>
#include <iostream>

int main() {
    double n = 1000.0;
    std::cout << "log2_n=" << std::log2(n) << "\n";
    std::cout << "n=" << n << "\n";
    std::cout << "n_log2_n=" << n * std::log2(n) << "\n";
    std::cout << "n_squared=" << n * n << "\n";
}

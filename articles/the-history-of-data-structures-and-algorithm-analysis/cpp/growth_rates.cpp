#include <cmath>
#include <iostream>
#include <vector>

int main() {
    for (double n : std::vector<double>{10, 100, 1000, 10000}) {
        std::cout << "n=" << n << ", log2=" << std::log2(n) << ", nlogn=" << n * std::log2(n) << ", n2=" << n*n << "\n";
    }
}

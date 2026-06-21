#include <algorithm>
#include <iostream>

int main() {
    double stock = 100.0;
    for (int t = 0; t <= 30; ++t) {
        std::cout << "time_step=" << t << ",stock=" << stock << "\n";
        stock = std::max(0.0, stock + 0.08 * stock - 0.03 * stock - 0.04 * stock);
    }
    return 0;
}

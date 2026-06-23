#include <iostream>

int main() {
    double tp = 86.0;
    double fn = 14.0;
    double sensitivity = tp / (tp + fn);
    std::cout << "sensitivity=" << sensitivity << "\n";
    return 0;
}

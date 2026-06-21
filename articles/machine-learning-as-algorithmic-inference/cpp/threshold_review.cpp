#include <iostream>
#include <iomanip>

int main() {
    double tp = 80.0, fp = 25.0, tn = 140.0, fn = 35.0;
    double total = tp + fp + tn + fn;
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "accuracy=" << (tp + tn) / total << "\n";
    std::cout << "precision=" << tp / (tp + fp) << "\n";
    std::cout << "recall=" << tp / (tp + fn) << "\n";
    return 0;
}

#include <iostream>
#include <iomanip>

double trust_quality(double verification, double validation, double security, double provenance, double monitoring, double governance) {
    return 100.0 * (0.18*verification + 0.18*validation + 0.18*security + 0.16*provenance + 0.15*monitoring + 0.15*governance);
}

int main() {
    std::cout << "trust quality=" << std::fixed << std::setprecision(3)
              << trust_quality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82) << "\n";
}

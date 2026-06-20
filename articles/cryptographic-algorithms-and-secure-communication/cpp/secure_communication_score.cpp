#include <iostream>
#include <iomanip>

int main() {
    auto score = [](double threat_model, double keys, double validation, double integrity, double authentication) {
        return 100.0 * (0.22 * threat_model + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication);
    };
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "standard secure channel score=" << score(0.86, 0.82, 0.90, 0.86, 0.84) << "\n";
    std::cout << "legacy manual transfer score=" << score(0.36, 0.24, 0.18, 0.34, 0.28) << "\n";
    return 0;
}

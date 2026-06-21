#include <iostream>
#include <iomanip>
#include <string>

std::string decision(double score, double threshold) {
    return score >= threshold ? "act" : "monitor";
}

int main() {
    double baseline = 0.42;
    double intervention = 0.57;
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "estimated_effect=" << intervention - baseline << "
";
    std::cout << "baseline_decision=" << decision(0.53, 0.55) << "
";
    std::cout << "new_threshold_decision=" << decision(0.53, 0.50) << "
";
}

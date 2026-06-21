#include <iostream>
#include <string>

std::string label(double score, double threshold) {
    return score >= threshold ? "favorable" : "not_favorable";
}

int main() {
    const double original = 0.57;
    const double counterfactual = 0.65;
    const double threshold = 0.62;
    std::cout << "original_label=" << label(original, threshold) << "\n";
    std::cout << "counterfactual_label=" << label(counterfactual, threshold) << "\n";
    std::cout << "decision_flipped=" << (label(original, threshold) != label(counterfactual, threshold)) << "\n";
    return 0;
}

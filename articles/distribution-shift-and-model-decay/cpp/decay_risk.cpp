#include <iostream>

int main() {
    double input_drift = 0.31;
    double label_drift = 0.16;
    double performance_decay = 0.10;
    double calibration_gap = 0.14;
    double subgroup_gap = 0.15;
    double override_rate = 0.11;
    double score = (input_drift + label_drift + performance_decay + calibration_gap + subgroup_gap + override_rate) / 6.0;
    std::cout << "decay_risk_score=" << score << "\n";
    return 0;
}

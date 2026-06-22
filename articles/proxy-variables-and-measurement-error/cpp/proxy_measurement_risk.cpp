#include <iostream>

int main() {
    double validity_gap = 0.42;
    double missingness = 0.12;
    double differential_error = 0.24;
    double label_error = 0.08;
    double score = (validity_gap + missingness + differential_error + label_error) / 4.0;
    std::cout << "measurement_risk_score=" << score << "\n";
    return 0;
}

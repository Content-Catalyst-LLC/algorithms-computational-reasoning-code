#include <algorithm>
#include <iostream>

int main() {
    double acceptance = 0.93;
    double quality = 0.71;
    double uncertainty = 0.29;
    double review_deficit = 0.65;
    double override_friction = 0.72;
    double weak_contestability = 0.0;
    double overreliance_gap = std::max(0.0, acceptance - quality);
    double score = (acceptance + overreliance_gap + uncertainty + review_deficit + override_friction + weak_contestability) / 6.0;
    std::cout << "automation_bias_risk_score=" << score << "\n";
    return 0;
}

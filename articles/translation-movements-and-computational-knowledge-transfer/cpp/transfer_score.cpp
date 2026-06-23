#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores{0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96};
    double sum = 0.0;
    for (double score : scores) sum += score;
    std::cout << "transfer_score=" << sum / scores.size() << "\n";
    return 0;
}

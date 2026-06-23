#include <iostream>

int main() {
    double pd = 0.035;
    double lgd = 0.45;
    double ead = 100000.0;
    double expected_loss = pd * lgd * ead;
    std::cout << "expected_loss=" << expected_loss << "\n";
    return 0;
}

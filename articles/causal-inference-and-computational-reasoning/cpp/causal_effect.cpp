#include <iostream>

struct Contrast {
    double treated_mean;
    double control_mean;
    double effect() const { return treated_mean - control_mean; }
};

int main() {
    Contrast contrast{0.64, 0.47};
    std::cout << "causal contrast = " << contrast.effect() << "\n";
    return 0;
}

#include <iostream>

int main() {
    double x = 10.0;
    double target = 0.0;
    double gain = 0.2;
    for (int i = 0; i < 5; ++i) {
        x = x - gain * (x - target);
    }
    std::cout << "final_state=" << x << "\n";
    return 0;
}

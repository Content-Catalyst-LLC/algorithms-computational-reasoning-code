#include <iostream>

int main() {
    double value = 12.0;
    double trigger = 10.0;
    std::cout << "event_triggered=" << (value >= trigger ? "true" : "false") << "\n";
    return 0;
}

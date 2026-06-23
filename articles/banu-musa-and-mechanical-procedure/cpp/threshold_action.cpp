#include <iostream>

int main() {
    double level = 7.5;
    double threshold = 5.0;
    std::cout << "action_triggered=" << (level >= threshold ? "true" : "false") << "\n";
    return 0;
}

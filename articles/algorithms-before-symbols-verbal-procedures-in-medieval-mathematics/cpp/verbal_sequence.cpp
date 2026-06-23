#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> steps = {"take the number", "double it", "add the adjustment", "check the result"};
    for (std::size_t i = 0; i < steps.size(); ++i) {
        std::cout << i + 1 << ": " << steps[i] << "\n";
    }
    return 0;
}

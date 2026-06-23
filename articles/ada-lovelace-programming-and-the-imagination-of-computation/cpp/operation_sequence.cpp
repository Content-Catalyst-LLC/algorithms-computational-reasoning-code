#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> operations{"initialize", "store", "multiply", "subtract", "repeat", "output"};
    std::cout << "operation_count=" << operations.size() << "\n";
    for (std::size_t i = 0; i < operations.size(); ++i) {
        std::cout << operations[i] << (i + 1 == operations.size() ? "\n" : " -> ");
    }
    return 0;
}

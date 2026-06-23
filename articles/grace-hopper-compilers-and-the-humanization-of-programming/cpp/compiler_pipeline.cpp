#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string source = "ADD PAYROLL-TOTAL TO TAX-BASE";
    std::istringstream stream(source);
    std::vector<std::string> tokens;
    std::string token;
    while (stream >> token) tokens.push_back(token);

    std::cout << "source=" << source << "\n";
    std::cout << "tokens=[";
    for (size_t i = 0; i < tokens.size(); ++i) {
        std::cout << tokens[i] << (i + 1 < tokens.size() ? ", " : "");
    }
    std::cout << "]\n";
    std::cout << "target_code=machine-specific instruction sequence\n";
}

#include <iostream>
#include <string>

std::string unary_increment(std::string tape) {
    std::size_t i = 0;
    while (i < tape.size() && tape[i] == '1') {
        i++;
    }
    if (i == tape.size()) {
        tape.push_back('_');
    }
    tape[i] = '1';
    if (i + 1 == tape.size()) {
        tape.push_back('_');
    }
    return tape;
}

int main() {
    std::cout << "incremented_tape=" << unary_increment("111_") << "\n";
    return 0;
}

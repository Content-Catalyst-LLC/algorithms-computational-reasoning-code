#include <iostream>
#include <string>
#include <vector>

struct Instruction {
    std::string op;
    int arg;
};

int main() {
    std::vector<Instruction> program{{"LOAD", 2}, {"ADD", 3}, {"STORE", 0}, {"HALT", 0}};
    int acc = 0;
    for (const auto& inst : program) {
        if (inst.op == "LOAD") acc = inst.arg;
        else if (inst.op == "ADD") acc += inst.arg;
        else if (inst.op == "STORE") std::cout << "store address=" << inst.arg << " value=" << acc << "\n";
        else if (inst.op == "HALT") {
            std::cout << "halt accumulator=" << acc << "\n";
            break;
        }
    }
    return 0;
}

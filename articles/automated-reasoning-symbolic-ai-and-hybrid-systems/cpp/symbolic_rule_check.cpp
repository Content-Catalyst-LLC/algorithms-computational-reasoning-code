#include <iostream>
#include <set>
#include <string>
#include <vector>

int main() {
    std::set<std::string> facts = {"has_documentation", "logs_decisions"};
    std::vector<std::string> premises = {"has_documentation", "logs_decisions"};
    bool fires = true;
    for (const auto& premise : premises) {
        if (!facts.count(premise)) fires = false;
    }
    std::cout << "rule_fires=" << std::boolalpha << fires << "\n";
    return 0;
}

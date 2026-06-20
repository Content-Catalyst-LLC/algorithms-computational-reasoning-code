#include <iostream>
#include <vector>

struct ClientUpdate {
    int examples;
    double weight;
};

double federated_average(const std::vector<ClientUpdate>& updates) {
    int total = 0;
    double weighted = 0.0;
    for (const auto& update : updates) {
        total += update.examples;
        weighted += update.examples * update.weight;
    }
    return total == 0 ? 0.0 : weighted / total;
}

int main() {
    std::vector<ClientUpdate> updates = {{100, 0.42}, {240, 0.55}, {160, 0.49}};
    std::cout << "federated average weight=" << federated_average(updates) << "\n";
    return 0;
}

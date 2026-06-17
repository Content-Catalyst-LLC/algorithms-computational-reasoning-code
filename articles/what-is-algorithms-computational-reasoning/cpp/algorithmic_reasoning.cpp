#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Scenario {
  std::string name;
  double representation;
  double correctness;
  double governance;
  double brute_force;
};

int main() {
  std::vector<Scenario> scenarios = {
    {"Brute-force procedure", 40, 28, 20, 92},
    {"Indexed search design", 62, 52, 38, 42},
    {"Graph-aware reasoning", 76, 68, 54, 30},
    {"Governed computational reasoning", 86, 82, 86, 18}
  };
  std::cout << "scenario,reasoning_score,warning\n";
  for (const auto& s : scenarios) {
    double score = std::clamp(0.30 * s.representation + 0.30 * s.correctness + 0.30 * s.governance - 0.10 * s.brute_force, 0.0, 100.0);
    std::cout << s.name << "," << score << ",Synthetic governance diagnostic only.\n";
  }
}

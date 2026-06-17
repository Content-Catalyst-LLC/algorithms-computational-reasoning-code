#include <iostream>
#include <string>
#include <vector>

struct AbstractionCase {
  std::string name;
  double clarity;
  double scope;
  double detail;
  double interpretation;
  double governance;
};

int main() {
  std::vector<AbstractionCase> cases = {
    {"Search ranking", 82, 70, 62, 60, 56},
    {"Transit model", 78, 72, 66, 72, 66},
    {"Database schema", 84, 78, 70, 74, 70},
    {"Decision-support score", 70, 60, 48, 52, 66}
  };
  std::cout << "case_name,abstraction_score,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.clarity + 0.20*c.scope + 0.20*c.detail + 0.23*c.interpretation + 0.15*c.governance;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

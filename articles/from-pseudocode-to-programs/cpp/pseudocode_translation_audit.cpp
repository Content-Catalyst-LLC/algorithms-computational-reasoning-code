#include <iostream>
#include <string>
#include <vector>

struct TranslationCase {
  std::string name;
  double intent;
  double control;
  double edge;
  double tests;
  double maintain;
};

int main() {
  std::vector<TranslationCase> cases = {
    {"Search ranking prototype", 82, 80, 64, 68, 72},
    {"Decision-rule implementation", 76, 74, 66, 62, 68},
    {"Simulation loop", 84, 82, 72, 70, 74},
    {"Data-cleaning procedure", 78, 76, 70, 66, 72}
  };
  std::cout << "case_name,translation_quality,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.intent + 0.22*c.control + 0.18*c.edge + 0.18*c.tests + 0.20*c.maintain;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

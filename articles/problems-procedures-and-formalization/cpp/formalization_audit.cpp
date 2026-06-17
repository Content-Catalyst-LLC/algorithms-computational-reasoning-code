#include <iostream>
#include <string>
#include <vector>

struct FormalizationCase {
  std::string name;
  double input;
  double output;
  double objective;
  double assumptions;
  double governance;
};

int main() {
  std::vector<FormalizationCase> cases = {
    {"Document search", 82, 78, 70, 58, 56},
    {"Worker scheduling", 72, 76, 58, 54, 62},
    {"Public service triage", 60, 72, 52, 46, 66},
    {"Scientific simulation", 86, 80, 76, 84, 70}
  };
  std::cout << "case_name,formalization_score,warning\n";
  for (const auto& c : cases) {
    double score = 0.20*c.input + 0.20*c.output + 0.25*c.objective + 0.20*c.assumptions + 0.15*c.governance;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

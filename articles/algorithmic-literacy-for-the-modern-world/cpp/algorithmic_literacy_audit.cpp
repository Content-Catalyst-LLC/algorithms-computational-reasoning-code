#include <iostream>
#include <string>
#include <vector>

struct LiteracyCase {
  std::string name;
  double transparency;
  double interpretability;
  double contestability;
  double governance;
  double judgment;
};

int main() {
  std::vector<LiteracyCase> cases = {
    {"Search ranking", 62, 66, 38, 52, 68},
    {"Public decision-support workflow", 58, 56, 70, 76, 74},
    {"Scientific simulation dashboard", 76, 74, 60, 68, 80},
    {"Recommendation feed", 40, 48, 32, 46, 50}
  };
  std::cout << "case_name,literacy_support_score,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.transparency + 0.22*c.interpretability + 0.18*c.contestability + 0.18*c.governance + 0.20*c.judgment;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

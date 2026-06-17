#include <iostream>
#include <string>
#include <vector>

struct DecompositionCase {
  std::string name;
  double subproblem;
  double boundary;
  double sequencing;
  double dependencies;
  double recomposition;
};

int main() {
  std::vector<DecompositionCase> cases = {
    {"Search system", 82, 78, 82, 72, 72},
    {"Public decision-support workflow", 74, 66, 68, 60, 58},
    {"Scientific simulation", 86, 82, 80, 78, 82},
    {"Knowledge architecture", 80, 76, 74, 70, 80}
  };
  std::cout << "case_name,decomposition_score,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.subproblem + 0.20*c.boundary + 0.18*c.sequencing + 0.20*c.dependencies + 0.20*c.recomposition;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

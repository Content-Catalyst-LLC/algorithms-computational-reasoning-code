#include <iostream>
#include <string>
#include <vector>

struct DebugCase {
  std::string name;
  double reproduce;
  double trace;
  double isolate;
  double verify;
  double regression;
};

int main() {
  std::vector<DebugCase> cases = {
    {"Graph traversal infinite loop", 88, 78, 80, 82, 78},
    {"Data pipeline missing-value bug", 84, 74, 72, 76, 74},
    {"Simulation instability", 80, 78, 70, 74, 66},
    {"Recommendation ranking tie bug", 76, 68, 70, 72, 70}
  };
  std::cout << "case_name,debugging_quality,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.reproduce + 0.20*c.trace + 0.18*c.isolate + 0.22*c.verify + 0.18*c.regression;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

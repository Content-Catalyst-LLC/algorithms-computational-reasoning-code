#include <iostream>
#include <string>
#include <vector>

struct BoundaryCase {
  std::string name;
  double input;
  double output;
  double state;
  double stopping;
  double failure;
};

int main() {
  std::vector<BoundaryCase> cases = {
    {"Graph traversal", 84, 80, 86, 80, 70},
    {"Decision-support workflow", 68, 70, 74, 62, 60},
    {"Numerical simulation", 82, 78, 84, 78, 66},
    {"Recommendation ranking", 74, 72, 70, 60, 52}
  };
  std::cout << "case_name,boundary_score,warning\n";
  for (const auto& c : cases) {
    double score = 0.22*c.input + 0.22*c.output + 0.22*c.state + 0.20*c.stopping + 0.14*c.failure;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

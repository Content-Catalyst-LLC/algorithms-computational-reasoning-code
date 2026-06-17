#include <iostream>
#include <string>
#include <vector>

struct LogicCase {
  std::string name;
  double rule;
  double predicate;
  double trace;
  double test;
  double governance;
};

int main() {
  std::vector<LogicCase> cases = {
    {"Input validation rules", 82, 84, 68, 82, 70},
    {"Database query constraints", 78, 80, 72, 76, 72},
    {"Decision-rule workflow", 74, 70, 68, 72, 78},
    {"Program invariant checks", 80, 78, 74, 80, 66}
  };
  std::cout << "case_name,logic_quality,warning\n";
  for (const auto& c : cases) {
    double score = 0.24*c.rule + 0.24*c.predicate + 0.20*c.trace + 0.18*c.test + 0.14*c.governance;
    std::cout << c.name << "," << score << ",Synthetic educational diagnostic only.\n";
  }
}

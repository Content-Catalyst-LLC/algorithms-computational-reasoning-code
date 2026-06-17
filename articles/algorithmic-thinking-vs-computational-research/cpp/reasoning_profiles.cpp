#include <iostream>
#include <string>
#include <vector>

struct Profile {
  std::string name;
  double step;
  double decomp;
  double control;
  double test;
  double representation;
  double governance;
};

int main() {
  std::vector<Profile> profiles = {
    {"Recipe-like procedure", 86, 72, 70, 62, 42, 20},
    {"Classroom algorithm exercise", 90, 82, 84, 78, 62, 32},
    {"Search and ranking system", 72, 70, 76, 66, 78, 70},
    {"Public decision-support workflow", 68, 66, 64, 72, 80, 86},
    {"Scientific modeling workflow", 74, 78, 76, 82, 86, 74}
  };
  std::cout << "name,algorithmic_score,computational_score,warning\n";
  for (const auto& p : profiles) {
    double algorithmic = 0.28*p.step + 0.24*p.decomp + 0.24*p.control + 0.24*p.test;
    double computational = 0.16*p.step + 0.14*p.decomp + 0.14*p.control + 0.14*p.test + 0.22*p.representation + 0.20*p.governance;
    std::cout << p.name << "," << algorithmic << "," << computational << ",Synthetic educational diagnostic only.\n";
  }
}

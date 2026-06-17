#include <stdio.h>

typedef struct {
  const char* name;
  double subproblem;
  double boundary;
  double sequencing;
  double dependencies;
  double recomposition;
} DecompositionCase;

int main(void) {
  DecompositionCase cases[] = {
    {"Search system", 82, 78, 82, 72, 72},
    {"Public decision-support workflow", 74, 66, 68, 60, 58},
    {"Scientific simulation", 86, 82, 80, 78, 82},
    {"Knowledge architecture", 80, 76, 74, 70, 80}
  };
  printf("case_name,decomposition_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].subproblem + 0.20*cases[i].boundary + 0.18*cases[i].sequencing + 0.20*cases[i].dependencies + 0.20*cases[i].recomposition;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

#include <stdio.h>

typedef struct {
  const char* name;
  double input;
  double output;
  double state;
  double stopping;
  double failure;
} BoundaryCase;

int main(void) {
  BoundaryCase cases[] = {
    {"Graph traversal", 84, 80, 86, 80, 70},
    {"Decision-support workflow", 68, 70, 74, 62, 60},
    {"Numerical simulation", 82, 78, 84, 78, 66},
    {"Recommendation ranking", 74, 72, 70, 60, 52}
  };
  printf("case_name,boundary_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].input + 0.22*cases[i].output + 0.22*cases[i].state + 0.20*cases[i].stopping + 0.14*cases[i].failure;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

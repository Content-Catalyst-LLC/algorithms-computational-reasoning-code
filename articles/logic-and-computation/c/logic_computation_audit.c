#include <stdio.h>

typedef struct {
  const char* name;
  double rule;
  double predicate;
  double trace;
  double test;
  double governance;
} LogicCase;

int main(void) {
  LogicCase cases[] = {
    {"Input validation rules", 82, 84, 68, 82, 70},
    {"Database query constraints", 78, 80, 72, 76, 72},
    {"Decision-rule workflow", 74, 70, 68, 72, 78},
    {"Program invariant checks", 80, 78, 74, 80, 66}
  };
  printf("case_name,logic_quality,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.24*cases[i].rule + 0.24*cases[i].predicate + 0.20*cases[i].trace + 0.18*cases[i].test + 0.14*cases[i].governance;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

#include <stdio.h>

typedef struct {
  const char* name;
  double clarity;
  double scope;
  double detail;
  double interpretation;
  double governance;
} AbstractionCase;

int main(void) {
  AbstractionCase cases[] = {
    {"Search ranking", 82, 70, 62, 60, 56},
    {"Transit model", 78, 72, 66, 72, 66},
    {"Database schema", 84, 78, 70, 74, 70},
    {"Decision-support score", 70, 60, 48, 52, 66}
  };
  printf("case_name,abstraction_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].clarity + 0.20*cases[i].scope + 0.20*cases[i].detail + 0.23*cases[i].interpretation + 0.15*cases[i].governance;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

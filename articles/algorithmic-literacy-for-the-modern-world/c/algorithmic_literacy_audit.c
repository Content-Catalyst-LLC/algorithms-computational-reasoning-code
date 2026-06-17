#include <stdio.h>

typedef struct {
  const char* name;
  double transparency;
  double interpretability;
  double contestability;
  double governance;
  double judgment;
} LiteracyCase;

int main(void) {
  LiteracyCase cases[] = {
    {"Search ranking", 62, 66, 38, 52, 68},
    {"Public decision-support workflow", 58, 56, 70, 76, 74},
    {"Scientific simulation dashboard", 76, 74, 60, 68, 80},
    {"Recommendation feed", 40, 48, 32, 46, 50}
  };
  printf("case_name,literacy_support_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].transparency + 0.22*cases[i].interpretability + 0.18*cases[i].contestability + 0.18*cases[i].governance + 0.20*cases[i].judgment;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

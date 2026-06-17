#include <stdio.h>

typedef struct {
  const char* name;
  double intent;
  double control;
  double edge;
  double tests;
  double maintain;
} TranslationCase;

int main(void) {
  TranslationCase cases[] = {
    {"Search ranking prototype", 82, 80, 64, 68, 72},
    {"Decision-rule implementation", 76, 74, 66, 62, 68},
    {"Simulation loop", 84, 82, 72, 70, 74},
    {"Data-cleaning procedure", 78, 76, 70, 66, 72}
  };
  printf("case_name,translation_quality,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].intent + 0.22*cases[i].control + 0.18*cases[i].edge + 0.18*cases[i].tests + 0.20*cases[i].maintain;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

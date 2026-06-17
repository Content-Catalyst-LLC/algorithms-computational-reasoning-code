#include <stdio.h>

typedef struct {
  const char* name;
  double input;
  double output;
  double objective;
  double assumptions;
  double governance;
} FormalizationCase;

int main(void) {
  FormalizationCase cases[] = {
    {"Document search", 82, 78, 70, 58, 56},
    {"Worker scheduling", 72, 76, 58, 54, 62},
    {"Public service triage", 60, 72, 52, 46, 66},
    {"Scientific simulation", 86, 80, 76, 84, 70}
  };
  printf("case_name,formalization_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.20*cases[i].input + 0.20*cases[i].output + 0.25*cases[i].objective + 0.20*cases[i].assumptions + 0.15*cases[i].governance;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

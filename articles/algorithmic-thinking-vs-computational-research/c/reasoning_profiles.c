#include <stdio.h>

typedef struct {
  const char* name;
  double step;
  double decomp;
  double control;
  double test;
  double representation;
  double governance;
} Profile;

int main(void) {
  Profile profiles[] = {
    {"Recipe-like procedure", 86, 72, 70, 62, 42, 20},
    {"Classroom algorithm exercise", 90, 82, 84, 78, 62, 32},
    {"Search and ranking system", 72, 70, 76, 66, 78, 70},
    {"Public decision-support workflow", 68, 66, 64, 72, 80, 86},
    {"Scientific modeling workflow", 74, 78, 76, 82, 86, 74}
  };
  printf("name,algorithmic_score,computational_score,warning\n");
  for (int i = 0; i < 5; i++) {
    double algorithmic = 0.28*profiles[i].step + 0.24*profiles[i].decomp + 0.24*profiles[i].control + 0.24*profiles[i].test;
    double computational = 0.16*profiles[i].step + 0.14*profiles[i].decomp + 0.14*profiles[i].control + 0.14*profiles[i].test + 0.22*profiles[i].representation + 0.20*profiles[i].governance;
    printf("%s,%.3f,%.3f,Synthetic educational diagnostic only.\n", profiles[i].name, algorithmic, computational);
  }
  return 0;
}

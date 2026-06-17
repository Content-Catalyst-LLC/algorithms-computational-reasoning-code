#include <stdio.h>

typedef struct {
  const char* name;
  double reproduce;
  double trace;
  double isolate;
  double verify;
  double regression;
} DebugCase;

int main(void) {
  DebugCase cases[] = {
    {"Graph traversal infinite loop", 88, 78, 80, 82, 78},
    {"Data pipeline missing-value bug", 84, 74, 72, 76, 74},
    {"Simulation instability", 80, 78, 70, 74, 66},
    {"Recommendation ranking tie bug", 76, 68, 70, 72, 70}
  };
  printf("case_name,debugging_quality,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = 0.22*cases[i].reproduce + 0.20*cases[i].trace + 0.18*cases[i].isolate + 0.22*cases[i].verify + 0.18*cases[i].regression;
    printf("%s,%.3f,Synthetic educational diagnostic only.\n", cases[i].name, score);
  }
  return 0;
}

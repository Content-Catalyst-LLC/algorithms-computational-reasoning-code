#include <stdio.h>

typedef struct {
  const char* name;
  double representation;
  double correctness;
  double governance;
  double brute_force;
} Scenario;

static double clamp(double v) {
  if (v < 0.0) return 0.0;
  if (v > 100.0) return 100.0;
  return v;
}

int main(void) {
  Scenario scenarios[] = {
    {"Brute-force procedure", 40, 28, 20, 92},
    {"Indexed search design", 62, 52, 38, 42},
    {"Graph-aware reasoning", 76, 68, 54, 30},
    {"Governed computational reasoning", 86, 82, 86, 18}
  };
  printf("scenario,reasoning_score,warning\n");
  for (int i = 0; i < 4; i++) {
    double score = clamp(0.30 * scenarios[i].representation + 0.30 * scenarios[i].correctness + 0.30 * scenarios[i].governance - 0.10 * scenarios[i].brute_force);
    printf("%s,%.3f,Synthetic governance diagnostic only.\n", scenarios[i].name, score);
  }
  return 0;
}

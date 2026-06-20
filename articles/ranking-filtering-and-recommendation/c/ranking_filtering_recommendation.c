#include <stdio.h>
double ranking_score(double text_match, double quality, double freshness, double diversity_bonus, double risk_penalty) {
    return 0.36*text_match + 0.30*quality + 0.16*freshness + 0.14*diversity_bonus - 0.20*risk_penalty;
}
int main(void) { printf("%.6f\n", ranking_score(0.92, 0.88, 0.60, 0.35, 0.04)); return 0; }

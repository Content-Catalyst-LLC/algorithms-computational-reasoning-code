#include <stdio.h>

int main(void) {
    double due_process = 0.58;
    double transparency = 0.52;
    double human_review = 0.60;
    double appeal_readiness = 0.54;
    double score = (due_process + transparency + human_review + appeal_readiness) / 4.0;
    printf("procedural_readiness_score=%.4f\n", score);
    return 0;
}

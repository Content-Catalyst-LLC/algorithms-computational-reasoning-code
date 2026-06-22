#include <stdio.h>

int main(void) {
    double notice = 0.70;
    double reasons = 0.62;
    double evidence_access = 0.48;
    double human_review = 0.55;
    double correction = 0.52;
    double remedy = 0.44;
    double score = (notice + reasons + evidence_access + human_review + correction + remedy) / 6.0;
    printf("contestability_score=%.4f\n", score);
    return 0;
}

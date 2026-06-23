#include <stdio.h>

int main(void) {
    double engagement_pressure = 0.92;
    double creator_impact = 0.88;
    double public_knowledge_impact = 0.78;
    double user_control = 0.44;
    double contestability = 0.42;
    double score = (engagement_pressure + creator_impact + public_knowledge_impact + (1.0 - user_control) + (1.0 - contestability)) / 5.0;
    printf("attention_risk_score=%.4f\n", score);
    return 0;
}

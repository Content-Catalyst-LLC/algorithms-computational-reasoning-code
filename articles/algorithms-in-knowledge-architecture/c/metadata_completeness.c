#include <stdio.h>

int main(void) {
    double present_fields = 11.0;
    double required_fields = 12.0;
    double score = present_fields / required_fields;
    printf("metadata_completeness_score=%.4f\n", score);
    return 0;
}

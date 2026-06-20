#include <stdio.h>

int main(void) {
    const char *names[] = {"A", "B", "C", "D"};
    double score[] = {0.52, 0.49, 0.82, 0.35};
    for (int i = 0; i < 4; i++) printf("%s %.2f\n", names[i], score[i]);
    return 0;
}

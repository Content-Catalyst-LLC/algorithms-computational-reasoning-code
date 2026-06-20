#include <stdio.h>

int feasible(int x, int y) {
    return 2*x + y <= 8 && x + 2*y <= 8 && x >= 0 && y >= 0;
}

int objective(int x, int y) { return 3*x + 4*y; }

int main(void) {
    int bx = 0, by = 0, bv = -1;
    for (int x = 0; x < 10; x++) {
        for (int y = 0; y < 10; y++) {
            if (feasible(x, y) && objective(x, y) > bv) {
                bx = x; by = y; bv = objective(x, y);
            }
        }
    }
    printf("best x=%d y=%d objective=%d\n", bx, by, bv);
    return 0;
}

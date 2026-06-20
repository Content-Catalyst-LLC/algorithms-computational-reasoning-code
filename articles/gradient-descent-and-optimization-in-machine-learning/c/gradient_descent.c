#include <stdio.h>

typedef struct { double x; double y; } Point;

static Point DATA[] = {{-2,-2.85},{-1,-0.67},{0,1.47},{1,3.63},{2,5.82}};
static int N = 5;

double mse(double w, double b) {
    double total = 0.0;
    for (int i=0; i<N; i++) {
        double e = DATA[i].y - (w * DATA[i].x + b);
        total += e * e;
    }
    return total / N;
}

void step(double *w, double *b, double eta) {
    double grad_w = 0.0, grad_b = 0.0;
    for (int i=0; i<N; i++) {
        double err = ((*w) * DATA[i].x + (*b)) - DATA[i].y;
        grad_w += (2.0 / N) * err * DATA[i].x;
        grad_b += (2.0 / N) * err;
    }
    *w -= eta * grad_w;
    *b -= eta * grad_b;
}

int main(void) {
    double w = 0.0, b = 0.0;
    for (int i=0; i<80; i++) step(&w, &b, 0.08);
    printf("weight=%.6f bias=%.6f loss=%.6f\n", w, b, mse(w,b));
    return 0;
}

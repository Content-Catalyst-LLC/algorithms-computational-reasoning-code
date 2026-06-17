#include <stdio.h>
int score_in_range(double x){ return x >= 0.0 && x <= 100.0; }
int main(void){ printf("test_name,status\nscore_72,%s\nscore_150,%s\n", score_in_range(72.0) ? "pass" : "fail", score_in_range(150.0) ? "pass" : "fail"); return 0; }

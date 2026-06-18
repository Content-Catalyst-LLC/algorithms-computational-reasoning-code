#include <stdio.h>
double efficiency_gain(double baseline, double optimized){ return (baseline - optimized) / baseline; }
int main(void){ printf("test_name,value\nefficiency_gain_percent,%.3f\n", 100*efficiency_gain(100.0,64.0)); return 0; }

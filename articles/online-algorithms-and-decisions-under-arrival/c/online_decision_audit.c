#include <stdio.h>
int main(void){ double threshold=5*10.0+50.0, offline=50.0; printf("test_name,value\nthreshold_strategy,%.3f\noffline_optimum,%.3f\nratio,%.3f\n", threshold, offline, threshold/offline); return 0; }

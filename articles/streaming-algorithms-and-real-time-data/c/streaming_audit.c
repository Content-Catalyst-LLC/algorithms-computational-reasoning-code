#include <stdio.h>
int main(void){ double arrival=90.0, processing=100.0; printf("test_name,value\nutilization,%.3f\nstable,%s\n", arrival/processing, arrival < processing ? "true" : "false"); return 0; }

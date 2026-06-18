#include <stdio.h>
int growth(int b, int d){ int total=0, pow=1; for(int i=0;i<=d;i++){ total += pow; pow *= b; } return total; }
int main(void){ printf("test_name,value\nsearch_space_growth,%d\npermutation_count,6\n", growth(2,3)); return 0; }

#include <stdio.h>
double selection_rows(double rows,double selectivity){ return rows*selectivity; }
double join_rows(double l,double r,double ld,double rd){ double d = ld > rd ? ld : rd; return (l*r)/d; }
int main(void){ printf("test_name,value\nselection_estimated_rows,%.3f\njoin_estimated_rows,%.3f\n", selection_rows(1000000,0.012), join_rows(500000,200000,50000,40000)); return 0; }

#include <stdio.h>
int linear_search(int *xs, int n, int target){ for(int i=0;i<n;i++){ if(xs[i]==target) return i; } return -1; }
int main(void){ int xs[]={7,2,9,1}; printf("test_name,value\nlinear_search_9,%d\nsort_demo,1:2:7:9\n", linear_search(xs,4,9)); return 0; }

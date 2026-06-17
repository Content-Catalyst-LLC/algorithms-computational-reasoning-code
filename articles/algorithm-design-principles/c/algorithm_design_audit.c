#include <stdio.h>
int nondecreasing(int *xs, int n){ for(int i=0;i<n-1;i++){ if(xs[i] > xs[i+1]) return 0; } return 1; }
int main(void){ int a[]={1,2,2,3}; int b[]={1,3,2}; printf("test_name,status\nsorted_valid,%s\nsorted_invalid,%s\n", nondecreasing(a,4)?"pass":"fail", nondecreasing(b,3)?"pass":"fail"); return 0; }

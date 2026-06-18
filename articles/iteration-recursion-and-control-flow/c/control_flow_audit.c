#include <stdio.h>
int factorial(int n){ return n <= 0 ? 1 : n * factorial(n-1); }
int main(void){ printf("test_name,value\nfactorial_5,%d\niterative_sum,%d\n", factorial(5), 1+2+3); return 0; }

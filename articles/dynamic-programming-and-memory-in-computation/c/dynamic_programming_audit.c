#include <stdio.h>
int fib(int n){ int dp[64]={0}; dp[1]=1; for(int i=2;i<=n;i++){ dp[i]=dp[i-1]+dp[i-2]; } return dp[n]; }
int main(void){ printf("test_name,value\nfibonacci_10,%d\nstate_space_size,100000\n", fib(10)); return 0; }

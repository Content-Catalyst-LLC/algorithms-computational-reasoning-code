#include <iostream>
#include <vector>
int fib(int n){ std::vector<int> dp(n+2); dp[1]=1; for(int i=2;i<=n;i++) dp[i]=dp[i-1]+dp[i-2]; return dp[n]; }
int main(){ std::cout << "test_name,value\nfibonacci_10," << fib(10) << "\nstate_space_size,100000\n"; }

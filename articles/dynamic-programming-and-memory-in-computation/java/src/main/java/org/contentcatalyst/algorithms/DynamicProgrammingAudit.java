package org.contentcatalyst.algorithms;
public class DynamicProgrammingAudit {
  static int fib(int n){ int[] dp = new int[n+2]; dp[1]=1; for(int i=2;i<=n;i++){ dp[i]=dp[i-1]+dp[i-2]; } return dp[n]; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("fibonacci_10," + fib(10));
    System.out.println("state_space_size,100000");
  }
}

from __future__ import annotations

def fibonacci_memo(n: int, memo: dict[int,int] | None = None) -> int:
    if memo is None:
        memo={}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n]=n
    else:
        memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    return memo[n]

def edit_distance(a: str, b: str) -> int:
    rows=len(a)+1; cols=len(b)+1
    dp=[[0]*cols for _ in range(rows)]
    for i in range(rows): dp[i][0]=i
    for j in range(cols): dp[0][j]=j
    for i in range(1,rows):
        for j in range(1,cols):
            cost=0 if a[i-1]==b[j-1] else 1
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[-1][-1]

def knapsack_01(values: list[int], weights: list[int], capacity: int) -> int:
    dp=[0]*(capacity+1)
    for value, weight in zip(values, weights):
        for w in range(capacity, weight-1, -1):
            dp[w]=max(dp[w], value+dp[w-weight])
    return dp[capacity]

def state_space_size(dimensions: list[int]) -> int:
    total=1
    for dimension in dimensions:
        total *= dimension
    return total

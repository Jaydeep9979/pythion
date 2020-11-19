import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math,bisect,collections,functools
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    dp=[[-1 for i in range(len(arr)+10)] for j in range(len(arr)+10)]
    @functools.lru_cache(None)
    def solve(i,j):
        if i>=j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]

        mn=float('inf')
        for k in range(i,j):
            if dp[i][k]!=-1:
                t1=dp[i][k]
            else:
                t1=solve(i,k)
            if dp[k+1][j]!=-1:
                t2=dp[k+1][j]
            else:
                t2=solve(k+1,j)

    
            ans=t1+t2+arr[i-1]*arr[k]*arr[j]
            mn=min(mn,ans)
        
        dp[i][j]=mn
        return mn
    x=solve(1,len(arr)-1)
    









        
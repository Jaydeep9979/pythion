import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
import math,bisect,collections,functools
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    pre={}
    def solve(arr,i,j):
        if i>=j:
            return 0
        ans=float('inf')
        for k in range(i,j):
            if (i,k) in pre:
                t1=pre[(i,k)]
            else:
                t1=solve(arr,i,k)
            if (k+1,j) in pre:
                t2=pre[(k+1,j)]
            else:
                t2=solve(arr,k+1,j)
            temp=t1+t2+arr[i-1]*arr[k]*arr[j]
            
            ans=min(ans,temp)
        pre[(i,j)]=ans
        return ans
    print(solve(arr,1,len(arr)-1))


    




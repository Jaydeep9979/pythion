import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math,bisect,collections
for testcase in range(int(input())):
    s1=input()
    s2=input()
    dp=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    i=len(s1)
    j=len(s2)
    ans=''
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            ans+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>=dp[i][j-1]:
            ans+=s1[i-1]
            i-=1
        else:
            ans+=s2[j-1]
            j-=1
    while j>0:
        ans+=s2[j-1]
        j-=1
    while i>0:
        ans+=s1[i-1]
        i-=1
    ans=ans[::-1]
    for i in dp:
        print(i)
    print(ans)
    











        
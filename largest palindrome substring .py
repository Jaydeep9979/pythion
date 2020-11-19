import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s=input()
    if not s:
         print(0)
    ans=0
    dp=[[0 for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)-1,-1,-1):
        for j in range(i,len(s)):
            if i==j:
                dp[i][j]=1
            elif j==i+1 and s[i]==s[j]:
                dp[i][j]=1
            elif s[i]==s[j] and dp[i+1][j-1]==1:
                dp[i][j]=1
            else:
                dp[i][j]=0
            if dp[i][j]:
                ans=max(ans,j-i+1)
    for i in dp:
        print(i)
    print(ans)
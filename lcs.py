import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s1=input()
    s2=input()
    # def lcs(s1,s2,i,j):
    #     if i==0 or j==0:
    #         return 0
    #     if s1[i-1]==s2[j-1]:
    #         return 1+lcs(s1,s2,i-1,j-1)
    #     else:
    #         return max(lcs(s1,s2,i-1,j),lcs(s1,s2,i,j-1))
    # print(lcs(s1,s2,len(s1),len(s2)))


    dp=[[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1] and i!=j:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    for i in dp:
        print(i)
    print(dp[-1][-1])
    s=''
    i=len(s1)
    j=len(s2)
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            s+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]: 
            #s+=s1[i-1]
            i-=1
        else:
           # s+=s2[j-1]
            j-=1
    while i>0:
        s+=s1[i-1]
        i-=1
    while j>0:
        s+=s2[j-1]
        j-=1
    print(s[::-1])

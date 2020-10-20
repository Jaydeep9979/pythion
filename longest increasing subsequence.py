import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=[6,9,10,5,1,6,2]
    dp=[1]*len(arr)
    st=[-1]*len(arr)
    for i in range(len(arr)):   
        for j in range(i):
            if arr[i]>=arr[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                st[i]=j
    start=dp.index(max(dp))
    ans=[]
    print(st)
    while start!=-1:
        ans.append(arr[start])
        start=st[start]
    print(dp)
    print(ans[::-1])
    print(max(dp))


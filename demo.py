import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	coin=[1,2,5]
	total=7
	dp=[0 for i in range(total+1)]
	for i in range(1,total+1):
		dp[i]=float('inf')
	for i in range(1,(len(coin)+1)):
		for j in range(coin[i-1],total+1):
				#print(1+dp[i-1][j-coin[i-1]],dp[i-1][j],end=' ')
				dp[j]=min(1+dp[j-coin[i-1]],dp[j])
		print(dp)
		
	for i in dp:
		print(i,end=' ')
	print(dp[-1][-1])












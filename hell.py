import math,bisect,heapq,collections,itertools,datetime,functools,sys,os
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
n=int(input())
arr=list(map(int,input().split()))
for i in range(3,-1,-1):
	if i==1:
		break
print(i)
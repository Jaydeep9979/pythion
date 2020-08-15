import math,bisect,heapq,collections,itertools,datetime,functools,sys,os
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')

for testcase in range(int(input())):
	arr=list(map(int,input().split()))
	n=len(arr)
	flag=1
	for i in range(n-1,0,-1):
		if arr[i-1]<arr[i]:
			ind=i-1
			flag=0
			break
	if flag:
		arr.sort()
		print(arr)
	else:
		for i in range(len(arr)-1,ind,-1):
			if arr[ind]<arr[i]:
				arr[ind],arr[i]=arr[i],arr[ind]
				break
		print(arr)
		ind+=1
		n-=1
		while ind<n:
			arr[ind],arr[n]=arr[n],arr[ind]
			ind+=1
			n-=1
		print(arr)
			

	
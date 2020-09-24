import math,sys,os,collections,functools,itertools,string
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=[[1,0,0],[0,0,0],[0,0,0]]
	rows,cols=len(arr),len(arr[0])
	queue=collections.deque()
	for r,row in enumerate(arr):
		for c,val in enumerate(row):
			if val==1:
				queue.append((r,c))
	dist=0
	while queue:
		new=[]
		for r,c in queue:
			for i,j in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
				#print(i,j,row,col)
				if 0<=i<rows and 0<=j<cols and arr[i][j]==0:
					arr[i][j]=1
					new.append((i,j))
		queue=new
		if new:
			dist+=1
	print(dist)


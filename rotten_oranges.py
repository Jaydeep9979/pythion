import math,sys,os,collections,functools,itertools,string
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=[[2,1,1],[1,1,0],[0,1,1]]
    queue=collections.deque() 
    row,col=len(arr),len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==2:
                queue.append((i,j))
    time=0			
    while queue:
        for i in arr:
            print(i)
        print()
        new=[]
        for i,j in queue:
            if i-1>=0 and arr[i-1][j]==1:
                arr[i-1][j]=2
                new.append((i-1,j))
            if i+1<row and arr[i+1][j]==1:
                arr[i+1][j]=2
                new.append((i+1,j))
            if j-1>=0 and arr[i][j-1]==1: 
                arr[i][j-1]=2
                new.append((i,j-1))
            if j+1<col and arr[i][j+1]==1:
                arr[i][j+1]=2
                new.append((i,j+1))
        if new:
            time+=1
        queue=new
    f=0
    for i in range(row):
        for j in range(col):
            if arr[i][j]==1:
               # return -1
                print(-1)
                f=1
    print(time)
    if not f:
        print(time)	

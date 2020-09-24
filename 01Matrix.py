class Solution:
    def updateMatrix(self, arr: List[List[int]]) -> List[List[int]]:
        if len(arr)==0:
            return arr
    	dist=[[float('inf') for i in range(len(arr[0]))] for j in range(len(arr))]
        queue=collections.deque()
        row,col=len(arr),len(arr[0])
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j]==0:
                    dist[i][j]=0
                    queue.append((i,j))
        
        while queue:
            new=[]
            for i in dist:
                print(i)
            print()
            # i,j=queue.pop()
            # for r,c in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
            #     if 0<=r<row and 0<=c<col and dist[i][j]+1<dist[r][c]:
            #         dist[r][c]=dist[i][j]+1
            #         queue.append((r,c))

            for i,j in queue:
            	if i-1>=0 and dist[i-1][j]>dist[i][j]+1:
            		dist[i-1][j]=dist[i][j]+1
            		new.append((i-1,j))
            	if j-1>=0 and dist[i][j-1]>dist[i][j]+1:
            		dist[i][j-1]=dist[i][j]+1
            		new.append((i,j-1))
            	if i+1<row and dist[i+1][j]>dist[i][j]+1:
            		dist[i+1][j]=dist[i][j]+1
            		new.append((i+1,j))
            	if j+1<col and dist[i][j+1]>dist[i][j]+1:
            		dist[i][j+1]=dist[i][j]+1
            		new.append((i,j+1))
            queue=new
        for i in dist:
            print(i)    
            
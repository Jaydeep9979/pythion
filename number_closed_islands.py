class Solution:
    def closedIsland(self, arr: List[List[int]]) -> int:
    	if len(arr)==1:
		return 0
        row,col=len(arr),len(arr[0])
        def dfs(arr,i,j):
            if 0<=i<row and 0<=j<col and arr[i][j]==0:
                arr[i][j]=-1
                dfs(arr,i,j+1)
                dfs(arr,i+1,j)
                dfs(arr,i,j-1)
                dfs(arr,i-1,j)
            
        for i in range(row):
            for j in range(col):
                if (i==0 or j==0 or i==(row-1) or j==(col-1)) and arr[i][j]==0:
                    dfs(arr,i,j)
        count=0
        for i in range(row):
            for j in range(col):
                if arr[i][j]==0:
                    dfs(arr,i,j)
                    count+=1
        return (count)
            
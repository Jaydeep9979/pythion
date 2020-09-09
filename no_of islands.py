class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        def dfs(grid,i,j):
            if i<row and j<col and grid[i][j]=="1":
                grid[i][j]="0"
                dfs(grid,i+1,j)
                dfs(grid,i,j+1)
                dfs(grid,i-1,j)
                dfs(grid,i,j-1)
            return 
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    count+=1
                    dfs(grid,i,j)
        return (count)



                

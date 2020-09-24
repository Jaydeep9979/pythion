class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        ans=0
        def dfs(grid,i,j):
            if 0<=i<row and 0<=j<col and grid[i][j]=='S':
                grid[i][j]='#'
                return 1+dfs(grid,i+1,j)+dfs(grid,i,j+1)+dfs(grid,i-1,j)+dfs(grid,i,j-1)+
                        dfs(grid,i-1,j-1)+dfs(grid,i-1,j+1)+dfs(grid,i+1,j-1)+dfs(grid,i+1,j+1)
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='S':
                    ans=max(ans,dfs(grid,i,j))
        return ans
        
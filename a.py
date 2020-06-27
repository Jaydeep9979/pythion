class Solution:
    def findTargetSumWays(self, arr: List[int], diff: int) -> int:
        target=(sum(arr)-diff)//2
        dp=[[1 for i in range(target+1)] for j in range(len(arr)+1)]
        for i in range(1,target+1):
            dp[0][i]=0
        for i in range(1,len(arr)+1):
            for j in range(1,target+1):
                if arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
        return dp[-1][-1]
        
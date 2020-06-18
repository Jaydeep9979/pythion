class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        
        s2=s1[::-1]
        if s1==s2:
            return len(s1)

        dp=[[0 for i in range(len(s1)+1)] for j in range(len(s1)+1)]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s1)+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1]
                

                

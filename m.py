class Solution:
    def numSub(self, s: str) -> int:
        count=0
        ans=collections.defaultdict(int)
        for i in s:
            if i=='0':
                count=0
                ans[count]+=1
            else:
                count+=1
        x=0
        for key,val in ans.items():
            if key!=0:
                x+=(val*(val+1))//2
        return x
        git add.e
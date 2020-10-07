class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        stack=[]
        left=[]
        for i,val in enumerate(height):
            while stack and stack[-1][0]>=val:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][1])
            stack.append((val,i))   
        right=[]
        n=len(height)
        stack=[]
        for i in range(len(height)-1,-1,-1):
            val=height[i]
            while stack and stack[-1][0]>=val:
                stack.pop()
            #stack is empty 
            if not stack:
                right.append(n)
            else:
                right.append(stack[-1][1])
            stack.append((val,i))
        right=list(reversed(right))
        ans=0
        for i in range(len(height)):
            r=right[i]
            l=left[i]
            val=height[i]
            ans=max(ans,(r-l-1)*val)
        return ans

        
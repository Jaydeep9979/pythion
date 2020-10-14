class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        jumps=0
        curend=0
        cur_far_end=0
        for i in range(len(nums)-1):
            if i>cur_far_end:
                return -1
            cur_far_end=max(cur_far_end,i+nums[i])
            if curend==i:
                jumps+=1
                curend=cur_far_end
        return jumps
                
# This is an implicit bfs solution. i == curEnd means you visited 
# all the items on the current level. Incrementing jumps++ is like incrementing 
# the level you are on. And curEnd = curFarthest
# is like getting the queue size (level size) for the next level you are traversing.
            
            
            

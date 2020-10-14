import collections
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]>=0 and 0<=start<len(arr):
            if arr[start]==0:
                return True
            arr[start]=-arr[start]
            return self.canReach(arr,start+arr[start]) or self.canReach(arr,start-arr[start])
        return False


        #BFS Approach
        # if arr[start]==0:
        #     return True
        # queue=collections.deque()       
        # queue.append(start)
        # visited=[False]*(len(arr))
        # while queue:
        #     index=queue.popleft()
        #     for new_ind in [index+arr[index],index-arr[index]]:
        #         if 0<=new_ind<len(arr) and not visited[new_ind]:  
        #             if arr[new_ind]==0:
        #                 return True
        #             queue.append(new_ind)
        #     visited[index]=True
        # return False

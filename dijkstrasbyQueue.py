import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph={}
        for u,v,w  in times:
            graph[u]=(v,w)
        queue=collections.deque()
        queue.append(K,0)
        distance=[float('inf')]*(N+1)
        distance[0]=0
        while queue:
            vertex,dist=queue.popleft()
            if dist<distance[vertex]:
                distance[vertex]=dist
                for v,w in graph[vertex]:
                    queue.append((v,w+dist))
        mx=max(distance)
        if mx==float('inf'):
            return -1
        return mx




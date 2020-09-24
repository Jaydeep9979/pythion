import collections,heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph,queue,distance=collections.defaultdict(list),[],[0]+[float('inf')]*N
        for u,v,w in times:
            graph[u].append((v,w))
            heapq.heappush(queue,(K,0))
            while queue:
                node,time=heapq.heappop(queue)
                if time < distance[node]:
                    distance[node]=time
                    for v,w in graph[node]:
                        heapq.heappush(queue,(v,time+w))

        mx=max(distance)
        if mx==float('inf'):
            return -1
        return mx
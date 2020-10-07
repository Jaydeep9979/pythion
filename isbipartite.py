import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        color=[-1]*(N+1)
        graph=[[] for i in range(N+1)]
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        def isbipartite(graph,N,color,node):
            color[node]=1
            queue=collections.deque()
            queue.append(node)
            while queue:
                curr=queue.popleft()
                for new in graph[curr]:
                    if color[curr]==color[new]:
                        return False
                    if color[new]==-1:
                        color[new]=1-color[curr]
                        queue.append(new)
            return True
        for node in range(1,N+1):
            if color[node]==-1:
                if not isbipartite(graph,N,color,node):
                    return False
        return True


        


             
import collections
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        G=collections.defaultdict(list)
        visited=[0]*(len(graph))
        for i in range(len(graph)):
            for node in i:
                G[i].append(node)
        def dfs(node):
            if visited[node]==1:
                return True
            if visited[node]==-1:
                return False
            visited[node]=-1
            for vertex in graph[node]:
                if not dfs(vertex):
                    return False
            visited[node]=1
            return True
        ans=[]
        for node in list(G.keys()):
            if dfs(node):
                ans.append(node)
        print(ans)
    

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        visited=[0]*(numCourses)
        def dfs(node):
            if visited[node]==-1:
                return True
            if visited[node]:
                return False
            visited[node]=-1
            for vertex in graph[node]:
                if dfs(vertex):
                    return True
            visited[node]=1
            return False
        for node in list(graph.keys()):
            if  dfs(node):
                return True
            visited[node]=1
        return Fa

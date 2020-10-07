import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        visited=[0]*(numCourses)
        def dfs(node):
            if visited[node]==-1:
                return True
            if visited[node]==1:
                return False
            visited[node]=-1
            for adj in graph[node]:
                if dfs(adj):
                    return True
            return False
        for node in list(graph.keys()):
            if dfs(node):
                return []
        def check(node,stack):
            visited[node]=True
            for adj in graph[node]:
                if visited[adj]==False:
                    check(adj)
            stack.append(node)
        stack=[]
        visited=[False]*numCourses
        for node in range(numCourses):
            if visited[node]==False:
                check(node,stack)
        return stack[::-1]

        
        

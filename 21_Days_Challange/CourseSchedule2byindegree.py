import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(list)
        in_degree=collections.defaultdict(int)
        queue=collections.deque()
        for u,v in prerequisites:
            graph[u].append(v)
            in_degree[v]+=1
        for i in range(numCourses):
            if i not in in_degree:
                queue.append(i)       
        course_schedule=[]
        while queue:
            node=queue.popleft()
            course_schedule.append(node)
            in_degree[node]=0
            for adj in graph[node]:
                in_degree[adj]-=1
                if in_degree[adj]==0:     
                    queue.append(adj)
            graph[node]=[]
        return course_schedule
        
        



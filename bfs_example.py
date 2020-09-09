import math,sys,os,collections,functools
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	n=int(input())
	arr=[['a','b'],['a','c'],['b','d'],['e','b'],['d','e'],['d','f'],['e','f']]
	def bfs(s,graph,visited):
		queue=[]
		queue.append(s)
		visited[s]=1
		while queue:
			curr=queue.pop(0)
			print(curr,end=' ')
			for u in graph[curr]:
				if visited[u]!=1:
					queue.append(u)
					visited[u]=1

	graph=collections.defaultdict(list)
	for u,v in arr:
		graph[u].append(v)
	visited=collections.defaultdict(int)
	bfs('a',graph,visited)

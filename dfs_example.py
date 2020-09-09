import math,sys,os,collections,functools
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	n=int(input())
	arr=[['a','b'],['a','c'],['b','d'],['b','e'],['c','e'],['d','e'],['d','f']]
	def dfs(s,edges,visited):
		visited[s]=1
		print(s, end=' ')
		for i in range(len(edges[s])):
			if visited[edges[s][i]]==False:
				dfs(edges[s][i],edges,visited)

	edges=collections.defaultdict(list)
	for u,v in arr:
		edges[u].append(v)
		edges[v].append(u)
	visited=collections.defaultdict(int)
	dfs('a',edges,visited)

		                                          
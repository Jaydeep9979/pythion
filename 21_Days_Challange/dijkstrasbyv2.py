import math,sys,os,collections,functools,itertools
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	graph=[ [0, 1, 4, 0, 0,0],[1, 0, 4, 2, 7, 0],[4, 4, 0, 3, 5, 0],[0, 2, 3, 0, 4, 6],[0, 7, 5, 4, 0, 7],[0, 0, 0, 6, 7, 0]]
	def dijkstra(graph):
		v=len(graph)
		processed=[False]*len(graph)
		dist=[float('inf')]*len(graph)
		parent=[-1]*len(graph)
		# intialisation vertex
		dist[0]=0
		parent[0]=-1
		def SelectMinVertex(value,processed):
			vertex=0
			minimum=float('inf')
			for ver,dist in enumerate(value):
				if dist<minimum:
					vertex=ver
					minimum=dist
			return vertex


				
		for i in range(v-1):
			u=SelectMinVertex(dist,processed)
			processed[u]=True
			for j in range(v):
				if processed[j]==False and graph[u][j]!=0 and dist[u]!=float('inf') and dist[u]+graph[u][j]<dist[v]:
					dist[v]=dist[u]+graph[u][j]
					parent[j]=u
		
		
		








	dijkstra(graph)
from queue import PriorityQueue

class Graph:
	def __init__(self,num):
		self.graph=[[] for i in range(num)]
	
	def addEdge(self,u,v,cost):
		self.graph[u].append((v,cost))
		self.graph[v].append((u,cost))
		
		
	def bestFirstSearch(self,start,end):
		visited=[False for i in self.graph]
		queue=PriorityQueue()
		queue.put((-1,start))
		visited[start]=True
		path=[]
		
		while True:
			if not queue.empty():
				curr_node=queue.get()[1]
			else:
				break
			
			path.append(curr_node)
			
			if curr_node==end:
				print(path)
				break
			
			for node,cost in self.graph[curr_node]:
				if not visited[node]:
					visited[node]=True
					queue.put((cost,node))


					

graph=Graph(14)
graph.addEdge(0,1,3)
graph.addEdge(0,2,6)
graph.addEdge(0,3,5)
graph.addEdge(1,4,9)
graph.addEdge(1,5,8)
graph.addEdge(2,6,12)
graph.addEdge(2,7,14)
graph.addEdge(3,8,7)
graph.addEdge(8,9,5)
graph.addEdge(8,10,6)
graph.addEdge(9,11,1)
graph.addEdge(9,12,10)
graph.addEdge(9,13,2)
graph.bestFirstSearch(0,9) 
			
	

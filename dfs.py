class Graph:

	def __init__(self,num):
		self.v=num
		self.adj=[[] for i in range(self.v)]
		
	def addEdge(self,u,v):
		self.adj[u].append(v)
		self.adj[v].append(u)
	
	def dfs(self,s):
		visited=[False for i in range(self.v)]
		stack=[]
		
		stack.append(s)
		
		while(len(stack)):
			v=stack.pop()
			
			if (not visited[v]):
				print(v,end=" ")
				visited[v]=True
			
			for i in self.adj[v]:
				if (not visited[i]):
					stack.append(i)
		
	
		
g = Graph(5); # Total 5 vertices in graph 
g.addEdge(1, 0); 
g.addEdge(0, 2); 
g.addEdge(2, 1); 
g.addEdge(0, 3); 
g.addEdge(1, 4); 

print("Following is Depth First Traversal") 
g.dfs(0) 



import heapq

li=[]

edgeg={}
graph={}
vis={}
def heuristic(graph,u,v):
   heapq.heapify(li)
   node=u

   value=edgeg[node]
   while node != v:
      vis[node]=True
      print(node)
      for unode in graph[node]:
         if not vis[unode[0]]:
            heapq.heappush(li,(edgeg[node]+unode[1],unode[0]))
      nodeextract=heapq.heappop(li)
      node=nodeextract[1]
      # heapq.heappush(li,(edgeg[nodeextract[0]],))
   print(node)



def add_edge(graph,u,v,cost):
   # if graph.has_key(u):
   if u in graph:
      graph[u].append((v,cost))
   else:
      graph[u]=[]
      vis[u]=False
      graph[u].append((v,cost))
   # if graph.has_key(v):
   if v in graph:
      graph[v].append((u,cost))
   else:
      graph[v]=[]
      vis[v]=False
      graph[v].append((u,cost))


def edgeg_update(v,g):
   edgeg[v]=g



add_edge(graph,'a','b',1)
add_edge(graph,'a','c',1)
add_edge(graph,'a','d',1)
add_edge(graph,'b','e',1)
add_edge(graph,'b','f',1)
add_edge(graph,'c','g',1)
add_edge(graph,'c','h',1)
add_edge(graph,'d','i',1)
add_edge(graph,'d','j',1)


edgeg_update('a',38)
edgeg_update('b',17)
edgeg_update('c',9)
edgeg_update('d',27)
edgeg_update('e',5)
edgeg_update('f',10)
edgeg_update('g',3)
edgeg_update('h',4)
edgeg_update('i',15)
edgeg_update('j',10)

heuristic(graph,'a','e')
print('f')

import heapq

li=[]
edgeg={}
graph={}
vis={}

def a_star_heuristic(graph,u,v):
    heapq.heapify(li)
    node=u

    while node != v:
        vis[node]=True
        print(node,"->")
        for unode in graph[node]:
            if not vis[unode[0]]:
                heapq.heappush(li,(edgeg[node]+unode[1],unode[0]))
        nodeextract=heapq.heappop(li)
        node=nodeextract[1]
    print(node,"->")


def add_edge(graph,u,v,cost):
    if graph.has_key(u):
        graph[u].append((v,cost))
    else:
        graph[u]=[]
        vis[u]=False
        graph[u].append((v,cost))
    if graph.has_key(v):
        graph[v].append((u,cost))
    else:
        graph[v]=[]
        vis[v]=False
        graph[v].append((u,cost))


def edgeg_update(v,g):
    edgeg[v]=g



add_edge(graph,'a','b',4)
add_edge(graph,'a','c',3)
add_edge(graph,'b','f',5)
add_edge(graph,'b','e',12)
add_edge(graph,'c','e',10)
add_edge(graph,'c','d',7)
add_edge(graph,'d','e',2)
add_edge(graph,'f','g',16)
add_edge(graph,'e','g',5)



edgeg_update('a',14)
edgeg_update('b',12)
edgeg_update('c',11)
edgeg_update('d',6)
edgeg_update('e',4)
edgeg_update('f',11)

a_star_heuristic(graph,'a','g')
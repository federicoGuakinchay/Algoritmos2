class vertx():
    pi    = None
    d     = 10**1000
    
#grafo dirigido  y ponderado 
def create_a_graph_for_a_dijkstra(Vertices,Aristas):
    Graph = {}
    for v  in Vertices:
        Graph[v] = None
    columns = Graph.copy()
    for v in Vertices:
        Graph[v]= columns.copy()
    for (u,v,w) in Aristas:
        if w > 0:
            Graph[u][v] = w
            vertx_elements = vertx()
            Graph[u]['vertx_elements']=(vertx_elements) # init_relax 
    return Graph

'''def initRelax(G, s):
    for v in G:
        v.d = MAX_VALUE
        v.pi = None
    s.d = 0'''

'''def init_relax(G,s):
    for i in G.keys():
        vertx_elements = vertx()
        G[i]['vertx_elements']=(vertx_elements)
    G[s]['vertx_elements'].d = 0'''
    
'''def relax(u, v):
        if v.d > (u.d + w(u, v)):
            v.d = u.d + w(u, v)
            v.pi = u
'''
def relax(Graph,u, v):
    if (Graph[v]['vertx_elements'].d) > (Graph[u]['vertx_elements'].d + Graph[u][v]):
            Graph[v]['vertx_elements'].d = (Graph[u]['vertx_elements'].d + Graph[u][v])
            Graph[v]['vertx_elements'].pi = u
'''
def DIJKSTRA(G, s):
    initRelax(G, s)
    S = {}
    Q = minQueue(G.V)
    while len(Q) > 0:
        u = Q.dequeue()
        add(S, u)
        for v in u.adjunt():
            if v not in S:
                relax(u, v)
'''          
# Dijkstra
def Dijkstra(Graph, Source, Target):
    s = set()
    V = Graph.keys()
    Q = minQueue(Graph,V)
    while len(Q) > 0:
        u = Q.dequeue()
        s.add(Graph[u[0]])
        s.add(Graph[u[1]])
        for v in Graph(u):
            u.append(v)
            if Graph[u][v]!=None:
                if v not in s:
                    relax(u, v)
                
def minQueue(G,V):
    Q = []
    for i in V:
        for j in V:
            if  G[i][j] != None:
                a= (i,j)
                Q.append(a)
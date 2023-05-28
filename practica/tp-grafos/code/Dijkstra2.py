class vertx():
    pi    = None
    d     = 10**1000
    
#grafo dirigido  y ponderado 
def create_a_graph_for_a_dijkstra(Vertices,Aristas):
    Graph = {}
    for v  in Vertices:
        Graph[v] = {}
        vertx_elements = vertx()
        Graph[v]['vertx_elements']=(vertx_elements) # init_relax 
        
    for (u,v,w) in Aristas:
        if w > 0:
            Graph[u][v] = w
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
def relax(Graph , u , v):
    if (Graph[v]['vertx_elements'].d) > (Graph[u]['vertx_elements'].d + Graph[u][v]):
            Graph[v]['vertx_elements'].d = (Graph[u]['vertx_elements'].d + Graph[u][v])
            Graph[v]['vertx_elements'].pi = u
            return True
    else: return False
    
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
def Dijkstra(Graph , start_v , end_v):
    s = set()
    V = Graph.keys()
    Q = [start_v]
    Graph[start_v]['vertx_elements'].d = 0 
    while len(Q) > 0:
        u = Q.pop()
        s.add(u)
        for v in Graph[u]:
            if v != 'vertx_elements':
                continuar = relax(Graph , u , v)
                if v not in s or continuar == True:
                    Q.append(v)
                #relax(Graph , u , v)
                    
def print_graph(Graph):
    g = Graph.copy()
    for i in Graph.keys():
        print(i , end='  ')
        print(g[i].keys())

''' Test '''
vertices = [1,2,3,4,5,6,7,8,9,10]
Aristas = [(1,2,1),(1,4,1),(1,5,3),(1,6,5),(4,8,1),(5,6,1),(6,10,10),(8,9,1),(9,10,1)]       
G = create_a_graph_for_a_dijkstra(vertices,Aristas)  
print ('_____________Grafo_____________')
print_graph (G)
Dijkstra(G , 1 , 10)
print ('pi :  ',G[6]['vertx_elements'].pi)
print (' d :  ',G[6]['vertx_elements'].d )
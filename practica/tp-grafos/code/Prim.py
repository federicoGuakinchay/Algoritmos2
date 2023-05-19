my_set = {1,2,3,4,5,6}
set2   = my_set.copy()
print(my_set.difference(set2))
print (my_set.difference(set2)==set())
#las aristas seran  3-tuplas   donde  el primer elemento sera  el vertice de donde sale la arista
#el segundo sera el vertice al que llega  y el ultomo  será el peso de la arista .
def create_a_graph_MA(Vertices,Aristas):
    Graph = {}
    for v  in Vertices:
        Graph[v] = None
    columns = Graph.copy()
    for v in Vertices:
        Graph[v]= columns.copy()
    for (u,v,w) in Aristas:
        if w > 0:
            Graph[u][v] = w
    return Graph

'''def PRIM(Grafo): 
Descripción: Implementa el algoritmo de PRIM 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo'''

def PRIM (Graph): 
    T={}
    iter = Graph.keys()
    for v  in iter:
        T[v] = None
    columns = Graph.copy()
    for v in iter:
        T[v]= columns.copy()
    u=[iter(0)]
    for i in Graph.keys():
        v,v_peso = search_lca(u) # search low cost arist
        T[u][v] = v_peso
        u.append[v]
    return T 
        
def search_lca(Graph,u): 
    v_peso = 1000
    for i in u:
        for j in Graph[i]:
            if Graph[i][j] < v:
                v_peso = Graph[i][j]
                v = j 
    return v,v_peso 


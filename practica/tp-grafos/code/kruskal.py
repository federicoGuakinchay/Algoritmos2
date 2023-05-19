'''def KRUSKAL(Grafo): 
Descripción: Implementa el algoritmo de KRUSKAL 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo

def KRUSKAL(G):
A={}
for each v in G.V:
	make_set(v)
Esorted = sort_by_weight_asc(G.E)
for each (u, v) in Esorted:
if find_set(u) != find_set(v):
	insert(A, (u,v))
	union(u,v)
 
'''
def KRUSKAL(Graph): 
    A = {}
    v = set()
    u = set()
    iter = Graph.keys()
    for v in iter:
        v.add(v)
    E_sortered = sort_by_weight_asc(Graph)
    for i,j,peso  in E_sortered: 
        if (i in u) != (j  in  v ):
            A[i]={j:peso}
            u.add(i)
        elif (j in u) != (i  in  v ):
            A[j]={i:peso}
            u.add(i)
        if  u == v:
            return A

    

def sort_by_weight_asc(G):
    E_sortered = []
    m= G.copy()
    iter  = G.keys()
    for i in iter:
        for j in iter: 
            if i != j: 
                if m[i][j] > 0:
                    E_sortered.append((i,j,G[i][j]))
                    m[j][i]=0
    E_sortered.sort(key=lambda x:x[2])
    return (E_sortered)

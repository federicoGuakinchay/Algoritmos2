class vertex_element:
	value = None    
	d     = None    
	pi    = None    
	f     = None    
	colour = 'WHITE'

class aristas:
    elemnt  = None
    peso    = None
    
    
' Search the Vertix Whit More Conections '
def search_VWMC(Graph):
    iter = Graph.keys()
    long = 1
    for i in iter:
        long_i = Graph[i]
        if long_i > long:
            long = long_i
            v = i
    if long == 1 : 
        print('the Graph is empty')
        return(False)
    else:return v 


def create_a_graph_2 (Vertices,Aristas):
    Graph = {}
    for v  in Vertices:
        node = vertex_element()
        Graph[v] = [node]
    long=len(Aristas)
    cont = long 
    while cont != 0 : 
        tupla = Aristas[0]
        Graph[tupla[0]].append(tupla[1]) 
        Aristas.remove(Aristas[0])
        cont -=1
    return Graph

'''     Ejercicio 7
Implementar la función que responde a la siguiente especificación.
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
'''
def countConnections(Graph):
    iter = Graph.keys()
    cc    = 0   # count of conections
    for i in iter: 
        if Graph[i] !=[]:
            cc =+ (len(Graph[i])-1)
    return cc

'''     Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
'''
def convertToBFSTree(Graph):
    #comprovar que el grafo sea conexo 
    v = search_VWMC(Graph)#la raiz 
    L=[v]
    Graph[v][0].d = 0 
    Graph[v][0].colour = 'Gray'
    for i in Graph[v]:
        L.append (i)
    while L != []: 
        a = L[0]
        L.pop(0)
        Graph[a][0].colour = 'Black'
        end = len (Graph[a])
        for i in (1,end): 
            if Graph[i][0].colour == 'white':
                Graph[i][0].colour = 'Gray'
                Graph[i][0].pi     = a
                Graph[i][0].d      = Graph[a][0].d + 1
                L.append(i)
    return Graph            

                
    
'''     Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
'''
# utilizando un grafo dirigido..
def convertToDFSTree(Graph,v):
    time = 0
    DFS_Visit(Graph,v,time)
    iter = Graph.keys()
    for i in iter: 
        if Graph[i][0].colour == 'white': 
            DFS_Visit(Graph,i,time)

def DFS_Visit(Graph,u,time):
    time=+1
    Graph[u][0].d = time
    Graph[u][0].colour = 'Gray'
    for  i  in Graph[u]: 
        if Graph[i][0].coulour == 'white':
            Graph[i][0].pi = u 
            DFS_Visit(Graph,u,time)
    Graph[u][0].colour = 'Black'
    time=+1
    Graph[u][0].f = time
    

'''     Ejercicio 10
Implementar la función que responde a la siguiente especificación.
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
'''

'''Ejercicio 11 (Opcional)
Implementar la función que responde a la siguiente especificación.
def isBipartite(Grafo): 
Descripción: Implementa la operación es bipartito
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es bipartito.
'''
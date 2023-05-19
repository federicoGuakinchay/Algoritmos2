
    
"""
def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde 
            por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""

def create_a_graph (Vertices,Aristas,da=True): #da  = doble aristas... 
    #la lista de aristas se tomara como una lista de tuplas 
    #los vertices son unicos asi que se puede usar un diccionario para reconocerlos 
    Graph = {}
    for v  in Vertices :
        Graph[v]= []
    long=len(Aristas)
    cont = long 
    while cont != 0 : 
        tupla = Aristas[0]
        Graph[tupla[0]].append(tupla[1]) 
        if da == True :  
            Graph[tupla[1]].append(tupla[0])   
        Aristas.remove(Aristas[0])
        cont -=1
    return Graph

"""Ejercicio 2
Implementar la función que responde a la siguiente especificación.

def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los 
            vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
"""
def existPath(Graph, v1, v2): 
    Graph2 = create_empty_copiGraph(Graph)
    Graph2 = rellenar_Graph2_copi(Graph,Graph2,v1)
    return (Graph2[v2]!=[])
                    
def create_empty_copiGraph (Graph):
    iter = Graph.keys()
    Graph2={}
    for i in iter:
        Graph2[i] = []
    return Graph2

def rellenar_Graph2_copi(Graph, Graph2,v1):
    L =[]
    if Graph[v1] == [] or  Graph2 == []:
        return False
    else : 
        for i in Graph[v1]:
            L.append(i)
        while L != [] :
            a=L[0]
            if Graph2[a] == [] and Graph[a] != []: 
                for i in Graph[a]:
                    L.append(i)
                    Graph2[a].append(i) 
            L.pop(0)
    return Graph2
    
"""     Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
"""

def isConnected(Graph):
    Graph2 = create_empty_copiGraph(Graph)
    v = get_vertice(Graph)
    Graph2=rellenar_Graph2_copi(Graph,Graph2,v)
    iter = Graph.keys()
    for i in  iter:
        if Graph2[i] == []:
            return False 
    return True
    
def get_vertice(Graph):        
    iter = Graph.keys()
    for i in  iter:
        return(i)
"""
Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""
def isTree(Graph): 
    Graph2 = create_empty_copiGraph(Graph)
    v = get_vertice(Graph)
    Graph2=rellenar_Graph2_isTree(Graph,Graph2,v)
    if Graph2 == False:
        return False
    else:
        return True

def rellenar_Graph2_isTree(Graph, Graph2,v1):
    L =[]
    if Graph[v1] == [] or  Graph2 == []:
        return False
    else :
        frist= [v1] 
        for i in Graph[v1]:
            L.append(i)
            Graph2[v1].append(i)
        end = [i]
        while L != [] :
            a=L[0]
            if Graph2[a] == [] and Graph[a] != []: 
                for i in enumerate(Graph[a]):
                    if  i[1] != frist[0]:
                        L.append(i[1])
                        Graph2[a].append(i[1])
                        
                if i[1] != frist[0]:  
                    frist.append(a)
                    end.append(i[1])
                    
            elif  Graph2[a] != []:
                return False
            L.pop(0)
            if a == end [0]:
                end.pop(0)
                frist.pop(0)
    return Graph2
"""
Ejercicio 5 
Implementar la función que responde a la siguiente especificación.
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.

"""
def isComplete(Graph): 
    iter = Graph.keys()
    long = len (iter)-1
    for i in iter : 
        if long != len (Graph[i]):return False
    return True 

''''def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el 
grafo resultante se convierte en un árbol.'''

def convertTree(Graph):
    result = isConected_2(Graph)
    if result == False: 
        print ('hola')
        return False
    Graph2 = create_empty_copiGraph(Graph)
    v1 = get_vertice(Graph)
    Graph2 = rellenar_Graph2_copi(Graph,Graph2,v1)
    print(Graph2)
    lista = convertTree2(Graph2,v1)
    print(lista)
    
def convertTree2(Graph,v1):
    result = []
    if Graph[v1] == []:
        return False
    else :
        iter = Graph.keys() 
        for i in iter:
            for j in  Graph[i]:
                if Graph[j] == ['delete_aristas']:
                    tupla  = (i,j) 
                    result.append(tupla)
            Graph[i] = ['delete_aristas']        
    return result


def isConected_2(Graph): 
    Graph2  = create_empty_copiGraph(Graph)
    long    = 0 
    iter    = Graph.keys()
    for i in iter:
        long2= len(Graph[i])
        if long < long2:
            long = long2
            v1 = i 
    L =[v1]
    if Graph[v1] == [] or  Graph2 == []:
        return False
    else :
        Graph2[v1].append('nodo,conected') 
        while L != []:
            a = L[0] 
            L.remove(a)
            for i in Graph[a]:
                if Graph2[i]==[]:
                    L.append(i)
                    Graph2[i].append('nodo,conected')
        for i in iter:
            if Graph2[i] == []: 
                return False
        return True
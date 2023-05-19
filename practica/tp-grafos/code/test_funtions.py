from grafos import *
#grafo no conexo 
#L1=[1,2,3,4,5,6,7,88, 'esto es un nodo ',9]
#L2=[(1,4),(1,3),(3,4),(3,5),(4,2),(4,5),(2,6),(1,'esto es un nodo '),(7,88),(88,9),(7,9)]
#Grafo conexo 
L1=[1,2,3,4,5,6, 'esto es un nodo ']
L2=[(1,4),(1,3),(3,4),(3,5),(4,2),(4,5),(2,6),(1,'esto es un nodo ')]
#Grafo Arbol  
#L1=[1,2,3,4,5,6, 'esto es un nodo ']
#L2=[(1,4),(1,3),(1,'esto es un nodo '),(4,2),(4,5),(3,6)]
# grafo completo 
#L1=[1,2]
#L2=[(1,2)]
Graph  = create_a_graph(L1,L2)
print (Graph)
#result = existPath(Graph,1,'esto es un nodo ') # No funciona si el vertice no existe 
# tampoco fucion con grafos no simples  donde hay 2 aristas iguales 
#print (result)
result = isConnected(Graph)
print (result)
result = isTree(Graph)
print (result)
result = isComplete(Graph)
print (result)

L1=[1,2,3,4,5,6, 'esto es un nodo ']
L2=[(1,4),(1,3),(3,4),(3,5),(4,2),(4,5),(2,6),(1,'esto es un nodo ')]

'''Graph  = create_a_graph(L1,L2,da=False)
result = convertTree(Graph)
print(result)'''
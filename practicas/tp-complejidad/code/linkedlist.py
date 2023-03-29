class LinkedList:
	head=None
class Node:
	value=None
	key = None
	nextNode=None
#add(L,element) 
#Descripción: Agrega un elemento al comienzo de  L, siendo L una LinkedList que representa el TAD secuencia. 
#EntradaA: La Lista sobre la cual se quiere agregar el elemento (LinkedList)  y el valor del elemento (element) a  agregar.
#Salida:  No hay salida definida
def add(L,element,key=0): # O(f)=1
	nuevo_nodo= Node()
	nuevo_nodo.value = element   
	nuevo_nodo.key =  key                                             
	nuevo_nodo.nextNode = L.head
	L.head = nuevo_nodo

#search(L,element)
#Descripción: Busca un elemento de la lista que representa el TAD secuencia.
#Entrada: la lista sobre el cual se quiere realizar la búsqueda (Linkedlist) y el valor del elemento (element) a buscar.
#Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
def search (L,element): # O(f)= n
	currentnode=L.head
	cont=0
	while currentnode != None:
		if currentnode.key == element:
			return(currentnode.value)
		currentnode= currentnode.nextNode
		cont =cont +1
	return(None)
	
#insert(L,element,position)
#Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
#Entrada: la lista sobre el cual se quiere realizar la inserción (Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
#Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.
def insert (L,element, position): #O(f) = n
	cant_elementos=length(L)
	if position == 0:
		add(L,element) 
		return(0)
	elif cant_elementos<position:
		return(None)
	else:
		currentnode=L.head
		cont=0
		while currentnode != None:
			if position-1 == cont:
				nuevo_nodo= Node()
				nuevo_nodo.value = element
				nuevo_nodo.nextNode = currentnode.nextNode
				currentnode.nextNode = nuevo_nodo 
				return(cont+1)
			currentnode= currentnode.nextNode
			cont =cont +1

#delete(L,element)
#Descripción: Elimina un elemento de la lista que representa el TAD secuencia.
#Poscondición: Se debe desvincular el Node a eliminar.  
#Entrada: la lista sobre el cual se quiere realizar la eliminación (Linkedlist) y el valor del elemento (element) a eliminar.
#Salida: Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
def delete (L,element): #O(f)=n
	currentnode=L.head
	if L.head.key == element:
		valor = L.head.value
		L.head= currentnode.nextNode
		return(valor)
	else :
		cont=0
		while currentnode.nextNode != None:
			if currentnode.nextNode.key == element:
				valor = currentnode.nextNode.value
				currentnode.nextnode = currentnode.nextNode.nextNode
				return(valor)
			currentnode= currentnode.nextNode
			cont =cont +1
		return(None)

#length(L)
#Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
#Entrada: La lista sobre la cual se quiere calcular el número de elementos.
#Salida: Devuelve el número de elementos. 
def length (L): #O(f)=n
	currentnode=L.head
	cont=0
	while currentnode != None:	
		cont =cont +1
		currentnode= currentnode.nextNode
	return(cont)

#access(L,position)
#Descripción: Permite acceder a un elemento de la lista en una posición determinada.
#Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
#Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.
def access (L,position): #O(f)=n
	currentnode=L.head
	cant_elementos = length(L)
	if cant_elementos < position :
		return (None)
	else:	
		cont=0
		while currentnode != None:
			if cont == position:
				return(currentnode.value)
			currentnode= currentnode.nextNode
			cont =cont +1

#update(L,element,position)
#Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
#Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de  element. 
#Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.
def update (L,element, position): #O(f)=n
	cant_elementos=length(L)
	if position == 0:
		L.head.value=element
		return(0)
	elif cant_elementos<position+1:
		return(None)
	else:
		currentnode=L.head
		cont=0
		while currentnode != None:
			if position == cont:
				currentnode.value = element
				return(cont)
			currentnode= currentnode.nextNode
			cont =cont +1


#imprime una lista 
def print_list(L): #O(f)=n
	if L.head == None:
		return(L)
	currentnode=L.head
	while currentnode != None:
		print (currentnode.value, end=' ')
		currentnode= currentnode.nextNode
	print('')	
	return()

def add_in_end(L,element,key):
	currentnode=L.head
	cont=0
	while currentnode != None:	
		cont =cont +1
		if currentnode.nextNode == None:
			newnode = Node()
			newnode.value = element
			newnode.key = key
			currentnode.nextNode = newnode 
		currentnode= currentnode.nextNode
	return(cont)


#ordenamientos_______________________________________




#QuickSort  
def QuickSort(L):
  if L.head==None or L.head.nextNode==None:#primero eliminamos la opcion q nos puedan dar una lista vacio o una lista con un unico elemento
    return(L)
  else:
    Longitud=length(L)-1 #calcular la longitud 
    currentnode=L.head
    contador=length(L)
    while contador>1:
      contador=Comparador1(L,L.head.value,L.head,L.head,0,0,0,Longitud)
    if contador==0:
      currentnode=L.head
    else:
      currentnode=L.head.nextNode
    Longitud=Longitud-contador
    QuickSortRecursivo(L,currentnode.nextNode,currentnode,0,Longitud)

#esta funcion toma al primer pivote 'L.head' y ordena la lista en base a este.
#valor = pivote 
#PosicionOriginal= posicion del pivote
def Comparador1(L,valor,currentnode,currentnodeAnterior,contador,PosicionOriginal,posicion,Longitud):
  if posicion!=Longitud:
    if valor>currentnode.nextNode.value:
      Node=currentnode.nextNode #el nodo se eliminara de la lista y se cambiara la pocicion 
      currentnode.nextNode=currentnode.nextNode.nextNode
      FuncionCambia1(L,currentnodeAnterior,Node,PosicionOriginal)
      contador=contador+1
      contador=Comparador1(L,valor,currentnode,currentnodeAnterior,contador,PosicionOriginal,posicion+1,Longitud)
      return(contador)
    else:
      contador=Comparador1(L,valor,currentnode.nextNode,currentnodeAnterior,contador,PosicionOriginal,posicion+1,Longitud)
      return(contador)
  return(contador)

#aqui se cambia la pocicion 
def FuncionCambia1(L,currentnodeAnterior,Node,PosicionOriginal):
  if PosicionOriginal==0:
    Node.nextNode=L.head
    L.head=Node
  else:
    Node.nextNode=currentnodeAnterior.nextNode
    currentnodeAnterior.nextNode=Node

def QuickSortRecursivo(L,currentnode,currentnodeAnterior,posicion,Longitud):
    if Longitud>1:
      contador=Comparador(L,currentnode.value,currentnode,currentnodeAnterior,0,posicion,Longitud-1)
      if contador>1:
        QuickSortRecursivo(L,currentnodeAnterior.nextNode,currentnodeAnterior,0,contador) 
      resto=Longitud-contador
      if resto>1:
        QuickSortRecursivo(L,currentnode.nextNode,currentnode,0,resto-1)

def Comparador(L,valor,currentnode,currentnodeAnterior,contador,posicion,Longitud):
  if posicion!=Longitud:
    if valor > currentnode.nextNode.value:
      Node=currentnode.nextNode
      currentnode.nextNode=currentnode.nextNode.nextNode
      FuncionCambia(L,currentnodeAnterior,Node)
      contador=contador+1
      contador=Comparador(L,valor,currentnode,currentnodeAnterior,contador,posicion+1,Longitud)
      return(contador)
    else:
      contador=Comparador(L,valor,currentnode.nextNode,currentnodeAnterior,contador,posicion+1,Longitud)
      return(contador)
  return(contador)

def FuncionCambia(L,currentnodeAnterior,Node):
  Node.nextNode=currentnodeAnterior.nextNode
  currentnodeAnterior.nextNode=Node

"""   merge_sort  """

def Mergesort(L):
	left = LinkedList()
	right = LinkedList()
	result = LinkedList()
	longitud = length(L)
	if longitud <= 1:
		return (L)
	else:
		mitad = longitud // 2
		cont=0
		currentnode=L.head
		while currentnode != None:
			if cont < mitad:
				add(left,currentnode.value)
			else:
				add(right,currentnode.value)
			cont = cont +1
			currentnode= currentnode.nextNode
		left = Mergesort(left)
		right = Mergesort(right)
		if left == None:
			return(right)
		if right == None:
			return(left)
		currentleft=left.head
		if left.head != None and right.head != None:
			while currentleft.nextNode != None:
				currentleft=currentleft.nextNode 
			if currentleft.value <= right.head.value:
				currentleft.nextNode= right.head
				return (left)
		result = merge(left, right)
		return (result)

def merge(left, right):
	result=LinkedList()
	currentresult = Node()
	currentresult = result.head
	while length(left)> 0 or length(right) > 0:
		if left.head != None and right.head != None:
			if left.head.value <= right.head.value:
				if  result.head== None :
					a= left.head.nextNode
					left.head.nextNode= None
					result.head=left.head		
					left.head=None
					left.head= a
					currentresult= result.head

				else:		
					a= left.head.nextNode
					left.head.nextNode= None
					currentresult.nextNode=left.head		
					left.head=None
					left.head= a
					currentresult= currentresult.nextNode

			else:
				if result.head == None :
					a= right.head.nextNode
					right.head.nextNode= None
					result.head=right.head	
					right.head=None
					right.head= a
					currentresult= result.head

				else:
					a= right.head.nextNode
					right.head.nextNode= None
					currentresult.nextNode=right.head	
					right.head=None
					right.head= a
					currentresult= currentresult.nextNode

		if length(left) > 0  and right.head== None:
			a= left.head.nextNode
			left.head.nextNode= None
			currentresult.nextNode=left.head	
			left.head=None
			left.head= a
			currentresult= currentresult.nextNode

		if length(right) > 0 and left.head== None:		
			a= right.head.nextNode
			right.head.nextNode= None
			currentresult.nextNode=right.head		
			right.head=None
			right.head= a
			currentresult= currentresult.nextNode
	return (result)
	print('')
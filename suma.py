from linkedlist import *


def ContieneSuma(L,a):
	if L.head == None :
		return(False)
	if L.head.nextNode ==  None:
		return(False)
	r = Suma_total(L)
	if r <= a :
		return(False)
	elif r == a :
		return(True)
	else :
		r=Ultmia_Suma(L,a)
	return(r)

# si sumado todos los numeros de la lista aun asi queda como resultado a un numero menor
# a n entonses jamas seria posible
def Suma_total(L):
	currentnode = L.head
	sumaT = 0
	while currentnode != None:	
		sumaT =  sumaT + currentnode.value
		currentnode = currentnode.nextNode
	return(sumaT)

def Ultmia_Suma(L,a):
	currentnode = L.head
	sum_node 		= L.head
	valor 			= 0
	while sum_node != None:
		if sum_node.value <= a  :
			currentnode = L.head
			while currentnode != None:
				if sum_node.value + currentnode.value <= a  and currentnode != sum_node:
					valor = sum_node.value + currentnode.value
					if valor == a:
						return(True)
					else: 
						currentnode=currentnode.nextNode
				else:
					currentnode=currentnode.nextNode
		sum_node = sum_node.nextNode
	return(False)

'''Ejercicio 4:
Implementar un algoritmo que ordene una lista de elementos 
donde siempre el elemento del medio de la lista contiene 
antes que él en la lista la mitad de los elementos menores 
que él. Explique la estrategia de ordenación utilizada.
'''
def ordenar (lista):
	long		= len(lista)
	cont= 1
	if long % 2 == 0: 
		a  =  long/2
	else:
		a	 =  long//2 + 1
	L = []
	M = []
	for i in (long-1):
		if lista[i] < a:
			L.append(lista[i])			
		else:
			M.append(lista[i])
	ordenar2(L)
	ordenar2(M)
	cont = 0
	for a in lista:
		L.append(M[cont])
		cont =+ 1
		
def ordenar2(L):
	for i in L:
		j=i
		for j in L: 
			if L[i]<L[j]:
				a = L[i]
				L[i] = L[j]
				L[j] = a 

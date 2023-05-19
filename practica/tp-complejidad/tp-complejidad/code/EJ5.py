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

print("ingresar lista de numeros (A)")
L=LinkedList()
cont=0
add(L,0)
add(L,5)
add(L,5)
add(L,9)
add(L,5)
n=10
print("lista")
print_list(L)
r = ContieneSuma(L,n)
print ("contiene suma?")
print(r)

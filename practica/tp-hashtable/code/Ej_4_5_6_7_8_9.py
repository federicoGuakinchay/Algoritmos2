from my_dictionary import *

'''
Ejercicio 4
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente 
proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de 
p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la 
solución propuesta.

Ejemplo 1:
Entrada: S = ‘hola’ , P = ‘ahlo’
Salida: True, ya que P es una permutación de S

Ejemplo 2:
Entrada: S = ‘hola’ , P = ‘ahdo’
Salida: Falso, ya que P tiene al carácter ‘d’ que no se encuentra en S por lo que no es una 
permutación de S
'''
def es_permutacion(str1,str2): 
    D ,L_ab= create_hashtable(28,20)
    long1 = str1.__len__()
    long2 = str2.__len__()
    if long1 != long2:
        return False
    else : 
        for i in range (0,long1): 
            hash_insert(D,L_ab,str1[i],str1[i])
        for i in range (0,long1): 
            r=hash_search(D,L_ab,str1[i],str1[i])
            if r == False:
                return False
        return True

'''
Ejercicio 5
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus 
elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución 
propuesta.

Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición
'''

def ej5(L):
    D ,L_ab= create_hashtable(28,20)
    for i in range(0,len(L)):
        if i == 0:
            hash_insert(D,L_ab,L[i],L[i])
        else:
            r=hash_search(D,L_ab,L[i],L[i])
            if r == True: 
                return False
            else:
                hash_insert(D,L_ab,L[i],L[i])
                
'''
Ejercicio 6
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter 
(A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que 
representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar 
una función de hash apropiada para los códigos postales argentinos.
'''

def codigospostales(codigo,direccion):
    long = codigo.__len__()
    if long != 8:
        return False
    a = codigo[1]+codigo[2]+codigo[3]+codigo[4]
    b = codigo[0]+codigo[5]+codigo[6]+codigo[7]
    ra = a.isnumeric()
    rb = b.isalpha()
    if ra == False or rb == False:
        return False
    D ,L_ab= create_hashtable(28,20)
    a = int(a)
    for i in range(0,long):
        if i == 0:
            hash_insert_codigopostal(D,L_ab,a,codigo,direccion)
        else:
            r=hash_search_codigopostal(D,L_ab,a,codigo,direccion)
            if r == True: 
                print('la direccion ya fue ingresada')
                return False
            else:
                hash_insert_codigopostal(D,L_ab,a,codigo,direccion)

'''Ejercicio 7
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de 
caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. 
Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería 
devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y 
minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
'''
def ej7(cadena):
    b = cadena.isalpha()
    if b == False:
        return False
    anterior = None
    for i in range(0,len(cadena)):
        if cadena[i] == anterior:
            cont += 1
        else:
            result   = result + str(cadena[i]+str(cont))
            anterior = cadena[i]
            cont = 0
    result   = result + str(cadena[i]+str(cont))
    
'''Ejercicio 8
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. 
Implementar esta estrategia de la forma más eficiente posible con un costo computacional 
menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo de la solución 
propuesta.

Ejemplo 1:
Entrada: S = ‘abracadabra’ , P = ‘cada’
Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)'''

def ej8 (cadena1,cadena2):
    long1 = cadena1.__len__()
    long2 = cadena2.__len__()
    if long1 <= long2: 
        return False
    cont = 0
    result = 0
    for i in range (0,long1):
        if cadena1[i] == cadena2[cont]:
            cont += 1
        else: 
            if result < cont : 
                result = cont

'''Ejercicio 9
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un 
algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). 
¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
'''

def ej9 (s,t):
    long1 = len(s)
    long2 = len(t)
    D ,L_ab= create_hashtable(28,20)
    if long1 <= long2:
        return False
    for i in range (0,long2):
        hash_insert(D,L_ab,t[i],t[i])
    for i in range (0,long1): 
        r=hash_search(D,L_ab,s[i],s[i])
        if r == False:
            return False
    return True

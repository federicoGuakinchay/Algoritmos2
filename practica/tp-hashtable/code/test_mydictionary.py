from my_dictionary import *


D ,L_ab= create_hashtable(28,20)

print_hahs_table(D)

input('pres enter to continue:')
print('comprobando el insert')
print('')
hash_insert(D,L_ab,20,'hola_20')
hash_insert(D,L_ab,66,'hola_66')
hash_insert(D,L_ab,20,'hola_13')
hash_insert(D,L_ab,54,'hola_54')
hash_insert(D,L_ab,84,'hola_84')
hash_insert(D,L_ab,96,'hola_96')
hash_insert(D,L_ab,102,'hola_102')
hash_insert(D,L_ab,204,'hola_204')
hash_insert(D,L_ab,22,'hola_22')
hash_insert(D,L_ab,21,'hola_21')
print_hahs_table(D)
input('pres enter to continue:')
print('buscando el search key 66')

a=hash_search(D,L_ab,66)
print(a)
print('buscando el search la key 4')

a=hash_search(D,L_ab,4)
print(a)

input('pres enter to continue:')
print('borrando el  key 4')
r=hash_delete(D,L_ab,4)
print(r)
print('borrando el  key 66')
r=hash_delete(D,L_ab,66)
print(r)
print_hahs_table(D)


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
    long1 = str1.__len__()
    long2 = str2.__len__()
    if long1 != long2:
        return False
    else : 
        for i in range (0,long1): 
            hash_insert(str1[i],L_ab,20,'hola_20')

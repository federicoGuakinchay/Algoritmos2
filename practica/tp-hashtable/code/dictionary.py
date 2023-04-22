def create_dictionary(a):
    d =[]
    for i in range (0,a):
       d.append([])
    return(d)

'''
insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  
en el diccionario (dictionary). Resolver colisiones por encadenamiento. 
En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a 
insertar 
Salida: Devuelve D
'''
def insert (D,key,value):
    position = key % 11
    print(f'porition = {position}')
    D[position].append (value)
    return(D)
        
'''
search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor 
del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
'''        
def search(D,key):
    position = key % 11    
    if D[position] == []:
        return None
    else: return D[position]
    
    
'''
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) 
del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que 
se va a eliminar.
Salida: Devuelve D

'''
def delete(D,key):
    position = key % 11    
    if D[position] == []:
        return D
    else: 
        D[position] = []
        return D

    
    
    ''' a little test '''
D = create_dictionary(11)
print(D)
print(f'mod 54{54 % 11}')
insert(D,20,'hola_20')
insert(D,66,'hola_66')
insert(D,20,'hola_13')
#insert(D,54,'hola_54')
insert(D,84,'hola_84')
insert(D,96,'hola_96')
insert(D,102,'hola_102')
insert(D,204,'hola_204')
insert(D,22,'hola_22')
insert(D,21,'hola_21')

a=search(D,66)
print(a)
a=search(D,4)
print(a)
D=delete(D,4)
print(D)
D=delete(D,66)
print(D)

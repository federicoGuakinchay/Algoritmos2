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

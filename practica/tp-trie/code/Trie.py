class Trie:
	root = None

class TrieNode:
  parent = None
  children = None  
  key = None
  isEndOfWord = False

''' insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida '''
def insert(T,element):
    element  = str(element)  
    element   =   element.upper()
    seguir = element.isalpha()
    end = len(element)
    if  seguir == True:
        cont=0
        if T == None:
            T = Trie()
        elif T.root == None:
            new_node = TrieNode()    
            T.root = new_node
            currentree = T.root
        else :
            currentree = T.root
        insert_recursive(currentree,element,cont,end)
    else: 
        print('cadena no es valida :  usar solo letras a-z A-Z (sin espacios) ')
        return()     
    

def insert_recursive(currentree,element,cont,end):
    
    if currentree.children == None:
        
        currentree.children = list([])
    
    find = search_element(currentree.children,element[cont])  

    if find == None:    

        New_node = TrieNode()
        New_node.key = element[cont]
        New_node.parent = currentree
        currentree.children.append(New_node)
        a=len(currentree.children)
        find = currentree.children[a-1]
        
    if end == cont+1:
    
        find.isEndOfWord = True
        return()    
        
    insert_recursive(find,element,cont+1,end)
    return()
        
        
def search_element(L,element):
    a=len(L)
    if a == 0 :
        return(None)
    #else: a= a-1
    for i in range (0,a):
        if L[i].key == element : 
            return(L[i])
    return(None)



'''search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento.
'''
def search (T,element,return_node=False):
    element  = str(element)  
    element  = element.upper()
    seguir   = element.isalpha()
    end = len(element)
    if  seguir == True:
        cont=0
        if T == None:
            print ('No hay arbol:')
            return(False)
        elif T.root == None:
            print ('el arbol esta vacio')
            return(False)
        else :
            currentree = T.root
            find = recursive_search(currentree,element,cont,end)
            if return_node == False:
                if find != False:
                    find = find.isEndOfWord
                return(find)
            else: 
                return(find)
    else: 
        print('la cadena buscada no es valida :  usar solo letras a-z A-Z (sin espacios) ')
        return(False)      

def recursive_search(currentree,element,cont,end):

    if end == cont+1:

        find = search_element(currentree.children,element[cont])

        if find == None:
            return(False)
        else:
            return(find)
    find = search_element(currentree.children,element[cont])
    if find == None:
        return(False)
    else:
        
        find = recursive_search(find,element,cont+1,end)
        return(find)
    
'''delete(T,element)
	Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento.
'''

def delete(T,element):
    currenttre=search(T,element,True)
    if currenttre == False:
        print('palabra no encontrada en el trie ') 
        return (False)
    if currenttre.isEndOfWord == True:
        currenttre.isEndOfWord = False
    if currenttre.children == None:
        hijos = 0    
        while currenttre.parent != None and hijos == 0:
            if currenttre.isEndOfWord == True:
                currenttre.isEndOfWord = False
            if currenttre.children == None: 
                currenttre.parent.children.remove(currenttre)
            else: 
                return(True)
            currenttre= currenttre.parent            
            hijos = len(currenttre.children) 
            if currenttre.isEndOfWord == True:
                return(True)
        return(True)
    else: return (True)      

'''Ejercicio 4
Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas 
las palabras del árbol que empiezan por p y sean de longitud n. 
'''
           
def search_and_concat(T,patron,long):
    long_p= len(patron)
    if long_p >= long:
        return(False)
    else: 
        currentree = search(T,patron,return_node=True)
        end = long - long_p
        cont= 0 
        concat = patron.upper()
        list_of_words = []          
        list_of_words = recursive_search_and_concat(currentree,cont,end,list_of_words,concat)
        if list_of_words == []:
            return(False)
        else: 
            return(list_of_words)


def recursive_search_and_concat(currentree,cont,end,list_of_words,concat):
    if cont+1 <= end:
        if  currentree.children == None:
            return (list_of_words)
        a = len(currentree.children)
        if a != 0: 
            for i  in range (0,a):
                newconcat= concat+(str(currentree.children[i].key))
                if cont+1 != end:
                    list_of_words=recursive_search_and_concat(currentree.children[i],cont+1,end,list_of_words,newconcat)
                else: 
                    if currentree.children[i].isEndOfWord ==  True:
                        list_of_words.append(str(newconcat))   
            return(list_of_words)
        else: 
            return (list_of_words)
    else:
        return(list_of_words)       
     
'''Ejercicio 5
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo 
documento y False en caso contrario. Se considera que un 
Trie pertenecen al mismo documento cuando:
Ambos Trie sean iguales (esto se debe cumplir)
Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan 
sido insertadas en un orden diferente.
En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 
Analizar el costo computacional.
'''
def Trie_iguales(T1,T2):
    if T1 == None and T2 == None:
        print ('no hay arboles :')
        return(True)
    elif T1 == None or T2 == None:
        print ('un arbol esta vacio:')
        return(False)
    if T1.root == None and T2.root == None:
        print ('el arbol esta vacio')
        return(False)
    elif T1.root == None or T2.root == None:
        print ('uno de los arboles esta vacio')
        return(False)
    currentree = T1.root 
    list_of_words = []  
    concat =''           
    list_of_words = recursive_search_and_concat_EJ7(currentree,list_of_words,concat)
    print(list_of_words)
    long = len(list_of_words)
    for i in range (0,long): 
        seguir = search (T2,list_of_words[i])
        if seguir == False:
            return(False)
    return(True)
        
    


'''Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos 
cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a 
derecha y contiene los mismos caracteres que si se lee de derecha a izquierda,
ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin 
embargo abcd y dcka no son invertidas ya que difieren en un carácter.'''

def search_ci(T,cadena):
    result = search(T,cadena)
    if result == False:
        return(False)
    cadena2 = revertir_cadena(cadena)
    result = search(T,cadena2)
    return(result)

def revertir_cadena(cadena):
    a = len (cadena)
    newcadena = ''
    for i in range (0,a):
        newcadena = newcadena + cadena[a-i-1]
    return(newcadena)

'''Ejercicio 7:
Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su 
diccionario. Queremos añadir una función de auto-completar 
(al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una palabra, 
si sólo existe una forma correcta de continuarla entonces debemos indicarlo. 
Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el 
árbol Trie T y la cadena “pal” devuelve la forma de auto-completar 
la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, ya 
que podemos tener “groenlandia” o “groenlandés” 
(en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que 
representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. 
Por ejemplo, autoCompletar(T, ma’) devolvería “” si T presenta las cadenas “madera” y “mama”. 
'''

def search_and_concat_EJ7(T,patron,none_patron = False):
    long_p= len(patron)
    if long_p <= 0 :
        return(False)
    else: 
        currentree = search(T,patron,return_node=True)
        concat = patron.upper()
        list_of_words = []             
        list_of_words = recursive_search_and_concat_EJ7(currentree,list_of_words,concat)
        if list_of_words == []:
            return(False)
        else: 
            return(list_of_words)


def recursive_search_and_concat_EJ7(currentree,list_of_words,concat):
    if  currentree.children == None:
        return (list_of_words)
    if currentree.children == []:
        return(list_of_words)
    a = len(currentree.children)
    if a != 0: 
        for i  in range (0,a):
            newconcat= concat+(str(currentree.children[i].key))
            list_of_words=recursive_search_and_concat_EJ7(currentree.children[i],list_of_words,newconcat)
            if currentree.children[i].isEndOfWord ==  True:
                list_of_words.append(str(newconcat))   
        return(list_of_words)
    else: 
        return (list_of_words)

    
